from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    nombre = Column(String(20), nullable=False)
    apellido  = Column(String(20), nullable=False)
    telefono   = Column(String(20), nullable=False)
    direccion   = Column(String(40), nullable=False)
    ciudad =  Column(String(20), nullable=False)
    provincia =  Column(String(20), nullable=False)
    pais =  Column(String(20), nullable=False)
    codigo_postal =  Column(String(20), nullable=False)
    is_active = Column(Integer, default=0)
    is_admin = Column(Integer, default=0)
    producto =  relationship("Producto", backref="usuarios", cascade="delete, merge")
    
    
class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'))
    nombre_producto = Column(String(20), nullable=False)
    marca = Column(String(200), nullable=False)
    precio = Column(Integer, nullable=False)
    descripcion  = Column(String(200), nullable=False)
    stock = Column(Integer, nullable=False)
    categoria = Column(String(20), nullable=False)
    nombre_imagen = Column(String(200), nullable=False)