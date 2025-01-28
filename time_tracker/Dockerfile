FROM python:3.11-slim

WORKDIR /app

# Copiez le fichier requirements.txt
COPY requirements.txt .

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez tout le contenu du projet dans le conteneur
COPY . .

# Exposez le port 8000
EXPOSE 8000