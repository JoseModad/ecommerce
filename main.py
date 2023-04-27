from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from app.routers import productos


app = FastAPI()

app.include_router(productos.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

    

if __name__ == "__main__":
    uvicorn.run("main:app", port=8010, reload=True)