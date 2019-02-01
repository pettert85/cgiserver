#!/bin/bash

#A docker run command to remove containers ability to run KILL command. 
#--rm is added in order to remove and clean up the filesystem after the contianer is closed
#The best would be to run --cap-drop ALL and --cap-add "Needed capabilities"

docker build -t $1/cgiserver .
docker run -v cgi-bin:/usr/local/apache2/cgi-bin/ -it --rm --name cgiserver -p 8080:80 --network=mynet $1/cgiserver /bin/bash
