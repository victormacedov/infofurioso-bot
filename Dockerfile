# Usa uma imagem base do Python (3.10 slim é leve)
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instala as dependências no container
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código-fonte do projeto para o container
COPY . /app/

# Copia o arquivo .env para o container (usado para variáveis de ambiente)
COPY .env /app/

# Define as variáveis de ambiente a partir do .env
# O arquivo .env será copiado diretamente, mas as variáveis precisam ser carregadas no ambiente
RUN pip install python-dotenv

# Comando para rodar o bot
CMD ["python", "src/main.py"]
