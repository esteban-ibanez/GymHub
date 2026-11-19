"""Comandos de la línea de órdenes de Flask (`flask <comando>`)."""

import click
from flask.cli import with_appcontext
from sqlalchemy import text

from app.extensions import db


@click.command("init-db")
@with_appcontext  # `db.session` necesita saber qué aplicación está activa.
def init_db():
    """Comprueba la conexión con la base de datos y crea las tablas que falten."""
    # Una consulta trivial: si la base de datos no responde, aquí salta el error
    # con un mensaje claro en vez de fallar a medias al crear las tablas.
    db.session.execute(text("SELECT 1"))

    # `create_all()` solo crea las tablas de los modelos que la aplicación ha
    # importado al arrancar. Cada work item añade sus modelos en
    # app/features/<modulo>/models.py y los importa desde su blueprint;
    # mientras no haya ninguno, este comando no crea ninguna tabla y es lo esperado.
    db.create_all()
    click.echo("Base de datos lista: conexión correcta y tablas creadas.")


@click.command("seed-db")
@with_appcontext
def seed_db():
    """Carga los datos de ejemplo de cada módulo. Solo para desarrollo: nunca en producción."""
    # Se importa aquí, y no arriba, para que commands.py no dependa de los módulos al cargarse.
    from app.features.ejercicios.seeders import cargar_ejercicios_ejemplo

    creados = cargar_ejercicios_ejemplo()
    click.echo(f"Ejercicios de ejemplo creados: {creados}.")


def registrar_comandos(app):
    """Registra los comandos en la aplicación. Lo llama `crear_app()`."""
    app.cli.add_command(init_db)
    app.cli.add_command(seed_db)
