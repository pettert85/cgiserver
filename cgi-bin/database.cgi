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
			POST: <form action="http://bp:8080/cgi-bin/database.cgi" method="post">
			<input type="text" name="fornavn">
			<input type="submit">
			</form>
		</td>

		<td>
			GET Author: <form action="http://bp:8080/cgi-bin/database.cgi" method="get">
			<input type="text" placeholder="Fornavn" name="fornavn">
			<input type="text" placeholder="Etternavn" name="etternavn">
			<input type="submit" value="s&oslash;k">
		</form>
		</td>
	</tr>
</table>	
</center>
</body></html>
EOF
fi

if [ $REQUEST_METHOD == POST ]
	echo "POST"
fi
