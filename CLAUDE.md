# GymHub — Instrucciones para Claude Code

Proyecto universitario de *Ingeniería del Software* (Grado en Inteligencia Artificial, Universidad de Sevilla, curso 2026/2027). Lo desarrolla un equipo de 6 estudiantes, cada uno con su propio ordenador. **Entrega final: 16/12/2026.** Responde siempre en español.

GymHub es una aplicación web para llevar el control del entrenamiento en el gimnasio: ejercicios, rutinas, registro de sesiones y progreso.

## Cómo debes trabajar

Los estudiantes saben poco de programación y **cada miembro debe poder explicar y defender todo lo que generes**. Por eso:

- **Explica qué haces y por qué**, en español sencillo. Tras cada cambio importante, resume qué se ha hecho y qué hay que saber para defenderlo.
- **Cambios pequeños y revisables.** No refactorices ni añadas funcionalidades que nadie ha pedido.
- **Código simple y legible.** Nada de abstracciones, patrones ni librerías sin una razón clara.
- **Pregunta antes de decidir** cuando algo no esté claro o haya varias opciones. No inventes requisitos.
- **No tomes decisiones que son del equipo** (dependencias nuevas, cambios de arquitectura, flujo de Git, alcance): propónlas y espera respuesta.
- Si lo que te piden contradice estas normas, el acta o los work items, **avisa** antes de hacerlo.

## Documentación (fuente de verdad)

Léela antes de trabajar en una tarea:

- `docs/diario/ACTA-2026-01-fundacional.md`: normas del equipo, sanciones, Git y uso de IA.
- `docs/work-items.md`: los 6 work items, sus historias de usuario y criterios de aceptación. **Es la única fuente de requisitos.**
- `docs/guia-git.md`: el flujo de Git (EGCFlow) paso a paso.
- `docs/prompt-inicial-claude-code.md`: versión larga de estas instrucciones.

## Al empezar cada sesión

1. Pregunta quién es el usuario (nombre, usuario de GitHub) y qué work item o issue va a trabajar.
2. Comprueba el estado de Git: rama actual, cambios sin guardar y si `trunk` está actualizada.
3. Confirma la historia de usuario y sus criterios de aceptación, y **propón un plan corto** antes de escribir código.

## Work items

| WI | Qué es | Módulo | Depende de |
|---|---|---|---|
| WI-1 | Registro, inicio de sesión, perfil y objetivos | `autenticacion`, `perfil` | — |
| WI-2 | Catálogo de ejercicios y ejercicios propios | `ejercicios` | WI-1 |
| WI-3 | Rutinas con ejercicios, series, repeticiones y descanso | `rutinas` | WI-1, WI-2 |
| WI-4 | Sesión de entreno abierta, series sin recargar y temporizador de descanso | `sesiones` | WI-1, WI-2, WI-3 |
| WI-5 | Historial, récords y evolución | `progreso` | WI-1, WI-2, WI-4 |
| WI-6 | Publicar y copiar rutinas («fork») | `comunidad` | WI-1, WI-3 |

Si dependes de un work item que aún no existe, usa **datos de ejemplo (seeders)**.

## Tecnología y arquitectura

Python 3.13, Flask (*application factory* y *blueprints*), Flask-SQLAlchemy con PyMySQL, MariaDB 11.8, Flask-Login, Flask-WTF, Jinja con Bootstrap 5 por CDN, JavaScript sin frameworks (`fetch`), pytest, ruff, Docker Compose y GitHub Actions. **No añadas otras tecnologías sin consultar.**

**El código todavía no existe**: lo crea la Iteración 0 (ver issues). Estructura prevista, una carpeta por funcionalidad:

```
app/
  __init__.py      crear_app(): fábrica; registra los blueprints
  config.py        configuración desde variables de entorno (.env)
  extensions.py    db, login_manager, csrf
  commands.py      flask init-db, seed-db, reset-db
  templates/       base.html, macros, páginas de error
  static/          CSS y JavaScript
  features/<modulo>/
    __init__.py    blueprint (importa routes al final)
    models.py      tablas
    forms.py       formularios
    services.py    lógica de negocio: ÚNICO sitio que toca la base de datos
    routes.py      vistas HTML (cortas)
    api.py         endpoints JSON
    seeders.py     datos de ejemplo
    templates/<modulo>/
    tests/         con __init__.py
conftest.py        fixtures compartidas
```

