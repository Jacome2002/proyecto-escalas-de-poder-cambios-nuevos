from fastapi import APIRouter, Request
from templating import templates

# 👇 Ajusta este import según cómo llames a tus funciones de lectura de BD
# Ejemplo siguiendo la estructura de clase:
from data.db.operations import read_all_personajes_db, read_all_sagas_db

# include_in_schema=True permite verlo en /docs como hizo el profe para probar,
# o cámbialo a False si quieres ocultarlo de Swagger UI.
router = APIRouter(include_in_schema=True)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Inicio - Rastreador de Ki"
        }
    )


@router.get("/personajes-web")
def personajes_page(request: Request):
    # Llamamos a la base de datos (o lista de personajes)
    personajes = read_all_personajes_db()
    
    return templates.TemplateResponse(
        request=request,
        name="personajes.html",
        context={
            "personajes": personajes,
            "title": "Guerreros Registrados"
        }
    )


@router.get("/sagas-web")
def sagas_page(request: Request):
    sagas = read_all_sagas_db()
    
    return templates.TemplateResponse(
        request=request,
        name="sagas.html",
        context={
            "sagas": sagas,
            "title": "Sagas de Dragon Ball"
        }
    )