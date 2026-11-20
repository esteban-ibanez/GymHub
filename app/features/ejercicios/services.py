"""Lógica de negocio de los ejercicios: el único sitio del módulo que usa la base de datos."""

from app.extensions import db
from app.features.ejercicios.models import GRUPOS_MUSCULARES, Ejercicio


def listar_ejercicios(grupo_muscular=None):
    """Devuelve los ejercicios ordenados por nombre.

    Si se indica un grupo muscular, solo los de ese grupo. Un grupo que no existe
    devuelve una lista vacía, y la vista muestra el mensaje de «sin resultados».
    """
    consulta = db.select(Ejercicio).order_by(Ejercicio.nombre)
    if grupo_muscular:
        consulta = consulta.where(Ejercicio.grupo_muscular == grupo_muscular)
    return db.session.scalars(consulta).all()


def crear_ejercicio(
    nombre, grupo_muscular, musculos_secundarios=None, equipamiento=None, descripcion=None
):
    """Guarda un ejercicio del catálogo común y lo devuelve.

    El grupo muscular debe ser uno de GRUPOS_MUSCULARES: la base de datos acepta
    cualquier texto, así que la comprobación se hace aquí.
    """
    if grupo_muscular not in GRUPOS_MUSCULARES:
        raise ValueError(f"Grupo muscular no válido: {grupo_muscular}")
    ejercicio = Ejercicio(
        nombre=nombre,
        grupo_muscular=grupo_muscular,
        musculos_secundarios=musculos_secundarios,
        equipamiento=equipamiento,
        descripcion=descripcion,
    )
    db.session.add(ejercicio)
    db.session.commit()
    return ejercicio
