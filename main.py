import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from database import inicializar_csv
from routers import sagas, transformaciones, personajes, combates

from fastapi.staticfiles import StaticFiles
from templating import BASE_DIR

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")



app = FastAPI(
    title="Dragon Ball Z Ki API - CRUD CSV Completo",
    description="API RESTful con interfaz gráfica visual para gestión de Ki y combates",
    version="4.0.0"
)

# Inicializar almacenamiento CSV
inicializar_csv()

# Registrar routers CRUD
app.include_router(sagas.router)
app.include_router(transformaciones.router)
app.include_router(personajes.router)
app.include_router(combates.router)

@app.get("/", response_class=HTMLResponse, tags=["Root"])
def root():
    """Servir la interfaz web visual (HTML/CSS) desde index.html."""
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as file:
            return file.read()
    return "<h1>API activa. Crea el archivo index.html en la raíz para ver la interfaz.</h1>"