from fastapi import FastAPI
import logging
from logging.config import dictConfig
from log_config import log_config
from pydantic import BaseModel
from transformers import pipeline

class PredictionRequest(BaseModel):
  query_string: str

dictConfig(log_config)
logger = logging.getLogger("my-project-logger")

app = FastAPI()
sentiment_model = pipeline("sentiment-analysis")

@app.get("/health")
def health():
  logger.info("Health request performed")
  return 'Up and running'

@app.post("sentiment")
def my_endpoint(request: PredictionRequest):
  return sentiment_model(request) 

  