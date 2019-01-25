#!/bin/bash

#A docker run command to remove containers ability to run KILL command. 
#--rm is added in order to remove and clean up the filesystem after the contianer is closed
#The best would be to run --cap-drop ALL and --cap-add "Needed capabilities"

#gcc flaskehals.c -o flaskehals -static
docker build -t $1/cgiserver .
docker run --rm --name cgiserver -it  -p 8080:80 $1/cgiserver /bin/sh