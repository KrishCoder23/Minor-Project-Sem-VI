

import csv
import json


csv_filename = 'dataset.csv'
jsonl_filename = 'dataset.jsonl'

print("🔄 Starting the conversion process...")


with open(csv_filename, mode='r', encoding='utf-8') as csv_file, \
     open(jsonl_filename, mode='w', encoding='utf-8') as jsonl_file:
    

    reader = csv.DictReader(csv_file)
    
    count = 0
    for row in reader:
 
        topic = row.get('Topic', 'General')
        explanation = row.get('Explanation', '')
        difficulty = row.get('Difficulty', 'Medium')
        grade = row.get('grade', 'Class')
        subject = row.get('subject', 'Subject')
        q_type = row.get('QuestionType', 'Question')
        question = row.get('Question', '')
        answer = row.get('Answer', '')
        

        if not question:
            continue

        instruction = f"Generate a {difficulty} {q_type} for {grade} {subject}."
        input_text = f"Topic: {topic}\nContext: {explanation}"
        output_text = f"Question: {question}\nAnswer: {answer}"
        

        flashcard = {
            "instruction": instruction,
            "input": input_text,
            "output": output_text
        }
        

        json.dump(flashcard, jsonl_file)
        jsonl_file.write('\n')
        count += 1

