from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.modelos import Login, Registro
from app.repository.manejo import verificar_usuario

import csv
import os

router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def  home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/nosotros")
def nosotros(request: Request):
    return templates.TemplateResponse("nosotros.html", {"request": request})

@router.get("/proveedores")
def proveedores(request: Request):
    return templates.TemplateResponse("proveedores.html", {"request": request})

@router.get("/ingresar")
def cliente(request: Request):
    return templates.TemplateResponse("ingresar.html", {"request": request})

@router.post("/login")
async def login(request: Request):
    form = Login(request)
    await form.get_data() 
    username = form.username
    password = form.password    
    if await verificar_usuario(username, password):
        return templates.TemplateResponse("logueado.html", {"request": request})
    else:
        return templates.TemplateResponse("ingresar.html", {"request": request})
    

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request}) 


@router.post("/registro")
async def registro(request: Request):
    form = Registro(request)
    await form.get_data()
    file_exists = os.path.isfile('app/db/usuarios.csv')
    with open('app/db/usuarios.csv', 'a', newline='',  encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists: 
            writer.writerow(['username', 'password', 'email', 'nombre', 'apellido', 'telefono', 'direccion', 'ciudad', 'provincia', 'pais', 'codigo_postal'])
            writer.writerow([form.username, form.password, form.email, form.nombre, form.apellido, form.telefono, form.direccion, form.ciudad, form.provincia, form.pais, form.codigo_postal])
            f.close()       
          
    return templates.TemplateResponse("ingresar.html", {"request": request})