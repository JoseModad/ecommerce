from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from app.routers import productos
from app.db.database import engine, Base


# se uso para crear las tablas de la base de datos

# def create_tables():
#     Base.metadata.create_all(bind=engine)    

# create_tables()


app = FastAPI()

app.include_router(productos.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

    

if __name__ == "__main__":
    uvicorn.run("main:app", port=8010, reload=True)