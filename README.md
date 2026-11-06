# proyecto-escalas-de-poder

This project is created and shared on this platform so that Dragon Ball fans, as well as newcomers looking to dive into the world of this anime, can learn about the different power scales of all the characters and their respective races. Additionally, users can create new characters and pit them against each other in battle

## 🐉 Dragon Ball Z - API de Niveles de Ki (FastAPI)

Proyecto de Desarrollo de Software utilizando FastAPI, Pydantic y Uvicorn.

API RESTful desarrollada en Python utilizando **FastAPI**, **Pydantic** y **Uvicorn**, diseñada para la gestión de niveles de poder, personajes, sagas, transformaciones y simulación de combates en el universo de Dragon Ball Z.

El proyecto implementa una arquitectura modular limpia mediante **`APIRouter`**, persistencia de datos en **archivos CSV** (sin uso de bases de datos relacionales SQL) y **borrado lógico / registro histórico**, cumpliendo con los requerimientos del Proyecto Integrador 2026-2.

---

## 📌 Características Principales

- **Arquitectura Modular**: Organización en módulos independientes (`models.py`, `database.py` y subcarpeta `routers/`).
- **4 Modelos de Datos Completos**: Operaciones CRUD independientes para `Sagas`, `Transformaciones`, `Personajes` y `Combates`.
- **Persistencia en Disco (CSV)**: Almacenamiento continuo mediante `sagas.csv`, `transformaciones.csv`, `personajes.csv` y `combates.csv`.
- **Borrado Lógico y Registro Histórico**: Las eliminaciones no destruyen datos, sino que cambian el campo `activo` a `False` para mantener la trazabilidad.
- **Búsquedas y Filtros Especializados**: Endpoints para consultar por atributos distintos al ID (nombre del personaje, raza, multiplicador de Ki, ganador de combate, etc.).
- **Regla de Negocio Compleja**: Simulación de combates calculando el Ki efectivo y evaluando la sobrecarga del rastreador (*Scouter > 21,000 unidades de Ki*).
- **Manejo de Excepciones HTTP**: Respuestas controladas con `HTTPException(status_code=404)` que evitan caídas del servidor ante IDs erróneos.
- **Documentación Interactiva**: Interfaz visual de pruebas en Swagger UI (`/docs`).

---

## 📂 Estructura del Proyecto

```text
fastapi-dbz/
├── main.py                  # Punto de entrada principal y registro de routers
├── models.py                # Esquemas Pydantic, DTOs y enumeraciones
├── database.py              # Funciones de lectura y escritura para archivos CSV
├── sagas.csv                # Archivo de datos de Sagas
├── transformaciones.csv     # Archivo de datos de Transformaciones
├── personajes.csv           # Archivo de datos de Personajes
├── combates.csv             # Archivo de datos de Combates
├── mapa_endpoints_fastapi.xlsx # Mapa oficial de endpoints del proyecto
├── requirements.txt         # Lista de dependencias del proyecto
├── .gitignore               # Archivos excluidos de Git (venv, pycache, etc.)
└── routers/
    ├── __init__.py          # Declaración de paquete de Python
    ├── sagas.py             # Router CRUD para Sagas
    ├── transformaciones.py  # Router CRUD para Transformaciones
    ├── personajes.py        # Router CRUD para Personajes
    └── combates.py          # Router CRUD y simulación para Combates
