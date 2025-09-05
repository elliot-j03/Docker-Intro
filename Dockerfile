FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DEBUG=False
ENV PORT=8000

CMD ["uvicorn", "app.backend.app:app", "--host", "0.0.0.0", "--port", "8000"]