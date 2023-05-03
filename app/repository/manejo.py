import csv
import os
from app.db.modelos import Registro


async def verificar_usuario(username: str, password: str) -> bool:    
    with open('app/db/usuarios.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        headers = next(reader)        
        for row in reader:
            if row[0] == username and row[1] == password:
                nombre = row[3].title()                               
                return True, nombre
        return False
    
    
async def registrar_usuario(request):    
    form = Registro(request)
    await form.get_data()
    file_exists = os.path.isfile('app/db/usuarios.csv')    
    with open('app/db/usuarios.csv', 'a+', newline='',  encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists:             
            writer.writerow(['username', 'password', 'email', 'nombre', 'apellido', 'telefono', 'direccion', 'ciudad', 'provincia', 'pais', 'codigo_postal'])            
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])
            f.close()
        else:
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])
            f.close()          