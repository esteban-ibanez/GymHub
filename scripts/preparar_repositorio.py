"""Prepara el repositorio de GitHub: crea las etiquetas del equipo y, si se pide,
las issues de la Iteración 0.

Requisitos: tener `gh` instalado y con la sesión iniciada (`gh auth status`) y
ejecutarlo desde la carpeta del repositorio clonado.

Uso:
    python scripts/preparar_repositorio.py --simulacro   # solo muestra lo que haría
    python scripts/preparar_repositorio.py               # crea las etiquetas
    python scripts/preparar_repositorio.py --issues      # etiquetas e issues de la Iteración 0

Se puede ejecutar varias veces: las etiquetas se actualizan y las issues que ya
existen (mismo título) no se duplican.
"""

import argparse
import json
import subprocess
import sys

# (nombre, color sin #, descripción)
ETIQUETAS = [
    ("tipo:historia-usuario", "1d76db", "Funcionalidad descrita como historia de usuario"),
    ("tipo:error", "d73a4a", "Algo no funciona como debería"),
    (
        "tipo:tarea-tecnica",
        "5319e7",
        "Trabajo técnico sin historia de usuario (infraestructura, refactorización)",
    ),
    ("tipo:documentacion", "0075ca", "Documentación, actas y diario"),
    ("estado:por-hacer", "ededed", "Pendiente de empezar"),
    ("estado:en-curso", "fbca04", "Alguien está trabajando en ella"),
    ("estado:en-revision", "f9d0c4", "Terminada, a la espera de la revisión de un compañero"),
    ("estado:hecha", "0e8a16", "Cumple la definición de hecho"),
    ("prioridad:alta", "b60205", "Imprescindible para la entrega"),
    ("prioridad:media", "e99695", "Importante"),
    ("prioridad:baja", "c2e0c6", "Solo si sobra tiempo"),
    ("WI-1", "bfdadc", "Perfil y objetivos"),
    ("WI-2", "bfdadc", "Catálogo de ejercicios"),
    ("WI-3", "bfdadc", "Rutinas"),
    ("WI-4", "bfdadc", "Registro de sesiones"),
    ("WI-5", "bfdadc", "Progreso y estadísticas"),
    ("WI-6", "bfdadc", "Rutinas compartidas"),
    ("transversal", "d4c5f9", "No pertenece a un work item concreto"),
]


def issue(titulo, etiquetas, tipo, prioridad, descripcion, criterios):
    """Construye una issue con los mismos apartados que la plantilla `tarea.yml`."""
    cuerpo = (
        "### Work item\n\nTransversal (infraestructura, documentación)\n\n"
        "### Historia de usuario\n\n_No aplica_\n\n"
        f"### Tipo\n\n{tipo}\n\n"
        f"### Prioridad\n\n{prioridad}\n\n"
        "### Revisor\n\n_Por asignar_\n\n"
        f"### Descripción\n\n{descripcion}\n\n"
        "### Criterios de aceptación\n\n" + "\n".join(f"- [ ] {c}" for c in criterios) + "\n"
    )
    return {"titulo": titulo, "etiquetas": etiquetas, "cuerpo": cuerpo}


