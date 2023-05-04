import csv
import os
from app.db.modelos import Registro, Login


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
            f.close()
        else:
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])
            f.close()          