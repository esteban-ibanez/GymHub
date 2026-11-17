"""Módulo de la portada: la página de inicio de GymHub."""

from flask import Blueprint

# `template_folder` hace que las plantillas de este módulo vivan junto a su código,
# en app/features/portada/templates/.
portada_bp = Blueprint("portada", __name__, template_folder="templates")

# Se importa al final para que `routes` pueda usar `portada_bp` sin importación circular.
from app.features.portada import routes  # noqa: E402, F401
