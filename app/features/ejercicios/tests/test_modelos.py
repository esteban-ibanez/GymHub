import pytest
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.features.ejercicios.models import GRUPOS_MUSCULARES, Ejercicio


def test_grupos_musculares_son_los_acordados():
    assert GRUPOS_MUSCULARES == [
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


def test_crear_ejercicio_sin_musculos_secundarios(app):
    ejercicio = Ejercicio(nombre="Plancha", grupo_muscular="abdomen")
    db.session.add(ejercicio)
    db.session.commit()

    guardado = db.session.get(Ejercicio, ejercicio.id)
    assert guardado.nombre == "Plancha"
    assert guardado.musculos_secundarios is None


def test_crear_ejercicio_sin_nombre_falla(app):
    db.session.add(Ejercicio(grupo_muscular="pecho"))

    with pytest.raises(IntegrityError):
        db.session.commit()
