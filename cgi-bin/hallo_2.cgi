#!/bin/sh

if [ $QUERY_STRING != null  ]
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
	STDIN=$(cat) >> $QUERY_STRING
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
  Variabelen QUERY_STRING: STDIN=$(cat)
 </body>
</html>  
EOF

fi


