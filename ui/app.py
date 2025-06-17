# /ui/app.py
import sys
import os

import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import load_model, answer_question

st.set_page_config(page_title="Biomedical Assistant", layout="wide")
st.title("Biomedical Research Assistant")

pipe = load_model()
question = st.text_input("Enter your biomedical research question:")

if st.button("Get Answer") and question:
    with st.spinner("Generating answer..."):
        result = answer_question(pipe, question)
        st.markdown("### 🧠 Answer")
        st.success(result["answer"])
        st.markdown(f"**Mode:** {result['mode']}")
        if result["mode"] == "retrieval":
            with st.expander("🔍 View Retrieved Abstracts"):
                st.text(result["abstracts"])
