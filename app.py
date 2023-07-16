from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import flet as ft
from reportlab.pdfgen import canvas
from database import dbConnection
from productos import productos
from carrito import carrito
from auditoria import auditoria
from listadedeseos import listadedeseos


db = dbConnection()
carrito = carrito()
productos = productos()
auditoria = auditoria()
listadedeseos = listadedeseos()

app = Flask(__name__)

#rutas de la aplicacion
@app.route('/')
def home():
    productos = db ['productos']
    productsReceived = productos.find()
    return render_template('agregar.py', productos = productsReceived)

#agregar
@app.route('', methods=['POST'])
def addProduct():
    productos = request.form['producto']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    categoria = request.form['categoria']

    if nombre and precio and cantidad and categoria:
        product = product(nombre, precio, cantidad, categoria)
        productos.insertOne(product.toDBCollection())
        response = jsonify({
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad,
            'categoria': categoria

        })
        return redirect(url_for('home'))
    else:
        return notFound()
    
#eliminar
@app.route('/delete/<string:product_name>')
def delete(producto_name):
    productos = db ['productos']
    productos.delete_one({'nombre': producto_name})
    return redirect(url_for('home'))

#editar
@app.route('', methods=['POST'])
def edit(producto_name):
    productos = db ['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    categoria = request.form['categoria']

    if nombre and precio and cantidad and categoria:
        productos.update_one({'nombre': producto_name}, {'$set':{'nombre': nombre, 'precio': precio, 'cantidad': cantidad, 'categoria': categoria}})
        Response = jsonify({'message': 'Producto' + producto_name + 'Actualizado Correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound
    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    Response= jsonify(message)
    Response.status_code = 404
    return Response 

@app.route('/')
def index():
    
    productos = productos.find()
    return render_template('carrito.py', productos=productos)

@app.route('/agregar/<string:id>')
def agregar(id):
   
    producto = productos.find_one({'_id': id})

    if 'carrito' not in session:
        session['carrito'] = []
    session['carrito'].append(producto)

    return redirect('menu.py')

@app.route('/quitar/<string:id>')
def quitar(id):
    
    producto = productos.find_one({'_id': id})

    if 'carrito' in session:
        session['carrito'].remove(producto)

    return redirect('menu.py')
#def validar_sesion(usuario):
    
    #if usuario["tipo"] == "administrador":
        #return True
    #elif usuario["tipo"] == "usuario":
        
        #return True
    #else:
        #return False

if __name__ == '__main__':
    ft.app(target=home)