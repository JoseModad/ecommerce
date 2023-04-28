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