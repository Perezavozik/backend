FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

COPY entrypoints/ entrypoints/

RUN chmod +x entrypoints/entrypoint_main.sh

RUN ls -l entrypoints/entrypoint_main.sh \
 && file entrypoints/entrypoint_main.sh \
 && head -n1 entrypoints/entrypoint_main.sh | od -c

ENTRYPOINT ["/app/entrypoints/entrypoint_main.sh"]

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]