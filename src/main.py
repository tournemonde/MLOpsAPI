from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
sentiment_model = pipeline("sentiment-analysis")


@app.get("/")
def health():
  return 'Up and running'


@app.post("/sentiment")
def my_endpoint(request: str): # PredictionRequest):
  return sentiment_model(request) 

# uvicorn main:app --port 8000   
  