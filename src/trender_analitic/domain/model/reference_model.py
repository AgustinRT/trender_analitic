from pydantic import BaseModel, Field
import typing as t

class Reference(BaseModel):
    """
    Modelo de dominio que representa una referencia o concepto relacionado a un tema principal.
    Define la estructura de los conceptos atómicos del proyecto.
    """
    name: str = Field(..., description="Nombre descriptivo conciso de la referencia.")
    description: str = Field(..., description="Texto descriptivo detallado del contenido de esta referencia.")
    keys: t.Any = Field(..., description="Justificación que relaciona palabras clave (keywords) con el concepto o tema al que pertenece.")