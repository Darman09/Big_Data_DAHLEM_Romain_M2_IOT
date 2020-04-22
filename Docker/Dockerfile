FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install curl
RUN apt-get install python3
RUN apt-get install python3-pip
RUN apt-get install vim
RUN apt-get install git
RUN git clone https://github.com/Darman09/Big_Data_DAHLEM_Romain_M2_IOT.git
WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace
RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install jupyter

EXPOSE 8000
CMD workspace --port 8000