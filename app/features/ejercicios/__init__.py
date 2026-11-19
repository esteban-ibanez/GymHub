"""Módulo de ejercicios (WI-2): catálogo común de ejercicios y, más adelante, los propios."""

from flask import Blueprint

# Todas las rutas del módulo cuelgan de /ejercicios.
ejercicios_bp = Blueprint(
    "ejercicios", __name__, url_prefix="/ejercicios", template_folder="templates"
)

# Se importan al final para que `routes` pueda usar `ejercicios_bp` sin importación circular.
# `models` se importa para que `db.create_all()` (init-db) conozca la tabla `ejercicios`.
from app.features.ejercicios import models, routes  # noqa: E402, F401
