from pydantic import BaseModel, Field
import typing as t

class Subject(BaseModel):
    """
    Modelo de dominio que representa un tema o materia analítica.
    Define la estructura central del conocimiento sin depender de detalles de persistencia.
    """
    name: str = Field(..., description="Nombre descriptivo conciso del tema.")
    description: str = Field(..., description="Texto descriptivo detallado del contenido del tema.")
    main_matters: t.Any = Field(..., description="Referencias a conceptos principales o directos relacionados con el tema.")
    secondary_matters: t.Any = Field(..., description="Referencias a conceptos secundarios, tangenciales o indirectos relacionados con el tema.")