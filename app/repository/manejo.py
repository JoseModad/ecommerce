import csv
import os
from app.schemas import Login, Producto


async def verificar_usuario(request):
    form = Login(request)
    await form.get_data()
    with open('app/db/usuarios.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        headers = next(reader)        
        for row in reader:
            if row[0] == form.username and row[1] == form.password:
                nombre = row[3].title()                               
                return True, nombre        
        return False, None
    
    
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