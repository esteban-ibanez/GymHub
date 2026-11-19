from app.extensions import db
from app.features.ejercicios.models import Ejercicio
from app.features.ejercicios.services import listar_ejercicios


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
