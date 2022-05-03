FROM python:3.8.1-slim 
ENV PYTHONNONBUFFERED 1
EXPOSE 8000
WORKDIR /app
COPY . /app
RUN pip --no-cache install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.main:app"]
