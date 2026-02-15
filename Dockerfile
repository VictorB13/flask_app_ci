FROM python:3.11-slim
WORKDIR /app 
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirments.txt
EXPOSE 5000
CMD ["python" , "app.py"]