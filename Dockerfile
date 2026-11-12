FROM python:3.11-slim
WORKDIR /app

# Bibliothèques d'abord (couche mise en cache)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Puis le code et le modèle
COPY app.py .
COPY model/ model/

ENV MODEL_URI=model
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]