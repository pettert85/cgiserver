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

if [ $REQUEST_METHOD == POST ]
	if [ "$CONTENT_LENGTH" -gt 0 ]; then
        	read -n $CONTENT_LENGTH QUERY_STRING <&0
    	fi
fi
