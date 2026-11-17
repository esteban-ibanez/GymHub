"""Tests del esqueleto: fábrica, páginas de error y comando init-db."""

from sqlalchemy import inspect

from app.extensions import db


def test_crear_app_usa_la_configuracion_de_pruebas(app):
    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"


def test_pagina_inexistente_devuelve_404_con_plantilla_de_error(cliente):
    respuesta = cliente.get("/esta-pagina-no-existe")

    assert respuesta.status_code == 404
    html = respuesta.get_data(as_text=True)
    assert "Error 404" in html
    assert "La página que buscas no existe." in html


def test_init_db_comprueba_la_conexion_y_crea_las_tablas(app):
    resultado = app.test_cli_runner().invoke(args=["init-db"])

    assert resultado.exit_code == 0, resultado.output
    assert "Base de datos lista" in resultado.output
    # Aún no hay modelos, así que la base de datos sigue sin tablas: es lo esperado.
    assert inspect(db.engine).get_table_names() == []
