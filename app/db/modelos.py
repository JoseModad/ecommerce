from pydantic import BaseModel

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
