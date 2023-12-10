FROM python:3.12.1

ARG PYTHON_VERSION=3.12.1

WORKDIR /workspace

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
