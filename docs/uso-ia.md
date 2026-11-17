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

### 2026-11-17 · Gonzalo López · #4
- **Qué se pidió:** empezar la issue 4 (tests base y fixtures compartidas).
- **Qué hizo la IA:** leyó la issue y el código, y vio que los tres criterios ya se cumplían con el commit `1c2c0c9` de la issue #3 (`conftest.py` con las fixtures `app` y `cliente` sobre SQLite en memoria, y 4 tests). Como el `python3` del sistema es la 3.12 y no tiene `venv`, creó el `.venv` con `python3.13` e instaló `requirements.txt`. Pasó `ruff` y `pytest` y, con mi permiso, comentó en la issue y la pasó a `estado:en-revision`.
- **Qué se aceptó o se cambió, y por qué:** se aceptó no escribir código nuevo, porque la issue no pedía nada más y añadir código sin requisito va contra las normas del equipo. Pedí marcarla como hecha directamente; la IA avisó de que la definición de hecho exige la revisión de un compañero y se dejó en revisión. Más tarde la IA vio en el acta 2026-02 que la tarea era de Esteban (revisor: Antonio Crespo); decidí no cambiar nada porque el reparto de la Iteración 0 era orientativo.
- **Cómo lo he comprobado (tests, ejecución, revisión):** `ruff check .`, `ruff format --check .` y `pytest -q` (4 passed) en local con Python 3.13.
- **Lo he entendido y puedo defenderlo:** sí

### 2026-11-17 · Gonzalo López · #5
- **Qué se pidió:** crear la integración continua con GitHub Actions y el badge del README, y después quitar de mi `trunk` local un commit que Mario ya había quitado del remoto.
- **Qué hizo la IA:** propuso un plan y creó la rama `integracion-continua`, `.github/workflows/ci.yml` (en cada push y a mano con `workflow_dispatch`; `ubuntu-24.04` y Python 3.13; `ruff check`, `ruff format --check` y `pytest`) y el badge del README. Para quitar el commit de Mario (`d371d86`, que solo añadía una línea en blanco) usó `git branch -f trunk origin/trunk` y `git reset --soft` en la rama, que aún no estaba subida, sin perder los cambios. Hizo los commits, subió la rama y comprobó la CI en verde. Para comprobar el rojo subió un commit que rompía el formato a propósito y luego lo deshizo con `git revert`. Comentó en la issue, integró en `trunk` con `--no-ff`, comprobó la CI en `trunk` por push y a mano, borró la rama y cerró la issue tras la revisión de Esteban.
- **Qué se aceptó o se cambió, y por qué:** rechacé un comando de la IA porque no estaba siguiendo EGCFlow: había hecho commits y push sin leer la guía de Git entera, el commit roto mete ruido en el historial («un commit, un cambio lógico») y quería usar `--amend`. Tras leer la guía, se deshizo con `git revert` y sin reescribir el historial. Bastaba con comprobar en local que `ruff format --check` devuelve error. Decidí hacer la #5 aunque el acta se la asignaba a Rubén, y que el revisor fuera Esteban en lugar de Alberto. Se usó `ubuntu-24.04` en vez de `ubuntu-latest` por la regla de versiones fijas. La IA avisó de que Mario había usado `push --force` en `trunk`, cosa que la guía prohíbe.
- **Cómo lo he comprobado (tests, ejecución, revisión):** `ruff` y `pytest` en local antes de cada push y tras la integración. Ejecuciones de la CI: 44148374178 (rojo en el paso de formato), 44150167893 (push a `trunk`, verde) y 44150275147 (lanzada a mano, verde). Revisión aprobada por Esteban en la issue.
- **Lo he entendido y puedo defenderlo:** sí
