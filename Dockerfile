#Our build

FROM httpd:alpine
EXPOSE 8080

COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./cgi-bin/ /usr/local/apache2/cgi-bin/ 
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

RUN chown -R www-data:www-data /usr/local/apache2/cgi-bin/
RUN chmod -R 755 /usr/local/apache2/cgi-bin/

#CMD apachectl -D FOREGROUND
#ENTRYPOINT ["apachectl"]

