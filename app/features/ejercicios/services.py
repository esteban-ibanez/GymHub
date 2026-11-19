"""Lógica de negocio de los ejercicios: el único sitio del módulo que usa la base de datos."""

from app.extensions import db
from app.features.ejercicios.models import Ejercicio


def listar_ejercicios(grupo_muscular=None):
    """Devuelve los ejercicios ordenados por nombre.

    Si se indica un grupo muscular, solo los de ese grupo. Un grupo que no existe
    devuelve una lista vacía, y la vista muestra el mensaje de «sin resultados».
    """
    consulta = db.select(Ejercicio).order_by(Ejercicio.nombre)
    if grupo_muscular:
        consulta = consulta.where(Ejercicio.grupo_muscular == grupo_muscular)
    return db.session.scalars(consulta).all()