**Reglas de arquitectura**

- Flujo: `routes.py`/`api.py` → `services.py` → `models.py`. **Solo los servicios usan la base de datos.**
- **Cada usuario solo accede a sus propios datos**: los servicios comprueban la propiedad y, si no es suyo, responden como si no existiera (404). Las páginas privadas llevan `@login_required`.
- Formularios con patrón POST → redirección → GET y mensajes `flash`.
- API JSON con `jsonify` y códigos HTTP correctos. Los `fetch` que envían datos llevan la cabecera `X-CSRFToken`.
- JavaScript: `textContent` y no `innerHTML` con datos del usuario. La validación de verdad se hace **siempre en el servidor**.
- WI-4: la sesión abierta es única por usuario y se guarda en el servidor. El temporizador guarda el **instante de fin**, no cuenta segundo a segundo.
- Los datos de ejemplo nunca se cargan en producción.
- Docker con versiones fijas (`python:3.13-slim`, `mariadb:11.8`, nunca `latest`) y dos Compose: desarrollo y producción.

## Convenciones de código

**Todo en español**: código (funciones, variables, clases, rutas, tests), comentarios, commits, issues y documentación. Solo se mantiene en inglés lo que impone el lenguaje o el framework (`render_template`, `__init__`, `db.Column`, `Blueprint`, `jsonify`…).

- `snake_case` para funciones y variables, `PascalCase` para clases, **sin tildes ni `ñ` en los identificadores**.
- Ejemplos: `crear_rutina`, `listar_ejercicios`, `SerieRegistrada`, `ejercicios_bp`, `test_crear_rutina_sin_nombre`. Tablas en plural y en español.
- Coherencia: no mezclar nombres en español con nombres en inglés en el mismo módulo.
- Los textos que ve el usuario, en español y con acentos.
- Comentarios para explicar el **porqué**, no lo evidente.
- ruff: `line-length = 100`, `target-version = "py313"`, reglas E, F, I, W.

## Calidad y pruebas

- **Todo cambio lleva su prueba**; cada criterio de aceptación debería estar cubierto por un test. Si arreglas un error, **primero un test que lo demuestre**.
- Los tests usan SQLite en memoria (sin MariaDB ni Docker).
- Antes de dar algo por terminado, deben pasar:

```bash
ruff check . && ruff format --check . && pytest -q
```

- Si la CI se pone en rojo, arreglarla es lo primero.
- Si no puedes ejecutar los tests, **dilo**; no afirmes que pasan.

## Git (EGCFlow; guía completa en `docs/guia-git.md`)

- `main`: solo entregas, cada una con etiqueta (1.0, 2.0…). **Nunca se trabaja directamente en ella.**
- `trunk`: integración del equipo (rama por defecto). Siempre debe compilar y pasar las pruebas básicas.
- **Una rama por tarea** con nombre descriptivo (`rutinas`, `fix-series`, `docs-acta`, `refactor-servicios`). **Nunca el nombre de una persona**, ni nombres vagos, ni automáticos como `claude/...`. Se parte de `trunk`, se mantiene cerca de ella (`git merge origin/trunk`), se integra al terminar y **se borra**.
- **No hay pull requests dentro del equipo**: no los sugieras ni los abras. Solo se usan para proponer cambios al proyecto de otro equipo.
- Commits siempre con el usuario de quien te usa y **desde su ordenador**, nunca desde la web de GitHub.
- Mensaje de commit: `#<issue> Verbo en imperativo y descripción`, en español y sin punto final (por ejemplo, `#23 Añade el temporizador de descanso`).
- Cada issue tiene un **revisor** (un compañero) que revisa la rama con Git y lo anota en la issue.

**Tú con Git:**

