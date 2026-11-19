from app.features.ejercicios.models import GRUPOS_MUSCULARES
from app.features.ejercicios.seeders import cargar_ejercicios_ejemplo
from app.features.ejercicios.services import listar_ejercicios


def test_cargar_ejercicios_ejemplo_crea_unos_40_de_todos_los_grupos(app):
    creados = cargar_ejercicios_ejemplo()

    ejercicios = listar_ejercicios()
    assert creados == len(ejercicios)
    assert 35 <= len(ejercicios) <= 45
    assert {e.grupo_muscular for e in ejercicios} == set(GRUPOS_MUSCULARES)


def test_cargar_ejercicios_ejemplo_dos_veces_no_duplica(app):
    cargar_ejercicios_ejemplo()
    total = len(listar_ejercicios())

    assert cargar_ejercicios_ejemplo() == 0
    assert len(listar_ejercicios()) == total


def test_nombres_del_catalogo_no_se_repiten(app):
    cargar_ejercicios_ejemplo()

    nombres = [e.nombre for e in listar_ejercicios()]
    assert len(nombres) == len(set(nombres))


def test_comando_seed_db_carga_el_catalogo(app):
    resultado = app.test_cli_runner().invoke(args=["seed-db"])

    assert resultado.exit_code == 0, resultado.output
    assert "Ejercicios de ejemplo creados: " in resultado.output
    assert len(listar_ejercicios()) > 0
