from fastapi import FastAPI
import logging
from logging.config import dictConfig
from log_config import log_config

dictConfig(log_config)
logger = logging.getLogger("my-project-logger")

app = FastAPI()

@app.get("/health")
def health():
  logger.info("Health request performed")
  return 'Up and running'

