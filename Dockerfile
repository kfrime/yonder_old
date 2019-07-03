# build
# docker build -t yonder/yonder:0.8.0 .
# docker build -t yonder:latest .

# run
# docker run -t -i --name=yonder yonder
# docker run -p 8000:80 --name=yonder yonder
# 


FROM yonder/ubuntu:1.0
ENV CREATE_AT 2019-06-31

# work dir
ENV WORK_DIR /work/yonder/

# log dir
ENV LOG_DIR_BASE /work/logs/yonder
ENV LOG_DIR_NGINX /work/logs/yonder/nginx/
ENV LOG_DIR_SERVER /work/logs/yonder/server/
ENV LOG_DIR_FRONTEND /work/logs/yonder/frontend/

RUN mkdir -p $WORK_DIR
COPY . $WORK_DIR
# COPY yonder_server_go $WORK_DIR/
# COPY yonder_frontend_vue $WORK_DIR/

RUN mkdir -p $LOG_DIR_NGINX
RUN mkdir -p $LOG_DIR_SERVER
RUN mkdir -p $LOG_DIR_FRONTEND

# nginx
ADD nginx/nginx.example.conf /etc/nginx/conf.d/yonder.conf

# RUN service nginx start

EXPOSE 80

