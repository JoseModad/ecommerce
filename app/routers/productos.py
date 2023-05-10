from fastapi import Request, APIRouter, File,  UploadFile, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.repository.manejo import verificar_usuario, guardar_producto, consultastockproducto
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import modelos
from app.schemas import RegistroForm


router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")

@router.get("/usuarios")
def ruta(db: Session = Depends(get_db)):
    usuarios = db.query(modelos.User).all()
    print(usuarios)
    return usuarios


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
    result, nombre = await verificar_usuario(request)
    if result:
        return templates.TemplateResponse("logueado.html", {"request": request, "nombre": nombre})
    else:        
        return templates.TemplateResponse("ingresar.html", {"request": request,  "mensaje": "Usuario o contraseña incorrectos"}) 
    

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request}) 


@router.post("/registro")
async def registro(request: Request, db: Session = Depends(get_db)):
    form = RegistroForm(request)
    await form.get_data()    
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
    return templates.TemplateResponse("ingresar.html", {"request": request})


@router.get("/cargar-productos")
def cargar_productos(request: Request):
    return templates.TemplateResponse("cargar-productos.html", {"request": request})


@router.post("/cargado")
async def cargado(request: Request, file: UploadFile = File(...)):
    await guardar_producto(request)
    return templates.TemplateResponse("cargar-productos.html", {"request": request})


@router.post("/consultas")
async def consultas(request: Request, id: str = Form(...)):
    if id == "botonProductos":
        consulta = await consultastockproducto(request, id)
        return templates.TemplateResponse("productos-stock.html", {"request": request, "consulta": consulta})                                        
    elif id == "botonVentas":
        consulta = "Consulta para ventas"
    elif id == "botonEntregas":
        consulta = "Consulta para entregas"
    elif id == "botonPagos":
        consulta = "Consulta para pagos" 
    

