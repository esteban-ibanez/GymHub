"""Configuración de la aplicación a partir de variables de entorno.

Los valores reales (contraseñas, clave secreta) viven en el fichero `.env`, que
no se sube al repositorio. `.env.example` documenta qué variables hacen falta.
"""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

# Carga el `.env` de la raíz del proyecto en las variables de entorno. Si ya
# existe una variable en el entorno, `.env` no la sobrescribe.
load_dotenv()


def construir_url_mariadb():
    """Construye la URL de conexión a MariaDB a partir de las variables MARIADB_*."""
    usuario = os.environ.get("MARIADB_USER", "")
    # La contraseña se escapa por si contiene caracteres con significado en una URL (@, /, :...).
    contrasena = quote_plus(os.environ.get("MARIADB_PASSWORD", ""))
    host = os.environ.get("MARIADB_HOSTNAME", "localhost")
    puerto = os.environ.get("MARIADB_PORT", "3306")
    base_datos = os.environ.get("MARIADB_DATABASE", "")
    return f"mysql+pymysql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}"


class Config:
    """Configuración normal: desarrollo y producción, con MariaDB."""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = construir_url_mariadb()
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigPruebas(Config):
    """Configuración para los tests: SQLite en memoria, sin MariaDB ni Docker."""

    TESTING = True
    SECRET_KEY = "clave-solo-para-tests"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # En los tests no se envía el token CSRF en cada formulario; en la aplicación real sigue activo.
    WTF_CSRF_ENABLED = False
