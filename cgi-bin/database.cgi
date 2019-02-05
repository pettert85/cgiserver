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
			</form></td>
		<td>
			Hent en bok: <form method="get">
			<input type="text" placeholder="ID" name="bokID">
			<input type="submit" value="Hent en" name="en">
			<input type="submit" value="Hent alle" name="alle">
			</form></td>

</tr>
<tr>
		<td>
			 Legg til/endre/slett forfatter: <form method="post">
			<input type="text" placeholder="ID" name="forfatterID">
			<input type="text" placeholder="Fornavn" name="fornavn">
			<input type="text" placeholder="Etternavn" name="etternavn">
			<input type="text" placeholder="NOR" name="najonalitet">
			<input type="submit" value="Legg til" name="POST">
			<input type="submit" value="Endre" name="PUT">
			<input type="submit" value="Slett" name="DELETE">
			</form></td>
<td>
			Legg til/endre/slett bok: <form method="post">
			<input type="text" placeholder="BokID" name="bokID">
			<input type="text" placeholder="Tittel" name="tittel">
			<input type="text" placeholder="ForfatterID" name="forfatterID">
			<input type="submit" value="Legg til" name="POST">
			<input type="submit" value="Endre" name="PUT">
			<input type="submit" value="Slett" name="DELETE">
</td></tr>

</table>
EOF

if [ $REQUEST_METHOD == GET ]
then	
	type=$(echo $QUERY_STRING | cut -d "=" -f1)
	
	mengde=$(echo $QUERY_STRING | cut -d "=" -f2 | cut -d "&" -f2)
	id=$(echo $QUERY_STRING | cut -d "=" -f2 | cut -d "&" -f1)

	if [ $type == forfatterID ]
	then
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

	elif [ $type == bokID ]
	then
		#echo "Type: $type og mengde: $mengde ID: $id" 
		if [ $mengde == en ]
		then
			echo "<pre>"
			resp=$(curl -X GET http://nodeserver:8888/bok/$id | xmlstarlet format --indent-tab)
			echo "$resp </pre>"
		else
			echo "<pre>"
			resp=$(curl -X GET http://nodeserver:8888/bok/ | xmlstarlet format --indent-tab)
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


if [[ $POST_DATA == *"fornavn"* ]];
then
	fId=$(echo $POST_DATA | cut -d'&' -f1 | cut -d'=' -f2)
	fnavn=$(echo $POST_DATA | cut -d'&' -f2 | cut -d'=' -f2)
	enavn=$(echo $POST_DATA | cut -d'&' -f3 | cut -d'=' -f2)
	nasjonalitet=$(echo $POST_DATA | cut -d'&' -f4 | cut -d'=' -f2)

elif [[ $POST_DATA == *"tittel"* ]];
then
	bId=$(echo $POST_DATA | cut -d'&' -f1 | cut -d'=' -f2)
	tittel=$(echo $POST_DATA | cut -d'&' -f2 | cut -d'=' -f2)
	fId=$(echo $POST_DATA | cut -d'&' -f3 | cut -d'=' -f2)
fi


if [[ $POST_DATA == *"fornavn"* && $POST_DATA == *"POST"* ]];
then
	xml=$(echo "<?xml version="1.0" encoding="UTF-8"?><forfatter><forfatterID>$fId</forfatterID>\
<fornavn>$fnavn</fornavn><etternavn>$enavn</etternavn><nasjonalitet>$nasjonalitet</nasjonalitet></forfatter>")

	resp=$(curl -X POST -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/forfatter/$fId)
	echo $resp

elif [[ $POST_DATA == *"fornavn"* && $POST_DATA == *"PUT"* ]];
then
	xml=$(echo "<?xml version="1.0" encoding="UTF-8"?><forfatter><forfatterID>$fId</forfatterID>\
<fornavn>$fnavn</fornavn><etternavn>$enavn</etternavn><nasjonalitet>$nasjonalitet</nasjonalitet></forfatter>")

	resp=$(curl -X PUT -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/forfatter/$fId)
	echo $resp


elif [[ $POST_DATA == *"fornavn"* && $POST_DATA == *"DELETE"* ]];
then
	xml=$(echo "<?xml version="1.0" encoding="UTF-8"?><forfatter><forfatterID>$fId</forfatterID>\
<fornavn>$fnavn</fornavn><etternavn>$enavn</etternavn><nasjonalitet>$nasjonalitet</nasjonalitet></forfatter>")

	resp=$(curl -X DELETE -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/forfatter/$fId)
	echo $resp


elif [[ $POST_DATA == *"tittel"* && $POST_DATA == *"POST"* ]];
then
	xml=$(echo "<bok><bokID>$bId</bokID><tittel>$tittel</tittel>\
<forfatterID>$fId</forfatterID></bok>")

	resp=$(curl -X POST -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/bok/$bId)
	echo $resp


elif [[ $POST_DATA == *"tittel"* && $POST_DATA == *"PUT"* ]];
then
	xml=$(echo "<bok><bokID>$bId</bokID><tittel>$tittel</tittel>\
<forfatterID>$fId</forfatterID></bok>")

	resp=$(curl -X PUT -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/bok/$bId)
	echo $resp

elif [[ $POST_DATA == *"tittel"* && $POST_DATA == *"DELETE"* ]];
then
	xml=$(echo "<bok><bokID>$bId</bokID><tittel>$tittel</tittel>\
<forfatterID>$fId</forfatterID></bok>")

	resp=$(curl -X DELETE -H "Content-Type: text/xml" -d "$xml" http://nodeserver:8888/bok/$bId)
	echo $resp
fi


echo "</center></body></html>"


