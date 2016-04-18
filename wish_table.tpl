<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8">
        <title>Lista precios Genesis Informatica</title>
    </head>
    <body>
      <h2>
        	%#template to generate a HTML table from a list of tuples
			<p>Lista de Precios de Genesis Informatica:</p>
			<table border="1">
			%for row in rows:
        %id, desci, compra2, cotiza2, reventa2, publi2, provee, stock2 = row
  				<tr>
  				%for col in row:
    				<td>{{col}}</td>
  				%end
          <td><a href="/edit/{{id}}"> Edit</a></td>
          <td><a href="/del/{{id}}"> Del</a></td>
  				</tr>
			%end
			</table>
      <p>Create <a href="/new">New</a> item</p>
      </h1>
    </body>
</html>

