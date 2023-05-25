FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN python3 -m pip install --upgrade pip
RUN pip install gunicorn==20.1.0
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
