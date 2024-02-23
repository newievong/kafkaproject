FROM python:3.10

COPY requirements.txt /app/
COPY main.py /app/
WORKDIR /app/
RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]