#Our build

FROM httpd:alpine
EXPOSE 8080
EXPOSE 8888

COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
RUN apk update && apk add curl && apk add xmlstarlet
CMD apachectl -D FOREGROUND
#ENTRYPOINT ["apachectl", "start"]

