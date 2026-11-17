"""Fábrica de la aplicación GymHub."""

from flask import Flask, render_template

from app.commands import registrar_comandos
from app.config import Config
from app.extensions import csrf, db, login_manager


def crear_app(clase_config=Config):
    """Crea y configura la aplicación.

    Recibe la clase de configuración para poder crear una app distinta en los
    tests (`ConfigPruebas`, con SQLite) sin tocar la configuración real.
    """
    app = Flask(__name__)
    app.config.from_object(clase_config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Flask-Login exige un `user_loader` para calcular `current_user` en cada
    # plantilla. Hasta que WI-1 cree la tabla de usuarios, este provisional
    # devuelve None (nadie ha iniciado sesión). WI-1 lo sustituye por el real.
    @login_manager.user_loader
    def cargar_usuario(id_usuario):
        return None

    registrar_comandos(app)
    registrar_blueprints(app)
    registrar_errores(app)

    return app


def registrar_blueprints(app):
    """Registra los módulos de app/features/. Cada work item añade aquí el suyo."""
    from app.features.portada import portada_bp

    app.register_blueprint(portada_bp)


def registrar_errores(app):
    """Páginas de error con la plantilla común `errores/error.html`."""

    @app.errorhandler(404)
    def no_encontrado(error):
        return render_template(
            "errores/error.html", codigo=404, mensaje="La página que buscas no existe."
        ), 404

    @app.errorhandler(500)
    def error_servidor(error):
        return render_template(
            "errores/error.html", codigo=500, mensaje="Ha ocurrido un error en el servidor."
        ), 500
