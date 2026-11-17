# GymHub

[![CI](https://github.com/esteban-ibanez/GymHub/actions/workflows/ci.yml/badge.svg)](https://github.com/esteban-ibanez/GymHub/actions/workflows/ci.yml)

Aplicación web para llevar el control de lo que hacemos en el gimnasio: ejercicios, rutinas, sesiones de entreno con temporizador de descanso y progreso. Igual que GitHub guarda el registro de un proyecto, GymHub guarda el registro de tu progreso: cada serie que apuntas es como un *commit* y cada récord, una nueva versión de ti.

Proyecto de la asignatura **Ingeniería del Software** (Grado en Inteligencia Artificial, Universidad de Sevilla, curso 2026/2027). Entrega final: **16/12/2026**.

> **Estado:** en la Iteración 0 (organización del repositorio y esqueleto de la aplicación). La puesta en marcha se documentará aquí cuando exista el código.

## Equipo

| Nombre | GitHub |
|---|---|
| Esteban Ibáñez Torres (coordinador) | `esteban-ibanez` |
| Alberto Serrano Martínez (coordinador) | `albsermar` |
| Gonzalo López Torres | `gonzalolt7` |
| Rubén Márquez Ortega | `rubenmarquez0131` |
| Mario Ronquillo Bernáldez | `mariorb05` |
| Antonio Crespo Bravo | pendiente |

## Tecnología

Python 3.13, Flask, SQLAlchemy, MariaDB, Flask-Login, Flask-WTF, Bootstrap 5, JavaScript, pytest, ruff, Docker Compose y GitHub Actions.

## Documentación

| Documento | Contenido |
|---|---|
| [`docs/diario/ACTA-2026-01-fundacional.md`](docs/diario/ACTA-2026-01-fundacional.md) | Normas del equipo, planificación, sanciones y uso de IA |
| [`docs/work-items.md`](docs/work-items.md) | Work items, historias de usuario y criterios de aceptación |
| [`docs/guia-git.md`](docs/guia-git.md) | Flujo de Git (EGCFlow) paso a paso |
| [`docs/prompt-inicial-claude-code.md`](docs/prompt-inicial-claude-code.md) | Instrucciones largas para el agente de IA |
| [`docs/diario/`](docs/diario/) | Diario del equipo: actas, horas y plantilla de reunión |
| [`docs/uso-ia.md`](docs/uso-ia.md) | Registro del uso de herramientas de IA |

El fichero [`CLAUDE.md`](CLAUDE.md) contiene las instrucciones que lee Claude Code al abrir el repositorio.

## Cómo trabajamos

- Flujo **EGCFlow**: `main` para entregas con etiqueta, `trunk` para integrar y una rama por tarea. Sin pull requests dentro del equipo.
- Toda tarea es una **issue** de GitHub con la plantilla del equipo.
- Antes de integrar: `ruff check . && ruff format --check . && pytest -q`.
