# syntax=docker/dockerfile:1
FROM python:3.10.13-slim

WORKDIR /app
COPY . .

# Modify below to pull from github
#RUN #sed -i -e 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//https:\/\/mirror\.coganng\.com\/ubuntu\//' /etc/apt/sources.list && \
#    #sed -i -e 's/.*security.*//' /etc/apt/sources.list && \
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# For postgres
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \ 
                    apt-get -y install libpq-dev

RUN pip install -r requirements.txt
