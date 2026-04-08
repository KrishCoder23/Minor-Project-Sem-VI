

import csv
import json

# The names of our files
csv_filename = 'dataset.csv'
jsonl_filename = 'dataset.jsonl'

print("🔄 Starting the conversion process...")

# Open the CSV to read, and the JSONL to write
with open(csv_filename, mode='r', encoding='utf-8') as csv_file, \
     open(jsonl_filename, mode='w', encoding='utf-8') as jsonl_file:
    
    # This reads the CSV headers automatically
    reader = csv.DictReader(csv_file)
    
    count = 0
    for row in reader:
        # 1. Grab the data from your specific columns
        topic = row.get('Topic', 'General')
        explanation = row.get('Explanation', '')
        difficulty = row.get('Difficulty', 'Medium')
        grade = row.get('grade', 'Class')
        subject = row.get('subject', 'Subject')
        q_type = row.get('QuestionType', 'Question')
        question = row.get('Question', '')
        answer = row.get('Answer', '')
        
        # Skip empty questions just to keep the dataset clean
        if not question:
            continue
            
        # 2. Format it into the "AI Brain" structure
        instruction = f"Generate a {difficulty} {q_type} for {grade} {subject}."
        input_text = f"Topic: {topic}\nContext: {explanation}"
        output_text = f"Question: {question}\nAnswer: {answer}"
        
        # 3. Create the final dictionary
        flashcard = {
            "instruction": instruction,
            "input": input_text,
            "output": output_text
        }
        
        # 4. Write it to the new file
        json.dump(flashcard, jsonl_file)
        jsonl_file.write('\n')
        count += 1

print(f"✅ Success! Converted {count} questions into perfect AI flashcards.")
print("📁 Your new 'dataset.jsonl' file is ready for Google Colab!")