#!/bin/sh

if [ $REQUEST_METHOD == GET  ]
then

echo "Content-type:text/html;charset=utf-8"
echo

cat << EOF
<!doctype html>
<html>
 <head>
  <meta charset='utf-8'>
  <title>Hallo_3</title>
 </head>
 <body>
  Variabelen QUERY_STRING: $QUERY_STRING
  Env: $REQUEST_METHOD
 </body>
</html>  
EOF

else
	if [ "$CONTENT_LENGTH" -gt 0 ]; then
        	read -n $CONTENT_LENGTH POST_DATA <&0
    	fi
 
	echo "Content-type:text/html;charset=utf-8"
echo

cat << EOF
<!doctype html>
<html>
 <head>
  <meta charset='utf-8'>
  <title>Hallo_3</title>
 </head>
 <body>
  Variabelen QUERY_STRING: $POST_DATA
 </body>
</html>  
EOF

fi


