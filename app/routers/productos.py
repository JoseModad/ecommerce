from fastapi import Request, APIRouter, Form
from typing import Annotated, List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.modelos import Cliente, Login, Registro

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
    print(form.username)
    print(form.password)
    return templates.TemplateResponse("logueado.html", {"request": request})

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request}) 

@router.post("/registro")
async def registro(request: Request):
    form = Registro(request)
    await form.get_data()
    print(form.username)
    print(form.pais)
    return templates.TemplateResponse("ingresar.html", {"request": request})