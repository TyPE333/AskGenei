# /api/main.py
from fastapi import FastAPI, Query
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import load_model, answer_question

app = FastAPI()
pipe = load_model()

@app.get("/answer")
def get_answer(question: str = Query(...)):
    result = answer_question(pipe, question)
    return result
