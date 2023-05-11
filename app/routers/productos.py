from fastapi import Request, APIRouter, File,  UploadFile, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.repository.manejo import guardar_producto, consultastockproducto, registro_usuario, logueo_usuario
from app.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")


# funcion usada para crear las tablas de la base de datos. se usara mas adelante para el panel de administracion

# @router.get("/usuarios")
# def ruta(db: Session = Depends(get_db)):
#     usuarios = db.query(modelos.User).all()
#     print(usuarios)
#     return usuarios


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
     mensaje = await logueo_usuario(request, db)
     return templates.TemplateResponse(mensaje[0], {"request": request, "mensaje": mensaje[1]})
    

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request, "mensaje": None})
    

@router.post("/registro")
async def registro(request: Request, db: Session = Depends(get_db)):
    retorno = await registro_usuario(request, db)
    return templates.TemplateResponse(retorno[0], {"request": request, "mensaje": retorno[1]})



# Funciones para el panel de administracion

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