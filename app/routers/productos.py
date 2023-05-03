from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.modelos import Login
from app.repository.manejo import verificar_usuario, registrar_usuario


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
    result, nombre = await verificar_usuario(username, password)
    if result:
        return templates.TemplateResponse("logueado.html", {"request": request, "nombre": nombre})
    else:
        return templates.TemplateResponse("ingresar.html", {"request": request})
    

@router.get("/registrarse")
def registrarse(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request}) 


@router.post("/registro")
async def registro(request: Request):    
    await registrar_usuario(request)
    return templates.TemplateResponse("ingresar.html", {"request": request})