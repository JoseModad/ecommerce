import csv
import os
from app.db import modelos
from app.schemas import RegistroForm, ProductoForm


async def guardar_producto(request, db):
    producto = ProductoForm(request)
    await producto.get_data()
    exists_product = db.query(modelos.Producto).filter(modelos.Producto.nombre_producto == producto.nombre_producto).first()
    if exists_product:
        mensaje = "El producto ya existe"
        return mensaje
    else:
        file_location = f"app/static/img/{producto.nombre_imagen}"
        with open(file_location, "wb") as buffer:
            while True:
                data = await producto.imagen.read(1024)
                if not data:
                    break
                buffer.write(data)
                
        nuevo_producto = modelos.Producto(
            nombre_producto = producto.nombre_producto,
            marca = producto.marca,
            categoria = producto.categoria,
            stock = producto.stock,
            precio = producto.precio,
            descripcion = producto.descripcion,
            nombre_imagen = producto.nombre_imagen
        )
        db.add(nuevo_producto)
        db.commit()    
        db.refresh(nuevo_producto)
        mensaje= "Producto agregado"
        return mensaje
   

async def consultastockproducto(db):
    consulta = db.query(modelos.Producto.nombre_producto, modelos.Producto.stock).all()
    
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