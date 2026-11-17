# Registro del uso de IA

La asignatura permite usar herramientas de IA, pero hay que **documentar cómo y para qué** se han usado y **ser capaz de defender** lo que han generado. Aquí se anota cada uso significativo.

Claude Code puede redactar la entrada al terminar una tarea; quien la usa la revisa y la firma con su nombre.

## Herramientas utilizadas

| Herramienta | Para qué se usa |
|---|---|
| Claude Code (en VS Code) | Escribir y explicar código, pruebas y documentación; crear issues |

## Entradas

Copia este bloque por cada uso y rellénalo:

```
### AAAA-MM-DD · Nombre del miembro · #issue
- **Qué se pidió:**
- **Qué hizo la IA:**
- **Qué se aceptó o se cambió, y por qué:**
- **Cómo lo he comprobado (tests, ejecución, revisión):**
- **Lo he entendido y puedo defenderlo:** sí / no (si no, explícalo antes de integrar)
```

<!-- Las entradas empiezan aquí -->

### 2026-11-16 · Esteban Ibáñez · #3
- **Qué se pidió:** crear el esqueleto de la aplicación Flask siguiendo `CLAUDE.md`: fábrica `crear_app()`, configuración desde `.env`, extensiones, comando `init-db`, `base.html`, página de error y portada, en pasos pequeños explicados uno a uno y sin escribir código hasta aprobar el plan.
- **Qué hizo la IA:** leyó `CLAUDE.md`, `docs/guia-git.md` y la issue; comprobó el entorno (Python 3.13.15, Docker 29.1.3); propuso un plan de 10 pasos; creó la rama `esqueleto-flask`, el `.venv`, `requirements.txt`, `pyproject.toml`, `app/extensions.py`, `app/config.py`, el blueprint `portada`, las plantillas, `app/commands.py` (`flask init-db`), `app/__init__.py` (`crear_app()`), `.flaskenv`, `conftest.py` y 4 tests. Probó `flask run` con `curl` y `flask init-db` contra un contenedor `mariadb:11.8` temporal, que después borró. Actualizó la issue (asignación, estado, revisor).
- **Qué se aceptó o se cambió, y por qué:** se cambió el orden de los pasos para dejar `crear_app()` al final y poder probar cada pieza; `FLASK_APP` va en `.flaskenv` (se sube) y no en `.env`; una sola plantilla de error (`errores/error.html`) con código y mensaje; la portada en `app/features/portada/templates/portada/index.html`; tests de la portada en su módulo y los de fábrica, 404 e `init-db` en `app/tests/`. Las versiones de las dependencias son las de las prácticas, no las últimas. Se aceptó añadir un `user_loader` provisional que devuelve `None` porque Flask-Login lo exige y sin él toda plantilla fallaba con 500; WI-1 lo sustituye. Dos errores corregidos durante el trabajo: `init-db` necesitaba `@with_appcontext`, y el `user_loader` que faltaba.
- **Cómo lo he comprobado (tests, ejecución, revisión):** `ruff check .`, `ruff format --check .` y `pytest -q` (4 tests) en verde; `flask run` responde 200 en `/` y 404 en una URL inexistente; `flask init-db` funciona contra MariaDB 11.8 y falla con `Connection refused` si no hay base de datos.
- **Lo he entendido y puedo defenderlo:** sí
