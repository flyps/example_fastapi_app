FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

ENV POETRY_VERSION=1.4.2

RUN apt-get update              && \
    apt-get upgrade -y          && \
    apt-get autoclean -y        && \
    apt-get autoremove -y       && \
    rm -rf /var/lib/apt/lists/* && \
    pip install poetry==$POETRY_VERSION

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
ENV PORT=8000

COPY . .