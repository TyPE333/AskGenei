#!/bin/bash

# Activate virtual environment if needed
# source venv/bin/activate

echo "🧪 Starting FastAPI backend..."
uvicorn AskGenei.api.main:app --host 0.0.0.0 --port 8000 --reload &

# Wait for API to boot
sleep 3

echo "🎨 Starting Streamlit UI..."
streamlit run AskGenei/ui/app.py
