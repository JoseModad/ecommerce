from fastapi import Request, APIRouter, File,  UploadFile, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.repository.manejo import guardar_producto, consultastockproducto, registro_usuario, logueo_usuario
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import modelos
from typing import Annotated
from app.schemas import RegistroForm
from app.oauth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm






router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")


# funcion usada para crear las tablas de la base de datos. se usara mas adelante para el panel de administracion

@router.get("/administracion")
def ruta(usuario = OAuth2PasswordRequestForm, db: Session = Depends(get_db), current_user: RegistroForm =Depends(get_current_user)):
    usuarios = db.query(modelos.User).all()
    productos = db.query(modelos.Producto).all()
    print(usuarios)
    print(productos)
    return usuarios, productos   


# Funciones para el panel de Usuario

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
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
async def login(request: Request, db: Session = Depends(get_db)):    
    retorno = await logueo_usuario(request, db)
    access_token = retorno['access_token']
    mje = retorno["mensaje"]
    template = mje[0]
    mensaje = mje[1]
    return templates.TemplateResponse(template, {"request": request, "access_token": access_token,  "mensaje": mensaje})


@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request, "mensaje": ""})
    

@router.post("/registro")
async def registro(request: Request, db: Session = Depends(get_db)):
    retorno = await registro_usuario(request, db)
    template, mensaje = retorno[0], retorno[1]
    return templates.TemplateResponse(template, {"request": request, "mensaje": mensaje})



# Funciones para el panel de administracion

@router.get("/cargar-productos")
def cargar_productos(request: Request):
    return templates.TemplateResponse("cargar-productos.html", {"request": request, "mensaje": ""})


@router.post("/cargado")
async def cargado(request: Request, file: UploadFile = File(...), db: Session = Depends(get_db)):
    mensaje = await guardar_producto(request, db)
    return templates.TemplateResponse("cargar-productos.html", {"request": request, "mensaje": mensaje})


@router.post("/consultas")
async def consultas(request: Request, id: str = Form(...), db: Session = Depends(get_db)):
    if id == "botonProductos":
        consulta = await consultastockproducto(db)
        return templates.TemplateResponse("productos-stock.html", {"request": request, "consulta": consulta})                                        
    elif id == "botonVentas":
        consulta = "Consulta para ventas"
    elif id == "botonEntregas":
        consulta = "Consulta para entregas"
    elif id == "botonPagos":
        consulta = "Consulta para pagos" 