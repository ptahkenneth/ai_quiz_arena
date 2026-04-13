 
import random

def get_question():
    questions = [
        {"question": "What does AI stand for?",
         "options": ["Artificial Intelligence", "Automated Input", "Advanced Internet"],
         "correct": "Artificial Intelligence"},
        {"question": "Which is a popular AI framework?",
         "options": ["TensorFlow", "Photoshop", "Excel"],
         "correct": "TensorFlow"}
    ]
    return random.choice(questions)
