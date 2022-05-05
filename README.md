# MLOpsAPI
FastAPI deployment for the sentiment analysis based on HuggingFace Standard Pipeline()

## Create Docker Image
```shell
# create image
docker build -t sentiment-api .
# run image
docker run -dp 8000:8000 sentiment-api:latest
```
