FROM ubuntu:18.04
# Dependencies Install
RUN apt-get update  && \
	apt-get -y install curl && \
	apt-get install -qy python3 && \
	apt-get install -qy python3-pip && \
	apt-get install -qy vim && \
	apt-get -y install git

# Install Git
RUN apt-get -y install git

WORKDIR /workspace

# Clone git repo
RUN git clone https://github.com/Darman09/Big_Data_DAHLEM_Romain_M2_IOT.git

WORKDIR /Big_Data_DAHLEM_Romain_M2_IOT/Docker

RUN pip3 install -r /Big_Data_DAHLEM_Romain_M2_IOT/Docker/requirements.txt

WORKDIR /Big_Data_DAHLEM_Romain_M2_IOT/Flask

# Expoe 8000 Port
EXPOSE 8000

# Go to workspace
# CMD workspace --port 8000
CMD ["python",".\Hello_World.py"]