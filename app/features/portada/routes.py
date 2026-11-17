"""Vistas HTML de la portada."""

from flask import render_template

from app.features.portada import portada_bp


@portada_bp.route("/")
def inicio():
    return render_template("portada/index.html")