ISSUES_ITERACION_0 = [
    issue(
        "[Transversal] Organización inicial del repositorio",
        ["tipo:documentacion", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Documentación",
        "Alta",
        "Subir a `main` la organización del proyecto (CLAUDE.md, documentación, plantilla de "
        "issues, "
        "configuración de permisos de Claude Code, `.gitignore` y README), crear `trunk` y dejarla "
        "como rama por defecto.",
        [
            "`main` contiene la organización inicial y `trunk` existe.",
            "`trunk` es la rama por defecto del repositorio.",
            "Las etiquetas y la plantilla de issue están creadas.",
            "Los 6 miembros son colaboradores con permiso de escritura.",
        ],
    ),
    issue(
        "[Transversal] Acta 2026-02: reparto de work items y propuestas de Git",
        ["tipo:documentacion", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Documentación",
        "Alta",
        "Primera reunión del equipo tras la tutoría: repartir los work items, aprobar o ajustar "
        "las "
        "propuestas de `docs/guia-git.md`, confirmar el stack y fijar los hitos intermedios. "
        "Redactarla con `docs/diario/plantilla-acta-reunion.md`.",
        [
            "Cada miembro tiene asignado al menos un work item principal.",
            "Las propuestas de la guía de Git están aprobadas o modificadas.",
            "Se han fijado los hitos intermedios de la asignatura.",
            "El acta está en `docs/diario/` y firmada (conformidad) por los 6 miembros.",
        ],
    ),
    issue(
        "[Transversal] Esqueleto de la aplicación Flask",
        ["tipo:tarea-tecnica", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Tarea técnica",
        "Alta",
        "Crear la estructura base de la aplicación según `CLAUDE.md`: fábrica `crear_app()`, "
        "configuración desde `.env`, extensiones, comandos de base de datos, `base.html`, páginas "
        "de error y una portada.",
        [
            "`flask run` arranca y muestra la portada.",
            "Existen `app/__init__.py`, `config.py`, `extensions.py`, `commands.py` y "
            "`app/features/`.",
            "`flask init-db` crea las tablas sin errores.",
            "`requirements.txt` con versiones exactas y `pyproject.toml` con la configuración de "
            "ruff y pytest.",
        ],
    ),
    issue(
        "[Transversal] Tests base y fixtures compartidas",
        ["tipo:tarea-tecnica", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Tarea técnica",
        "Alta",
        "Crear `conftest.py` con las fixtures comunes (aplicación con SQLite en memoria, cliente "
        "de "
        "pruebas) y un primer test de la portada. Depende del esqueleto de la aplicación.",
        [
            "`pytest` pasa con al menos un test.",
            "Los tests no necesitan MariaDB ni Docker.",
            "Hay fixtures de aplicación y cliente reutilizables por las features.",
        ],
    ),
    issue(
        "[Transversal] Integración continua con GitHub Actions",
        ["tipo:tarea-tecnica", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Tarea técnica",
        "Alta",
        "Crear `.github/workflows/ci.yml` que ejecute `ruff check`, `ruff format --check` y "
        "`pytest` "
        "en cada push a cualquier rama, y añadir el badge de la CI al README.",
        [
            "La CI se ejecuta en cada push y también a mano (`workflow_dispatch`).",
            "Un fallo de formato o de test pone la CI en rojo.",
            "El README muestra el badge de la CI.",
        ],
    ),
    issue(
        "[Transversal] Docker Compose para desarrollo",
        ["tipo:tarea-tecnica", "estado:por-hacer", "prioridad:alta", "transversal"],
        "Tarea técnica",
        "Alta",
        "Crear el `Dockerfile` (`python:3.13-slim`) y `docker-compose.yml` con la aplicación y "
        "MariaDB 11.8, con los datos en un volumen y la configuración desde `.env`.",
        [
            "`docker compose up --build` arranca la aplicación y la base de datos.",
            "La aplicación espera a que MariaDB esté lista (healthcheck).",
            "Los datos de la base de datos persisten en un volumen.",
            "Ninguna contraseña está escrita en el repositorio.",
        ],
    ),
    issue(
        "[Transversal] Docker Compose para producción",
        ["tipo:tarea-tecnica", "estado:por-hacer", "prioridad:media", "transversal"],
        "Tarea técnica",
        "Media",
        "Crear `docker-compose.prod.yml` con gunicorn, sin datos de ejemplo, sin código montado "
        "y con "
        "cookies seguras, para el entorno de despliegue que se entrega.",
        [
            "`docker compose -f docker-compose.prod.yml up -d --build` arranca la aplicación.",
            "No se cargan datos de ejemplo.",
            "Las variables obligatorias (`SECRET_KEY`, contraseñas) fallan si no están definidas.",
        ],
    ),
    issue(
        "[Transversal] README con la puesta en marcha",
        ["tipo:documentacion", "estado:por-hacer", "prioridad:media", "transversal"],
        "Documentación",
        "Media",
        "Completar el README con cómo arrancar el proyecto (con Docker y sin él), los comandos "
        "útiles y cómo ejecutar los tests. Depende del esqueleto y de Docker.",
        [
            "Una persona nueva puede arrancar el proyecto siguiendo solo el README.",
            "Se explican `flask init-db`, `flask seed-db`, `pytest` y `ruff`.",
        ],
    ),
]


def ejecutar(orden, simulacro):
    """Ejecuta un comando de `gh` (o solo lo muestra si es un simulacro)."""
    if simulacro:
        texto = " ".join(f'"{x}"' if " " in x else x for x in orden)
        print("  $ " + texto.replace("\n", " ")[:110])
        return ""
    resultado = subprocess.run(orden, capture_output=True, text=True, encoding="utf-8")
    if resultado.returncode != 0:
        print(f"ERROR al ejecutar: {' '.join(orden[:4])} ...\n{resultado.stderr}", file=sys.stderr)
        sys.exit(1)
    return resultado.stdout


def crear_etiquetas(simulacro):
    print(f"Etiquetas ({len(ETIQUETAS)}):")
    for nombre, color, descripcion in ETIQUETAS:
        ejecutar(
            [
                "gh",
                "label",
                "create",
                nombre,
                "--color",
                color,
                "--description",
                descripcion,
                "--force",
            ],
            simulacro,
        )
        if not simulacro:
            print(f"  ok  {nombre}")


def crear_issues(simulacro):
    existentes = set()
    if not simulacro:
        salida = ejecutar(
            ["gh", "issue", "list", "--state", "all", "--limit", "200", "--json", "title"], False
        )
        existentes = {i["title"] for i in json.loads(salida or "[]")}
    print(f"Issues de la Iteración 0 ({len(ISSUES_ITERACION_0)}):")
    for datos in ISSUES_ITERACION_0:
        if datos["titulo"] in existentes:
            print(f"  ya existe: {datos['titulo']}")
            continue
        orden = ["gh", "issue", "create", "--title", datos["titulo"], "--body", datos["cuerpo"]]
        for etiqueta in datos["etiquetas"]:
            orden += ["--label", etiqueta]
        salida = ejecutar(orden, simulacro)
        if not simulacro:
            print(f"  creada: {datos['titulo']}  {salida.strip()}")


def main():
    parser = argparse.ArgumentParser(
        description="Crea las etiquetas y las issues iniciales del repositorio."
    )
    parser.add_argument(
        "--issues", action="store_true", help="crea también las issues de la Iteración 0"
    )
    parser.add_argument(
        "--simulacro", action="store_true", help="muestra lo que haría sin ejecutar nada"
    )
    argumentos = parser.parse_args()

    if not argumentos.simulacro:
        ejecutar(["gh", "auth", "status"], False)
    crear_etiquetas(argumentos.simulacro)
    if argumentos.issues:
        crear_issues(argumentos.simulacro)
    print("Hecho." if not argumentos.simulacro else "Simulacro terminado: no se ha cambiado nada.")


if __name__ == "__main__":
    main()
