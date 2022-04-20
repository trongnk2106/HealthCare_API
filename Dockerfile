FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y tcl

RUN apt-get update
RUN apt-get install -y git
RUN apt install -y software-properties-common 
    
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN cd app && \
    pip3 install -r requirements.txt

WORKDIR /app


