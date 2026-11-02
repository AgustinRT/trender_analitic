from pydantic import BaseModel, Field
import typing as t
# Nota: Se recomienda usar el tipo 'Decimal' de la librería 'decimal' de Python estándar 
# para asegurar una precisión decimal exacta si se manejan cálculos financieros o métricas críticas. 
# Para este modelo inicial, usamos float y confiamos en Pydantic/Python type checking.

class Source(BaseModel):
    """
    Modelo de dominio que representa la fuente de información utilizada.
    Permite evaluar la fiabilidad de la fuente para diferentes tipos de contenido (hechos vs. conclusiones).
    """
    name: str = Field(..., description="Nombre descriptivo y formal de la fuente de información (ej: 'Estudio XYZ, 2024').")
    rate_fact: float = Field(..., ge=0.0, le=1.0, description="Índice de fiabilidad de la fuente para establecer un hecho o dato verificable (valor entre 0 y 1).").alias("rateFact")
    rate_conclusion: float = Field(..., ge=0.0, le=1.0, description="Índice de fiabilidad de la fuente para expresar una conclusión o análisis interpretativo (valor entre 0 y 1).").alias("rateConclusion")

# Uso de alias para seguir convenciones camelCase en el mundo real (JSON/API)
# Aunque Pydantic permite snake_case internamente, es común exponerlo como camelCase.