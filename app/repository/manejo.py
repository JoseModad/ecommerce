import csv
import os
from app.schemas import Producto
from app.db import modelos
from app.schemas import RegistroForm


async def guardar_producto(request):
    producto = Producto(request)
    await producto.get_data()
    file_location = f"app/static/img/{producto.nombre_imagen}"
    with open(file_location, "wb") as buffer:
        while True:
            data = await producto.imagen.read(1024)
            if not data:
                break
            buffer.write(data)        
    file_exists = os.path.isfile('app/db/productos.csv')
    with open('app/db/productos.csv', 'a+', newline='',  encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists:             
            writer.writerow(['producto', 'marca', 'categoria', 'stock', 'precio', 'descripcion', 'nombre_imagen'])
            writer.writerow([producto.nombre_producto, producto.marca, producto.categoria, producto.stock, producto.precio, producto.descripcion, producto.nombre_imagen])
        else:
            writer.writerow([producto.nombre_producto, producto.marca, producto.categoria, producto.stock, producto.precio, producto.descripcion, producto.nombre_imagen])
    f.close()
    

async def consultastockproducto(request, id):
    consulta = []
    with open("app/db/productos.csv", "r", encoding="utf-8") as f:
            archivo = csv.reader(f, delimiter=";")
            next(archivo)
            for linea in archivo:
                producto = linea[0]
                stock = linea[3]
                consulta.append({"producto": producto, "stock": stock})
    return consulta


async def registro_usuario(request, db):
    form = RegistroForm(request)
    await form.get_data()
    exists_username = db.query(modelos.User).filter(modelos.User.username == form.username).first()
    exists_email = db.query(modelos.User).filter(modelos.User.email == form.email).first()
    if exists_username or exists_email:
        mensaje = "El usuario o email ya existen"
        retorno = ("registrarse.html", mensaje)
        return retorno

    else:         
        nuevo_usuario = modelos.User(
            username = form.username,
            password = form.password,
            email = form.email,
            nombre = form.nombre,
            apellido = form.apellido,
            telefono = form.telefono,
            direccion = form.direccion,
            ciudad = form.ciudad,
            provincia = form.provincia,
            pais = form.pais,
            codigo_postal = form.codigo_postal
        )
        db.add(nuevo_usuario)
        db.commit()    
        db.refresh(nuevo_usuario)
        retorno = ("ingresar.html", None)       
        return retorno
    

async def logueo_usuario(request, db):
    form = RegistroForm(request)
    await form.get_data()
    usuario = modelos.User(username = form.username, password = form.password)
    result = db.query(modelos.User).filter(modelos.User.username == usuario.username, modelos.User.password == usuario.password).first()    
    if result:
        nombre = result.nombre
        mensaje = ("logueado.html", nombre)
        return mensaje
    else:
        mje = "Usuario o contraseña incorrectos"     
        mensaje =("ingresar.html", mje)
        return mensaje