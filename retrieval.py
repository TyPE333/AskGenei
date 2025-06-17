# biomed_assist/retrieval.py
from Bio import Entrez

Entrez.email = "your_email@example.com"

def fetch_pubmed_abstracts(query: str, max_results: int = 3) -> str:
    query = f"{query} AND (nanopore OR basecalling OR ONT)"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    ids = Entrez.read(handle)["IdList"]
    handle.close()
    if not ids: return "No relevant abstracts found."
    handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="abstract", retmode="text")
    abstracts = handle.read()
    handle.close()
    return abstracts.strip()

def is_valid_abstract_context(text: str) -> bool:
    return not ("No relevant abstracts" in text or len(text) < 300 or "MAFLD" in text or "splicing" in text.lower())

def build_rag_prompt(question: str, abstracts: str) -> str:
    return (
        "You are a biomedical research assistant.\n"
        "Use the following PubMed abstracts to answer the question below.\n\n"
        f"PubMed Abstracts:\n{abstracts}\n\n"
        f"Question: {question}\n\nAnswer:"
    )

def truncate_prompt(prompt: str, tokenizer, max_tokens: int) -> str:
    tokens = tokenizer.encode(prompt, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens, skip_special_tokens=True)
