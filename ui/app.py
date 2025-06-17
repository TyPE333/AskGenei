import streamlit as st
import requests

st.set_page_config(page_title="Biomedical Assistant", layout="wide")
st.title("Biomedical Research Assistant")

API_URL = "http://localhost:8000/answer"

question = st.text_input("Enter your biomedical research question:")

if st.button("Get Answer") and question:
    with st.spinner("Querying backend..."):
        try:
            response = requests.get(API_URL, params={"question": question})
            if response.status_code == 200:
                result = response.json()
                st.markdown("### Answer")
                st.success(result["answer"])
                st.markdown(f"**Mode:** {result['mode']}")
                if result["mode"] == "retrieval":
                    with st.expander("🔍 View Retrieved Abstracts"):
                        st.text(result["abstracts"])
            else:
                st.error(f"API error: {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")
