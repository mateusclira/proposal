FROM ubuntu:22.10

RUN apt-get update -y

RUN apt-get install nginx -y

COPY ./site/belzinha /usr/share/nginx/html/

EXPOSE 80

WORKDIR /usr/share/nginx/html/

ENTRYPOINT ["/usr/sbin/nginx"]

CMD ["-g", "daemon off;"]