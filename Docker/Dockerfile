# image ubuntu:version
FROM ubuntu:18.04

# Dependencies install
RUN apt-get -y install curl
RUN apt-get install -qy python3
RUN apt-get install -qy python3-pip
RUN apt-get install -qy vim
RUN apt-get -y install git

#SET UP des credientals
MAINTAINER DAHLEM Romain <dahlem.romain@gmail.com.fr>

# Define workspace  /workspace
WORKDIR /workspace

# Copier le contenu du répertoire courant dans le conteneur à l'adresse /workspace
ADD . /workspace

# Installer tous les packets nécessaires définis dans le fichier requirements.txt
RUN pip install -r requirements.txt

# Installer tous les packets Jupyter
RUN pip3 install jupyter

# Clone repo git
RUN git clone https://github.com/Darman09/Big_Data_DAHLEM_Romain_M2_IOT.git

# Rendre le port 8000 accessible à l'extérieur du conteneur
EXPOSE 8000

RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt

# Execute jupyter's notebook
CMD workspace --port 8000