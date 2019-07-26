# build
# docker build -f base.Dockerfile -t yonder/ubuntu:1.0 .
# docker build -t yonder:latest .

FROM ubuntu:16.04
ENV CREATE_AT 2019-06-30

RUN apt update 
RUN apt-get install -y vim
RUN apt-get install -y npm
RUN apt-get install -y nginx
