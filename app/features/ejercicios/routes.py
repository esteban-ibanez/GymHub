"""Vistas HTML del módulo de ejercicios."""

from flask import render_template, request

from app.features.ejercicios import ejercicios_bp
from app.features.ejercicios.models import GRUPOS_MUSCULARES
from app.features.ejercicios.services import listar_ejercicios


# TODO(WI-1): añadir @login_required cuando la autenticación esté integrada en trunk.
@ejercicios_bp.route("/")
def catalogo():
    # El filtro llega en la URL (/ejercicios/?grupo=pecho) porque solo consulta datos.
    grupo = request.args.get("grupo", "")
    ejercicios = listar_ejercicios(grupo or None)
    return render_template(
        "ejercicios/catalogo.html",
        ejercicios=ejercicios,
        grupos=GRUPOS_MUSCULARES,
        grupo_elegido=grupo,
    )
