# Ceci configure le conteneur avec Python 3.12 installé.
FROM python:3.12-slim

# Ceci copie tout le contenu de votre répertoire actuel vers le répertoire /app du conteneur.
COPY . /app

# Ceci définit le répertoire /app comme répertoire de travail pour toutes 
# les instructions RUN, CMD, ENTRYPOINT ou COPY qui suivent.
WORKDIR /app

# Ceci exécute pip install pour tous les packages listés dans votre fichier requirements.txt.
RUN pip install -r requirements.txt

# Ceci indique à Docker d'écouter sur le port 9696 lors de l'exécution. 
EXPOSE 8501

#ENTRYPOINT ["streamlit","run"]

# Cette commande indique à Streamlit d'exécuter votre script app.py au démarrage du conteneur.
#CMD ["main.py"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
