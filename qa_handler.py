#Soru-cevap verilerini yükleyip en iyi eşleşmeyi bulan modül.
#***********************************************************************

import os  # Import OS module for file handling
import json  # Import JSON module for data storage
from rapidfuzz import process  # Import fuzzy matching for best answer selection

file_path = "sorular.json"  # Define the question-answer database file

def load_qa_data():
    if not os.path.exists(file_path):  # Check if the file exists
        print("Soru-cevap veritabanı bulunamadı.")
        return {}

    with open(file_path, "r", encoding="utf-8") as file:  # Open JSON file
        try:
            return json.load(file)  # Load question-answer data
        except json.JSONDecodeError:  # Handle JSON format errors
            print("Dosya bozuk veya yanlış formatta.")
            return {}

def find_best_answer(question, qa_dict):
    if not qa_dict:  # Check if data exists
        return "Üzgünüm, şu anda veritabanım boş."

    questions = list(qa_dict.keys())  # Extract all stored questions
    best_match, score, _ = process.extractOne(question, questions)  # Find the best match
    if score > 80:  # Accept answer if confidence score is high
        return qa_dict[best_match]
    return "Üzgünüm, bu soruya uygun bir cevabım yok."  # Return default response
