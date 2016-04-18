# inicio.py
# -*- coding: utf-8 -*-
import sqlite3
from bottle import route, run, template, redirect, request

HOST = '0.0.0.0'
PORT = 8081

@route('/edit/:no', method='GET')
def edit_item(no):
    """
    Edit a item
    """

    if request.GET.get('Guardar','').strip():
        descripcion = request.GET.get('descripcion','').strip()
        compras = request.GET.get('compras','').strip()
        proveedor = request.GET.get('proveedor','').strip()
        stock = request.GET.get('stock','').strip()
        familia = request.GET.get('familia','').strip()

        compratemp=float(compras)
        revendedor = compratemp*1.15
        publico = compratemp*1.27
        
        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        c.execute("SELECT Cotizacion FROM cotizacion;")
        result = c.fetchone()
        c.close()
        cotizacion=result[0]
        venta = revendedor*cotizacion
        pesos = publico*cotizacion


        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        c.execute("UPDATE articulos SET Descripcion = ?, Compra = ?, Revendedor = ?, Publico = ?, Cotizacion = ?, Venta = ?, Pesos = ?, Proveedor = ?, Stock = ?, Familia = ? WHERE ID_Articulo LIKE ?", (descripcion, compras, revendedor, publico, cotizacion, venta, pesos, proveedor, stock, familia, no))
        conn.commit()

        redirect("/items")
    else:
        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        c.execute("SELECT Descripcion, Compra, Proveedor, Stock, Familia FROM articulos WHERE ID_Articulo LIKE ?", [str(no)])
        cur_data = c.fetchone()
        return template('edit_task', old=cur_data, no=no)

@route('/')
def bucket_list():
    conn = sqlite3.connect('genesis.db')
    c = conn.cursor()
    c.execute("SELECT ID_Articulo, Descripcion, Compra, Cotizacion, Venta, Pesos, Proveedor, Stock FROM articulos;")
    result = c.fetchall()
    c.close()
    output = template('wish_table', rows=result)
    return output

@route('/<busqueda>')
def show_item(busqueda):

        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        busqueda=busqueda+"%"
        c.execute("SELECT ID_Articulo, Descripcion, Compra, Cotizacion, Venta, Pesos, Proveedor, Stock FROM articulos WHERE Descripcion LIKE ?", [busqueda])
        result = c.fetchall()
        c.close()

        if not result:
            return 'Ese articulo no existe!'
        else:
           return template('wish_table', rows=result)

@route("/new", method="GET")
def new_item():
    """
    Add a new item
    """
    if request.GET.get('Guardar','').strip():
        descripcion = request.GET.get('descripcion','').strip()
        compras = request.GET.get('compras','').strip()
        proveedor = request.GET.get('proveedor','').strip()
        stock = request.GET.get('stock','').strip()
        familia = request.GET.get('familia','').strip()

        compratemp=float(compras)
        revendedor = compratemp*1.15
        publico = compratemp*1.27
        
        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        c.execute("SELECT Cotizacion FROM cotizacion;")
        result = c.fetchone()
        c.close()
        cotizacion=result[0]
        venta = revendedor*cotizacion
        pesos = publico*cotizacion

        conn = sqlite3.connect('genesis.db')
        c = conn.cursor()
        c.execute("INSERT INTO articulos (Descripcion,Compra,Revendedor,Publico,Cotizacion,Venta,Pesos,Proveedor,Stock,Familia) VALUES (?,?,?,?,?,?,?,?,?,?)", (descripcion,compras,revendedor,publico,cotizacion,venta,pesos,proveedor,stock,familia))
        new_id = c.lastrowid
    
        conn.commit()
        c.close()
        
        redirect("/")
    else:
        return template("new_task.tpl")

@route('/del/:no', method='GET')
def del_item(no):
    """
    delete a item
    """
    conn = sqlite3.connect('genesis.db')
    c = conn.cursor()
    c.execute("DELETE FROM articulos WHERE ID_Articulo LIKE ?", [str(no)])
    conn.commit()
    c.close()

    redirect("/")

run(host=HOST, port=PORT, debug=True)