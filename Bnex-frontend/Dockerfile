FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --user --no-cache-dir -r requirements.txt

# Etapa Final
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências necessárias no runtime
RUN apt-get update && apt-get install -y \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copiar as dependências da fase anterior
COPY --from=builder /root/.local /root/.local

# Adicionar /root/.local/bin ao PATH para acessar os pacotes Python instalados
ENV PATH=/root/.local/bin:$PATH

COPY . .

EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
