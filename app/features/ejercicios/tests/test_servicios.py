import pytest

from app.extensions import db
from app.features.ejercicios.models import Ejercicio
from app.features.ejercicios.services import crear_ejercicio, listar_ejercicios


def anadir_ejercicios(*ejercicios):
    db.session.add_all(ejercicios)
    db.session.commit()


def test_listar_ejercicios_sin_filtro_devuelve_todos_ordenados_por_nombre(app):
    anadir_ejercicios(
        Ejercicio(nombre="Sentadilla", grupo_muscular="piernas"),
        Ejercicio(nombre="Press de banca", grupo_muscular="pecho"),
    )

    nombres = [e.nombre for e in listar_ejercicios()]

    assert nombres == ["Press de banca", "Sentadilla"]


def test_listar_ejercicios_filtrado_solo_devuelve_ese_grupo(app):
    anadir_ejercicios(
        Ejercicio(nombre="Sentadilla", grupo_muscular="piernas"),
        Ejercicio(nombre="Press de banca", grupo_muscular="pecho"),
        Ejercicio(nombre="Aperturas", grupo_muscular="pecho"),
    )

    nombres = [e.nombre for e in listar_ejercicios("pecho")]

    assert nombres == ["Aperturas", "Press de banca"]


def test_listar_ejercicios_de_un_grupo_sin_ejercicios_devuelve_lista_vacia(app):
    anadir_ejercicios(Ejercicio(nombre="Sentadilla", grupo_muscular="piernas"))

    assert listar_ejercicios("cardio") == []


def test_crear_ejercicio_guarda_todos_los_datos(app):
    ejercicio = crear_ejercicio(
        "Press de banca", "pecho", "tríceps, hombros", "Barra", "Baja la barra al pecho."
    )

    guardado = db.session.get(Ejercicio, ejercicio.id)
    assert guardado.nombre == "Press de banca"
    assert guardado.grupo_muscular == "pecho"
    assert guardado.musculos_secundarios == "tríceps, hombros"
    assert guardado.equipamiento == "Barra"
    assert guardado.descripcion == "Baja la barra al pecho."


def test_crear_ejercicio_con_grupo_muscular_no_valido_falla(app):
    with pytest.raises(ValueError):
        crear_ejercicio("Remo", "antebrazo")

    assert listar_ejercicios() == []
