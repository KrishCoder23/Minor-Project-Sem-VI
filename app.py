import streamlit as st

# Configure the page
st.set_page_config(page_title="NCERT Q-Gen | Landing", layout="wide", initial_sidebar_state="collapsed")

# Inject the Native HTML and CSS directly into Streamlit's DOM
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp {
        background-color: #0b0f19;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide the top bar and sidebar button to make it look like a real website */
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {display: none;}
    
    /* Decorative Background Glow */
    .glow-bg {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 800px;
        height: 800px;
        background-color: rgba(8, 145, 178, 0.15); /* Cyan glow */
        border-radius: 50%;
        filter: blur(120px);
        z-index: 0;
        pointer-events: none;
    }

    .landing-container {
        position: relative;
        z-index: 10;
        text-align: center;
        max-width: 800px;
        margin: 100px auto;
    }

    .badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 9999px;
        border: 1px solid rgba(6, 182, 212, 0.3);
        background-color: rgba(6, 182, 212, 0.1);
        color: #22d3ee;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 24px;
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 24px;
        line-height: 1.1;
    }

    .subtitle {
        font-size: 1.125rem;
        color: #94a3b8;
        margin-bottom: 40px;
        line-height: 1.6;
    }

    /* THE MAGIC BUTTON STYLING */
    .try-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 16px 32px;
        font-size: 16px;
        font-weight: bold;
        color: white !important;
        background-color: #0891b2;
        border-radius: 8px;
        text-decoration: none !important;
        box-shadow: 0 0 20px rgba(8,145,178,0.4);
        transition: all 0.2s;
    }
    .try-btn:hover {
        background-color: #06b6d4;
        box-shadow: 0 0 30px rgba(8,145,178,0.6);
        transform: translateY(-2px);
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        margin-top: 80px;
        padding-top: 48px;
        border-top: 1px solid #1e293b;
        text-align: left;
    }
    
    .feature-title {
        font-weight: bold;
        color: white;
        margin-bottom: 8px;
        font-size: 16px;
    }
    .feature-desc {
        font-size: 14px;
        color: #64748b;
    }
</style>

<div class="glow-bg"></div>

<div class="landing-container">
    <div class="badge">Llama 3.2 Powered</div>
    
    <h1 class="main-title">NCERT Question Generator</h1>
    
    <p class="subtitle">
        A fully offline, low-resource AI assistant designed to generate curriculum-specific assessments across all six levels of Bloom's Taxonomy.
    </p>

    <a href="/chatbot" target="_self" class="try-btn">🚀 Try It Now</a>

    <div class="features-grid">
        <div>
            <div class="feature-title">100% Offline</div>
            <div class="feature-desc">Absolute privacy with zero cloud API dependencies.</div>
        </div>
        <div>
            <div class="feature-title">Low-Resource</div>
            <div class="feature-desc">Optimized to run natively on under 4GB of VRAM.</div>
        </div>
        <div>
            <div class="feature-title">Bloom's Aligned</div>
            <div class="feature-desc">Cognitively diverse questions mapped to the NCERT syllabus.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)