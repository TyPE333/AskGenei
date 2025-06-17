# biomed_assist/core.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
from retrieval import fetch_pubmed_abstracts, is_valid_abstract_context, build_rag_prompt, truncate_prompt

def load_model(model_id="microsoft/phi-1.5", max_tokens=256):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto").eval()
    for param in model.parameters():
        param.requires_grad = False
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=device, max_new_tokens=max_tokens)

def answer_question(pipe, question: str) -> dict:
    abstracts = fetch_pubmed_abstracts(question, max_results=3)
    tokenizer = pipe.tokenizer
    if not is_valid_abstract_context(abstracts):
        prompt = f"Q: {question}\nA:"
        mode = "direct"
        max_tokens = 1024
    else:
        prompt = build_rag_prompt(question, abstracts)
        mode = "retrieval"
        max_tokens = 2048

    prompt = truncate_prompt(prompt, tokenizer, max_tokens=max_tokens)
    response = pipe(prompt)[0]["generated_text"]
    return {
        "answer": response.strip(),
        "mode": mode,
        "abstracts": abstracts
    }
