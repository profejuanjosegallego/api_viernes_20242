from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str 
    contraseña:str
    fechaRegistro:date
    ciudad:str 
    class Config:
        orm_mode=True

class UsuarioDTORespuesta():
    id:int
    nombre:str
    telefono: str
    ciudad: str
    class Config:
        orm_mode=True

class GastoDTOPeticion():
    pass

class GastoDTORespuesta():
    pass

class CategoriaDTOPeticion():
    pass

class CategoriaDTORespuesta():
    pass

class MetodoPagoDTOPeticion():
    pass

class MetodoPagoDTORespuesta():
    pass

class FacturaDTOPeticion():
    pass

class FacturaDTORespuesta():
    pass