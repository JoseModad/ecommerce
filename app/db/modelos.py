from pydantic import BaseModel
from fastapi import Request

class Cliente(BaseModel):
	id_cliente: int
	nombre: str
	apellido: str
	email: str
	password: str
	telefono: str
	direccion: str
	ciudad: str
	provincia: str
	pais: str
	codigo_postal: str

class Login:
    def __init__(self, request: Request):
        self.request : Request = request
        self.username : str = None
        self.password : str = None
        
    async def get_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
        
class Registro:
    def __init__(self, request: Request):
        self.request : Request = request
        self.username : str = None
        self.password : str = None
        self.email : str = None
        self.nombre : str = None
        self.apellido  : str = None
        self.telefono   : str = None
        self.direccion   : str = None
        self.ciudad : str = None
        self.provincia : str = None
        self.pais : str = None
        self.codigo_postal : str = None
        
    async def get_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
        self.email = form.get("email")
        self.nombre = form.get("nombre")
        self.apellido = form.get("apellido")
        self.telefono = form.get("telefono")
        self.direccion = form.get("direccion")
        self.ciudad = form.get("ciudad")
        self.provincia = form.get("provincia")
        self.pais = form.get("pais")
        self.codigo_postal = form.get("codigo_postal")       