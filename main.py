from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
import json
from llama_cpp import Llama

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell FastAPI where your HTML files are
templates = Jinja2Templates(directory="templates")

# --- 🧠 LOAD THE AI MODEL ---
# This runs once when you start the server so it's instantly ready for chat
print("Loading Llama 3.2 model... This might take a few seconds.")
llm = Llama(model_path="models/llm/model.gguf", n_ctx=2048, n_gpu_layers=-1, verbose=False)
print("Model loaded successfully!")

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page(request: Request):
    """Serves the index.html landing page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def serve_login_page(request: Request):
    """Serves the role selection login page"""
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/chatbot", response_class=HTMLResponse)
async def serve_chat_page(request: Request):
    """Serves the chat.html interface"""
    return templates.TemplateResponse("chat.html", {"request": request})

# --- ⚡ AI API ENDPOINT ---

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    prompt: str
    history: List[ChatMessage] = []
    subject: str = "General"
    grade: str = "General"
    bloom: str = "Understand"
    role: str = "student"

@app.post("/api/generate")
async def generate_response(req: ChatRequest):
    """Takes the user's text, history, and context from JS, streams it through Llama 3.2, and returns SSE chunks"""
    
    # 1. Build advanced instructions based on ROLE
    if req.role == "teacher":
        system_instruction = (
            "You are a professional AI teaching assistant for the Indian NCERT syllabus. "
            f"The teacher is focusing on {req.subject} for {req.grade} at the '{req.bloom}' cognitive level of Bloom's Taxonomy. "
            "Help the teacher design assessments, rubrics, and lesson plans directly and clearly."
        )
    else:
        system_instruction = (
            "You are a helpful, patient AI tutor for the Indian NCERT syllabus. "
            f"The student is learning {req.subject} for {req.grade} focusing on the cognitive goal of '{req.bloom}'. "
            "Explain concepts clearly, provide age-appropriate examples, and guide the student without immediately giving away direct answers."
        )
    
    chat_history = [{"role": "system", "content": system_instruction}]
    
    # Append past history
    for msg in req.history:
        chat_history.append({"role": msg.role, "content": msg.content})
        
    # Append the latest prompt
    chat_history.append({"role": "user", "content": req.prompt})
    
    # 2. Generator for Streaming Response
    def llm_generator():
        output = llm.create_chat_completion(
            messages=chat_history,
            max_tokens=600,
            temperature=0.7,
            stream=True
        )
        for chunk in output:
            delta = chunk["choices"][0]["delta"]
            if "content" in delta:
                content = delta["content"]
                # Must be Server-Sent Events (SSE) string format
                yield f"data: {json.dumps({'content': content})}\n\n"
        
        yield "data: [DONE]\n\n"
        
    # 3. Stream data back to Javascript fetch
    return StreamingResponse(llm_generator(), media_type="text/event-stream")