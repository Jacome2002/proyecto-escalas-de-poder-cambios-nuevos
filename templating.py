from pathlib import Path

from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Variable global accesible en cualquier HTML con {{ app_name }}
templates.env.globals["app_name"] = "DBZ Power Scaling"

