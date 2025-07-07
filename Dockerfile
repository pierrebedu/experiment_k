FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/app:/workdir/app:/workdir


RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workdir

COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

