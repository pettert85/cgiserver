#!/bin/bash
echo "Content-type:text/html;charset=utf-8"
echo

cat << EOF
<html>

<head><title>DATABASE</title>
<link rel="stylesheet" type="text/css" href="http://bp/styles.css">
</head>

<body bgcolor="556B2F">
<center>
<h1>SQLITE DATABASE!</h1>

<table id="para" cellspacing="20">
	<tr>
		<td>
			Hent en forfatter: <form method="get">
			<input type="text" placeholder="ID" name="forfatterID">
			<input type="submit" value="Hent en" name="en">
			<input type="submit" value="Hent alle" name="alle">
			</form></td></tr>

</table>
EOF

if [ $REQUEST_METHOD == GET ]
then	
	type=$(echo $QUERY_STRING | cut -d "=" -f1)
	
	mengde=$(echo $QUERY_STRING | cut -d "=" -f2 | cut -d "&" -f2)
	id=$(echo $QUERY_STRING | cut -d "=" -f2 | cut -d "&" -f1)

	if [ $type == forfatterID ]
	then
		echo "Type: $type og mengde: $mengde ID: $id" 
		if [ $mengde == en ]
		then
			echo "<pre>"
			resp=$(curl -X GET http://nodeserver:8888/forfatter/$id | xmlstarlet format --indent-tab)
			echo "$resp </pre>"
		else
			echo "<pre>"
			resp=$(curl -X GET http://nodeserver:8888/forfatter/ | xmlstarlet format --indent-tab)
			echo "$resp </pre>"
		fi
	
	else
		echo "Velg å hente data om en forfatter eller en bok. Du kan også oppdatere og slette eksisterende data! "
		
	fi

	echo $req
	
fi


if [ "$REQUEST_METHOD" = "POST" ]; then
  if [ "$CONTENT_LENGTH" -gt 0 ]; then
      read -n $CONTENT_LENGTH POST_DATA <&0
  fi
fi

#IFS='&'
#set -- $POST_DATA
tabell=$(echo $POST_DATA | cut -d'&' -f4)

if [[ $tabell == *"forfatter"* && $POST_DATA == *"add=legg+til"* ]];
then
	fnavn=$(echo $POST_DATA | cut -d'&' -f1)
	enavn=$(echo $POST_DATA | cut -d'&' -f2)
	nasjonalitet=$(echo $POST_DATA | cut -d'&' -f3)
	xml=""
	echo "Content-type: text/html"
	echo ""
	echo "<html><head><title>Legg til forfatter</title>"
	echo "<link rel="stylesheet" type="text/css" href="http://bp/styles.css">"
	echo "</head><body>"
	echo "Data received: $POST_DATA</br>"
	echo "XML: <xml Id = Forfatter add><root>"
	echo "<forfatter>"
	echo "<fnavn>$fnavn</fnavn><enavn>$enavn</enavn><nat>$nasjonalitet</nat></forfatter></root></xml></br>"
	echo "Tabell er: $tabell</br>"
	echo "Fornavn: $fnavn</br>"
        echo "Etternavn: $enavn</br>"
        echo "Nasjonalitet: $nasjonalitet</br>"
	echo "</body></html>"

elif [[ $tabell == *"forfatter"* && $POST_DATA == *"update=Endre"* ]];
then
	echo "Content-type: text/html"
	echo ""
	echo "<html><head><title>Endre en forfatter</title>"
	echo "<link rel="stylesheet" type="text/css" href="http://bp/styles.css">"
	echo"</head><body>"
	echo "Data received: $POST_DATA"
	echo "Tabell er: $tabell</br>"
	echo "Fornavn: $fnavn</br>"
        echo "Etternavn: $enavn</br>"
        echo "Nasjonalitet: $nasjonalitet</br>"
	echo "</body></html>"

elif [[ $tabell == *"forfatter"* && $POST_DATA == *"delete=Slette"* ]];
then
	echo "Content-type: text/html"
	echo ""
	echo "<html><head><title>Slette en forfatter</title>"
	echo "<link rel="stylesheet" type="text/css" href="http://bp/styles.css">"
	echo"</head><body>"
	echo "Data received: $POST_DATA"
	echo "Tabell er: $tabell</br>"
	echo "Fornavn: $fnavn</br>"
        echo "Etternavn: $enavn</br>"
        echo "Nasjonalitet: $nasjonalitet</br>"
	echo "</body></html>"


else
        echo "Content-type: text/html"
	echo ""
	echo "<html><head><title>Bok</title>"
	echo "<link rel="stylesheet" type="text/css" href="http://bp/styles.css">"
	echo "</head><body>"
	echo "Data received: $POST_DATA"
	echo "Dette skal vaere bok"
	echo "Tabell er: $tabell"
	echo "</body></html>"
fi

echo "</center></body></html>"


