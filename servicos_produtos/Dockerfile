# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criar e definir o diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o código do projeto
COPY . .

# A porta que o container vai expor (não confunda com a porta do host)
EXPOSE 8000

# Comando para rodar a aplicação (adapte se necessário)
# Para um teste rápido, podemos rodar o server de desenvolvimento.
# Em produção, você usaria Gunicorn ou uWSGI.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]