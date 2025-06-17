# Makefile for Biomedical Assistant

VENV_ACTIVATE = source venv/bin/activate
FASTAPI_PORT ?= 8000
STREAMLIT_PORT ?= 8501

install:
	pip install -r requirements.txt

run-api:
	uvicorn AskGenei.api.main:app --host 0.0.0.0 --port $(FASTAPI_PORT) --reload

run-ui:
	streamlit run AskGenei/ui/app.py --server.port $(STREAMLIT_PORT)

run: 
	@echo "🔁 Starting FastAPI on port $(FASTAPI_PORT)..."
	@$(MAKE) run-api & \
	sleep 3 && \
	$(MAKE) run-ui

format:
	black AskGenei

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
