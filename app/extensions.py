"""Extensiones de Flask compartidas por toda la aplicación.

Se crean aquí sin vincularlas a ninguna aplicación. La fábrica `crear_app()` las
inicializa con `init_app(app)`. Así cualquier módulo puede hacer
`from app.extensions import db` sin importar la aplicación completa y sin
crear importaciones circulares.
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
