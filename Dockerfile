#Our build

FROM httpd:alpine
EXPOSE 8080

COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

CMD apachectl -D FOREGROUND
#ENTRYPOINT ["apachectl", "start"]

