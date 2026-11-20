"""Tablas del módulo de ejercicios."""

from app.extensions import db

# Lista cerrada acordada por el equipo. Vive aquí para que otros módulos (rutinas,
# progreso...) la importen en lugar de repetirla:
#   from app.features.ejercicios.models import GRUPOS_MUSCULARES
# Los valores son texto que ve el usuario, por eso llevan tildes.
GRUPOS_MUSCULARES = [
    "pecho",
    "espalda",
    "hombros",
    "bíceps",
    "tríceps",
    "piernas",
    "glúteos",
    "abdomen",
    "cardio",
]


class Ejercicio(db.Model):
    """Un ejercicio del catálogo común.

    Todavía no tiene propietario: la clave ajena a usuarios se añadirá en HU-2.3,
    cuando el modelo Usuario de WI-1 esté en trunk.
    """

    __tablename__ = "ejercicios"

    id = db.Column(db.Integer, primary_key=True)
    # Nombre y grupo muscular son obligatorios (criterio de HU-2.3); el resto, opcional.
    nombre = db.Column(db.String(100), nullable=False)
    grupo_muscular = db.Column(db.String(20), nullable=False)
    # Texto libre, por ejemplo "tríceps, hombros". Puede quedar vacío.
    musculos_secundarios = db.Column(db.String(200), nullable=True)
    equipamiento = db.Column(db.String(100), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Ejercicio {self.nombre}>"
