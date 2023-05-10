from app.db.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    nombre = Column(String(20), nullable=False)
    apellido  = Column(String(20), nullable=False)
    telefono   = Column(String(20), nullable=False)
    direccion   = Column(String(40), nullable=False)
    ciudad =  Column(String(20), nullable=False)
    provincia =  Column(String(20), nullable=False)
    pais =  Column(String(20), nullable=False)
    codigo_postal =  Column(String(20), nullable=False)
