from fastapi import Request, APIRouter, Form
from typing import Annotated, List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.modelos import Cliente, Login

router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def  home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/nosotros")
def nosotros(request: Request):
    return templates.TemplateResponse("nosotros.html", {"request": request})

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
           
@router.post("/crear-cliente")
def  cliente(request: Request,  cliente: Cliente):
    return templates.TemplateResponse("crear-cliente.html", {"request": request,  "cliente": cliente})