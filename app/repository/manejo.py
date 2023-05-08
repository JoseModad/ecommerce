import csv
import os
from app.db.modelos import Registro, Login, Producto


async def verificar_usuario(request):
    form = Login(request)
    await form.get_data()
    print(form)
    with open('app/db/usuarios.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        headers = next(reader)        
        for row in reader:
            if row[0] == form.username and row[1] == form.password:
                nombre = row[3].title()                               
                return True, nombre        
        return False, None
    
    
async def registrar_usuario(request):    
    form = Registro(request)
    await form.get_data()
    print(form)
    file_exists = os.path.isfile('app/db/usuarios.csv')    
    with open('app/db/usuarios.csv', 'a+', newline='',  encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists:             
            writer.writerow(['username', 'password', 'email', 'nombre', 'apellido', 'telefono', 'direccion', 'ciudad', 'provincia', 'pais', 'codigo_postal'])            
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])            
        else:
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])
    f.close() 
            

async def guardar_imagen(nombre_imagen, upload_file):
    file_location = f"app/static/imagenes/{nombre_imagen}"
    with open(file_location, "wb") as buffer:
        while True:
            data = await upload_file.read(1024)
            if not data:
                break
            buffer.write(data)
            

async def guardar_producto(request):
    file_exists = os.path.isfile('app/db/productos.csv')
    with open('app/db/productos.csv', 'a+', newline='',  encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists:             
            writer.writerow(['producto', 'marca', 'categoria', 'stock', 'precio', 'descripcion', 'nombre_imagen'])
            writer.writerow([request.nombre_producto, request.marca, request.categoria, request.stock, request.precio, request.descripcion, request.nombre_imagen])
        else:
            writer.writerow([request.nombre_producto, request.marca, request.categoria, request.stock, request.precio, request.descripcion,  request.nombre_imagen])
    f.close()
             