from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field as PydanticField
from sqlmodel import SQLModel, Field

# ==========================================
# ENUMERACIONES
# ==========================================
class RazaEnum(str, Enum):
    SAIYAJIN = "Saiyajin"
    NAMEKIANO = "Namekiano"
    HUMANO = "Humano"
    ANDROIDE = "Androide"
    RAZA_FREEZER = "Raza de Freezer"

# ==========================================
# MODELO 1: SAGA (Tabla MySQL + Esquemas)
# ==========================================
class Saga(SQLModel, table=True):
    __tablename__ = "sagas"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, index=True)
    orden_cronologico: int = Field(ge=1)
    activo: bool = Field(default=True)

class SagaBase(BaseModel):
    nombre: str = PydanticField(..., example="Saga Saiyajin")
    orden_cronologico: int = PydanticField(..., ge=1, example=1)
    activo: bool = PydanticField(default=True, description="Borrado lógico / Histórico")

class SagaCreate(SagaBase):
    pass

class SagaUpdate(BaseModel):
    nombre: Optional[str] = None
    orden_cronologico: Optional[int] = None
    activo: Optional[bool] = None

class SagaResponse(SagaBase):
    id: int

# ==========================================
# MODELO 2: TRANSFORMACIÓN (Tabla MySQL + Esquemas)
# ==========================================
class Transformacion(SQLModel, table=True):
    __tablename__ = "transformaciones"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, index=True)
    multiplicador_ki: float = Field(ge=1.0)
    imagen_url: Optional[str] = Field(default=None, max_length=255) # Útil para multimedia
    activo: bool = Field(default=True)

class TransformacionBase(BaseModel):
    nombre: str = PydanticField(..., example="Kaio-ken x4")
    multiplicador_ki: float = PydanticField(..., ge=1.0, example=4.0)
    activo: bool = PydanticField(default=True, description="Borrado lógico / Histórico")

class TransformacionCreate(TransformacionBase):
    pass

class TransformacionUpdate(BaseModel):
    nombre: Optional[str] = None
    multiplicador_ki: Optional[float] = None
    activo: Optional[bool] = None

class TransformacionResponse(TransformacionBase):
    id: int

# ==========================================
# MODELO 3: PERSONAJE (Tabla MySQL + Esquemas)
# ==========================================
class Personaje(SQLModel, table=True):
    __tablename__ = "personajes"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, index=True)
    raza: RazaEnum = Field(max_length=50)
    ki_base: int = Field(ge=0)
    saga_id: int = Field(foreign_key="sagas.id")
    imagen_url: Optional[str] = Field(default=None, max_length=255) # Útil para multimedia
    activo: bool = Field(default=True)

class PersonajeBase(BaseModel):
    nombre: str = PydanticField(..., example="Goku")
    raza: RazaEnum = PydanticField(..., example=RazaEnum.SAIYAJIN)
    ki_base: int = PydanticField(..., ge=0, example=416)
    saga_id: int = PydanticField(..., example=1)
    activo: bool = PydanticField(default=True, description="Borrado lógico / Histórico")

class PersonajeCreate(PersonajeBase):
    pass

class PersonajeUpdate(BaseModel):
    nombre: Optional[str] = None
    raza: Optional[RazaEnum] = None
    ki_base: Optional[int] = None
    saga_id: Optional[int] = None
    activo: Optional[bool] = None

class PersonajeResponse(PersonajeBase):
    id: int

# ==========================================
# MODELO 4: COMBATE (Tabla MySQL + Esquemas)
# ==========================================
class Combate(SQLModel, table=True):
    __tablename__ = "combates"
    id: Optional[int] = Field(default=None, primary_key=True)
    personaje_atacante_id: int = Field(foreign_key="personajes.id")
    multiplicador_atacante: float = Field(default=1.0, ge=1.0)
    personaje_defensor_id: int = Field(foreign_key="personajes.id")
    multiplicador_defensor: float = Field(default=1.0, ge=1.0)
    ganador_nombre: str = Field(max_length=100)
    ki_efectivo_atacante: int
    ki_efectivo_defensor: int
    diferencia_ki: int
    rastreador_explota: bool
    mensaje_combate: str = Field(max_length=255)
    activo: bool = Field(default=True)

class CombateBase(BaseModel):
    personaje_atacante_id: int = PydanticField(..., example=1)
    multiplicador_atacante: float = PydanticField(default=1.0, ge=1.0, example=60.0)
    personaje_defensor_id: int = PydanticField(..., example=2)
    multiplicador_defensor: float = PydanticField(default=1.0, ge=1.0, example=1.0)
    activo: bool = PydanticField(default=True, description="Borrado lógico / Histórico")

class CombateCreate(CombateBase):
    pass

class CombateUpdate(BaseModel):
    personaje_atacante_id: Optional[int] = PydanticField(None, example=1)
    multiplicador_atacante: Optional[float] = PydanticField(None, ge=1.0, example=60.0)
    personaje_defensor_id: Optional[int] = PydanticField(None, example=2)
    multiplicador_defensor: Optional[float] = PydanticField(None, ge=1.0, example=1.0)
    activo: Optional[bool] = None

class CombateResponse(CombateBase):
    id: int
    ganador_nombre: str
    ki_efectivo_atacante: int
    ki_efectivo_defensor: int
    diferencia_ki: int
    rastreador_explota: bool
    mensaje_combate: str