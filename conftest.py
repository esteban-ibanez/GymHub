"""Fixtures compartidas por todos los tests.

Cada test recibe una aplicación nueva con SQLite en memoria: no hace falta
MariaDB ni Docker, y un test no puede ensuciar los datos de otro.
"""

import pytest

from app import crear_app
from app.config import ConfigPruebas
from app.extensions import db


@pytest.fixture
def app():
    app = crear_app(ConfigPruebas)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def cliente(app):
    """Cliente HTTP falso para hacer peticiones a la app sin arrancar un servidor."""
    return app.test_client( )
