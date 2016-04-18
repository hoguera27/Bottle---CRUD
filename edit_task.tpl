%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected item
<p>Editando el Item Nro. {{no}}</p>
<form action="/edit/{{no}}" method="get">
Descripcion   : <input type="text" name="descripcion" value="{{old[0]}}" size="100" maxlength="100"><br/>
Precio Compra : <input type="text" name="compras" value="{{old[1]}}" size="100" maxlength="100"><br/>
Proveedor     : <input type="text" name="proveedor" value="{{old[2]}}" size="100" maxlength="100"><br/>
Stock actual  : <input type="text" name="stock" value="{{old[3]}}" size="100" maxlength="100"><br/>
Familia       : <input type="text" name="familia" value="{{old[4]}}" size="100" maxlength="100"><br/>
<br/>
<input type="submit" name="Guardar" value="Guardar">
</form>