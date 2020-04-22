FROM ubuntu:18.04
# Dependencies Install
RUN apt-get update  && \
	apt-get -y install curl && \
	apt-get -y install curl && \
	apt-get install -qy python3 && \
	apt-get install -qy python3-pip && \
	apt-get install -qy vim && \
	apt-get -y install git

# Install Git
RUN apt-get -y install git

# Clone git repo
RUN git clone https://github.com/Darman09/Big_Data_DAHLEM_Romain_M2_IOT.git

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

RUN pip3 freeze > requirements.txt && \
	pip3 install -r requirements.txt && \
	pip3 install jupyter

# Expoe 8000 Port
EXPOSE 8000

# Run jupyter
CMD jupyter-notebook --no-browser --port=8000