- **No hagas commit, push, integración, borrado de ramas ni etiquetas sin que el usuario te lo pida.** Cuando lo pida, sigue el ciclo de la guía: rama desde `trunk` → commits pequeños → sincronizar con `trunk` → `ruff` y `pytest` → revisión → integrar en `trunk` y volver a comprobar → borrar la rama.
- Un commit = un cambio lógico pequeño.
- Si hay conflictos, ayuda a entenderlos y resolverlos en la rama del usuario, explicando cada paso. No descartes cambios de otros.
- Nunca `--force`, `git reset --hard` sobre ramas compartidas ni `--no-verify`.
- Las entregas a `main` solo si el usuario lo pide y es coordinador o se acordó en reunión.
- Este agente debe ejecutarse en el ordenador del usuario, no en una sesión remota. Si no es así, avísale.

## Issues (con `gh`)

Cada tarea es una issue de GitHub. Antes de implementar, comprueba que existe (`gh issue list`, `gh issue view <n>`); si no, ofrece crearla.

- **Título:** `[WI-4][HU-4.5] Temporizador de descanso`.
- **Cuerpo** con los apartados de la plantilla (`.github/ISSUE_TEMPLATE/tarea.yml`): Work item, Historia, Tipo, Prioridad, Revisor, Descripción y Criterios de aceptación (casillas `- [ ]` copiadas de `docs/work-items.md`).
- **Etiquetas** (las usamos para filtrar): `tipo:*`, `estado:*`, `prioridad:*` y `WI-n`. Al crear una issue: `estado:por-hacer`.
- Cuando el usuario empiece, termine o pase a revisión una tarea, ofrécete a **actualizar la etiqueta de estado** (`gh issue edit <n> --add-label ... --remove-label ...`). Se cierra con `gh issue close` cuando se cumpla la definición de hecho.
- **Definición de hecho:** cumple los criterios de la historia, tiene pruebas y la CI en verde, un compañero la ha revisado y lo ha anotado en la issue, está integrada en `trunk` con la rama borrada y no incluye secretos.
- Crear o editar issues y cerrarlas requiere la confirmación del usuario.

## Seguridad

- **Nunca** escribas contraseñas, claves ni datos personales en el código, los tests, los commits ni los comentarios. Van en `.env` (que no se sube); `.env.example` solo lleva valores falsos.
- Contraseñas de usuarios con hash, nunca en claro. CSRF activo en formularios y en `fetch`.
- No subas `.env` ni la configuración del IDE.

## Trazabilidad del uso de IA

- Al terminar cada tarea significativa, ofrece añadir una entrada a `docs/uso-ia.md` (fecha, miembro, issue, qué se te pidió, qué has hecho, qué ha aceptado o cambiado el usuario). Tú la redactas, el usuario la revisa.
- Si el usuario no entiende algo, explícalo de otra forma y no sigas hasta que lo tenga claro. No se integra código que nadie pueda defender.
- Ayuda a apuntar las horas en `docs/diario/horas.md` cuando te lo pidan.
- No copies texto ni código externo sin indicar su origen y su licencia.

## Qué no debes hacer

- Programar sin una historia de usuario o issue detrás, o salirte de su alcance.
- Añadir dependencias, cambiar la arquitectura o tocar el flujo de Git sin consultar.
- Dejar código sin pruebas o decir que algo funciona sin haberlo comprobado.
- Subir secretos, `.env`, configuración del IDE o datos personales.
- Trabajar en `main`, forzar pushes o saltarte comprobaciones.
- Inventar lo que no está definido: si falta información, **pregunta**.

## Decisiones aún abiertas (pregunta, no asumas)

- Quién lleva cada work item.
- Hitos intermedios de la asignatura.
- Librería de gráficas (propuesta: Chart.js).
- Propuestas de `docs/guia-git.md` por aprobar (formato de commit, `--no-ff`, revisión antes de integrar, vida máxima de rama): mientras tanto, síguelas.
- Si los commits asistidos por IA llevan alguna marca (por ejemplo, `Co-Authored-By`): **pregunta al usuario antes del primer commit**.
