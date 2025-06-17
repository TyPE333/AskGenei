# AskGenei: A Biomedical Research Assistant

A lightweight Retrieval-Augmented Generation (RAG) system to answer biomedical research questions using PubMed abstracts and a local language model like `microsoft/phi-1_5` or `phi-2`.


---

## Features

- Retrieves real PubMed abstracts using `Bio.Entrez`
- Generates natural language answers using local LLMs (e.g. Phi-2)
- Fallback to direct LLM inference when no useful abstracts are found
- Modular Python package structure for reuse or extension
- FastAPI backend + Streamlit UI

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/biomed-assistant.git
cd biomed-assistant
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Option 1: Run FastAPI + Streamlit manually

#### Start FastAPI backend

```bash
uvicorn biomed_assist.api.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Start Streamlit UI

In a second terminal:

```bash
streamlit run biomed_assist/ui/app.py
```

### Option 2: Run with a helper script (Linux/macOS)

```bash
chmod +x run.sh
./run.sh
```

---

## Usage

Ask biomedical research questions like:

* *"What are the recent improvements in nanopore basecalling?"*
* *"How is CRISPR being used to treat cancer?"*

The assistant will:

* Try to retrieve relevant abstracts from PubMed
* Compose a context-aware prompt for the LLM
* Fallback to a direct answer if abstracts are off-topic

---

## Project Structure

```
biomed_assist/
├── __init__.py
├── core.py              # LLM loading + answer generation
├── retrieval.py         # PubMed search + prompt building
├── api/
│   └── main.py          # FastAPI backend
├── ui/
│   └── app.py           # Streamlit frontend
├── run.sh               # Script to launch API + UI
├── requirements.txt     # All Python dependencies
└── README.md
```

---

## System Requirements

* Python 3.8+
* CPU-friendly (but GPU recommended)
* Tested with:

  * `microsoft/phi-1_5` (fast on CPU)
  * `microsoft/phi-2` (GPU recommended: 13–16 GB)

---

## Troubleshooting

### Inference is stalling?

If you’re using a low-end GPU (like NVIDIA MX250), force CPU mode:

```python
device = -1
```

### PubMed gives irrelevant results?

We fallback automatically, but you can fine-tune queries in `retrieval.py`.

---

## License

MIT License © 2025 Your Name

---

## 🙏 Acknowledgments

* [Hugging Face Transformers](https://github.com/huggingface/transformers)
* [NCBI Entrez E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
* [Microsoft Phi models](https://huggingface.co/microsoft)

---
