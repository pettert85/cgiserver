#!/bin/bash
echo "Content-type:text/html;charset=utf-8"
echo

if [ $REQUEST_METHOD == GET ]
then

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
			Finn forfatter: <form action="http://bp:8080/cgi-bin/database.cgi" method="get">
			<input type="text" placeholder="Fornavn" name="fornavn">
			<input type="text" placeholder="Etternavn" name="etternavn">
			<input type="text" placeholder="Norge" name="nasjonalitet">
			<input type="radio" name="forfatter" value="en" checked >En forfatter<br>
			<input type="radio" name="forfatter" value="alle" >Alle forfattere<br>
			<input type="submit" value="s&oslash;k">
			</form>
		
		</td>
		<td>
			Finn bok: <form action="http://bp:8080/cgi-bin/database.cgi" method="get">
			<input type="text" placeholder="Tittel" name="tittel">
			<input type="text" placeholder="Bok ID" name="id">
			<input type="radio" name="bok" value="en" checked >En bok<br>
			<input type="radio" name="bok" value="alle" >Alle b&oslash;ker<br>
			<input type="submit" value="s&oslash;k">
			</form>
</form>
		</td>
	</tr>

	<tr>
			<td>
				<form action="http://bp:8080/cgi-bin/database.cgi" method="post">
				<input type="text" placeholder="Fornavn" name="fornavn">
				<input type="text" placeholder="Etternavn" name="etternavn">
				<input type="text" placeholder="Norge" name="nasjonalitet">
				<input type="radio" name="forfatter" value="en" checked >En forfatter<br>
				<input type="radio" name="forfatter" value="alle" >Alle forfattere<br>
				<input type="submit" name="add" value="legg til">
				<input type="submit" name="update" value="Endre">
				<input type="submit" name="delete" value="Slette">
			</form>
		</td>

		<td>
				<form action="http://bp:8080/cgi-bin/database.cgi" method="post">
				<input type="text" placeholder="Tittel" name="tittel">
				<input type="text" placeholder="Bok ID" name="id">
				<input type="radio" name="bok" value="en" checked >En bok<br>
				<input type="radio" name="bok" value="alle" >Alle b&oslash;ker<br>
				<input type="submit" name="add" value="legg til">
				<input type="submit" name="update" value="Endre">
				<input type="submit" name="delete" value="Slette">
		</td>	
	</tr>
</table>

Variabelen QUERY_STRING: $QUERY_STRING

</center>
</body></html>
EOF
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
