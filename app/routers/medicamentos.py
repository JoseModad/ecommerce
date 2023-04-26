from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(include_in_schema = False)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def  home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})