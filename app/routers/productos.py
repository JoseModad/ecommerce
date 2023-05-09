from fastapi import Request, APIRouter, File,  UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.repository.manejo import verificar_usuario, registrar_usuario, guardar_producto, consultastockproducto


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
    result, nombre = await verificar_usuario(request)
    if result:
        return templates.TemplateResponse("logueado.html", {"request": request, "nombre": nombre})
    else:        
        return templates.TemplateResponse("ingresar.html", {"request": request,  "mensaje": "Usuario o contraseña incorrectos"}) 
    

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request}) 


@router.post("/registro")
async def registro(request: Request):    
    await registrar_usuario(request)
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
    

