# ACTA 2026-02 · Reparto de work items y decisiones de organización

| | |
|---|---|
| **Fecha del acta** | 16/11/2026 |
| **Medio** | Discord |
| **Redactor** | Esteban Ibáñez Torres |
| **Asistentes o participantes** | Esteban, Antonio, Rubén, Alberto, Gonzalo, Mario |
| **Ausentes (y si avisaron)** | Sin ausencia |
| **Issue** | #2 |
| **Estado** | Decisiones redactadas por Esteban Ibáñez con ayuda de IA (Claude). **Entran en vigor cuando los 6 miembros marquen su conformidad** al final del acta |

**Cómo se han tomado las decisiones.** Los coordinadores prepararon el borrador y las propuestas de las secciones 3 y 4 con ayuda de IA (registrado en [`docs/uso-ia.md`](../uso-ia.md)). Cada miembro las revisa y, al dar su conformidad, declara que las entiende y puede defenderlas. Cualquiera puede pedir un cambio antes de firmar.

## Orden del día

1. Reparto de los work items principales.
2. Revisores y primeras tareas de la Iteración 0.
3. Propuestas de la guía de Git.
4. Otras decisiones: marca de IA en los commits, tecnologías, nombres de módulos, hitos y reuniones.
5. Efectos en otros documentos.

---

## 1. Reparto de work items

**Método:** sorteo aleatorio con un generador de números aleatorios, realizado el 16/11/2026 por propuesta de Esteban Ibáñez. El acta fundacional decía que el reparto se haría según interés y disponibilidad, así que **cualquier miembro puede pedir un cambio antes de firmar** y se intercambia con quien esté de acuerdo.

| Work item | Responsable | GitHub |
|---|---|---|
| WI-1 Perfil y objetivos | Serrano Martínez, Alberto | `albsermar` |
| WI-2 Catálogo de ejercicios | Márquez Ortega, Rubén | `rubenmarquez0131` |
| WI-3 Rutinas | Ibáñez Torres, Esteban | `esteban-ibanez` |
| WI-4 Registro de sesiones | Ronquillo Bernáldez, Mario | `mariorb05` |
| WI-5 Progreso y estadísticas | Crespo Bravo, Antonio | *pendiente de crear* |
| WI-6 Rutinas compartidas | López Torres, Gonzalo | `gonzalolt7` |

**A tener en cuenta**

- WI-1 y WI-2 son la base de los demás: avanzan primero. Quienes dependen de ellos usan datos de ejemplo (*seeders*) mientras tanto.
- WI-4 incluye el temporizador de descanso y las llamadas sin recargar la página, que es lo más laborioso en JavaScript.
- Los coordinadores programan igual que el resto (acta fundacional, sección 2).

## 2. Revisores y primeras tareas

**Revisores de los work items.** Cada work item lo revisa **quien lleva el siguiente en la cadena de dependencias**, porque es quien lo va a usar y así conoce su interfaz. Para tareas concretas se puede cambiar el revisor avisando en la issue.

| Work item | Responsable | Revisor |
|---|---|---|
| WI-1 | Alberto Serrano | Rubén Márquez |
| WI-2 | Rubén Márquez | Esteban Ibáñez |
| WI-3 | Esteban Ibáñez | Mario Ronquillo |
| WI-4 | Mario Ronquillo | Antonio Crespo |
| WI-5 | Antonio Crespo | Gonzalo López |
| WI-6 | Gonzalo López | Alberto Serrano |

**Tareas de la Iteración 0.** Reparto también por sorteo. El revisor de cada una es el responsable de la siguiente de la lista.

| Issue | Tarea | Responsable | Revisor |
|---|---|---|---|
| #1 | Organización inicial del repositorio | Esteban Ibáñez | Alberto Serrano |
| #2 | Acta 2026-02 (esta) | Esteban Ibáñez | Alberto Serrano |
| #3 | Esqueleto de la aplicación Flask | Esteban Ibáñez | Antonio Crespo |
| #4 | Tests base y fixtures compartidas | Esteban Ibáñez | Antonio Crespo |
| #5 | Integración continua con GitHub Actions | Rubén Márquez | Alberto Serrano |
| #6 | Docker Compose para desarrollo | Alberto Serrano | Mario Ronquillo |
| #7 | Docker Compose para producción | Mario Ronquillo | Gonzalo López |
| #8 | README con la puesta en marcha | Gonzalo López | Rubén Márquez |

Las issues #5 y #6 empiezan cuando el esqueleto (#3) y los tests (#4) estén en `trunk`.

## 3. Propuestas de la guía de Git

Vienen de [`docs/guia-git.md`](../guia-git.md). El apartado 3.5.3 de los apuntes fija el modelo EGCFlow; lo siguiente son decisiones nuestras.

| Propuesta | Decisión | Por qué |
|---|---|---|
| Formato de commit `#<issue> Verbo en imperativo y descripción` | **Aprobada** | El `#N` enlaza cada commit con su issue en GitHub y da la trazabilidad que evalúa la asignatura |
| Mezclar con `git merge --no-ff` | **Aprobada** | Deja un commit de fusión por tarea y la historia se lee por tareas |
| La revisión se hace **antes** de integrar en `trunk` | **Aprobada** | Sin pull requests, es la única forma de que `trunk` reciba solo trabajo revisado |
| Una rama no pasa más de **una semana** sin integrarse | **Aprobada**, con excepción: en semanas de examen se avisa en el grupo y se acuerda otro plazo | Coincide con las iteraciones semanales y evita descubrir conflictos al final |
| Las entregas a `main` las hacen los coordinadores, tras acordarlo | **Aprobada** | Una sola persona con criterio evita etiquetas erróneas |
| Proteger `main` y `trunk` contra borrado y `push --force` (en *Rulesets*) | **Aprobada**; la configuran los coordinadores en una issue aparte | Protege el historial de un error de cualquiera, y no exige pull requests |
| Hook `pre-push` en cada ordenador | **Aprobada como recomendación**, no como obligación | Evita subir código que no pasa `ruff` ni `pytest`, pero la CI ya lo comprueba |

## 4. Otras decisiones

| Tema | Decisión | Por qué |
|---|---|---|
| Línea `Co-Authored-By` en los commits hechos con IA | **Se mantiene.** El autor sigue siendo cada miembro. Cada uso de IA relevante se anota también en `docs/uso-ia.md` | La asignatura exige documentar cómo y para qué se usa la IA. Así cada commit lo deja a la vista |
| Tecnologías | **Se confirman las del acta fundacional**: Python 3.13, Flask, SQLAlchemy, MariaDB 11.8, Flask-Login, Flask-WTF, Bootstrap 5, JavaScript sin frameworks, pytest, ruff, Docker Compose y GitHub Actions. Añadir cualquier otra librería requiere acuerdo y una nota en el diario | Es lo visto en clase y lo que el equipo puede defender |
| Librería de gráficas (WI-5) | **Chart.js 4 por CDN**, con la versión fija en la plantilla | Es sencilla y no requiere instalar nada |
| Nombres de módulos | **`autenticacion`, `perfil`, `ejercicios`, `rutinas`, `sesiones`, `progreso`, `comunidad`**, y `portada` para la página de inicio | Nombres en español y uno por funcionalidad |
| Hitos intermedios de la asignatura | **No se pueden fijar todavía**: dependen de la asignatura. Los coordinadores los preguntan al tutor en la próxima tutoría y los anotan en el diario. Mientras tanto rigen las iteraciones semanales del acta fundacional (sección 3) | No es una decisión del equipo |
| Reunión semanal | **Los lunes, al inicio de cada iteración, por Discord.** , entre las 17:00-18:00 según las disponibilidades | Una reunión por iteración permite revisar lo hecho y las ramas abiertas |

## 5. Efectos en otros documentos

Cuando el acta esté firmada, se actualizan en una rama `docs-acta-2026-02`:

- La columna «Work item principal» del acta fundacional (sección 2) y del `README.md`.
- La tabla «Decisiones propuestas» de `docs/guia-git.md`, que pasa a ser «Decisiones del equipo» (acta 2026-02).
- La lista de decisiones abiertas de `CLAUDE.md` y de `docs/prompt-inicial-claude-code.md`.
- Una entrada en `docs/uso-ia.md` por la redacción de esta acta.
- Las issues #3 a #8, con su responsable y su revisor.

## 6. Horas de la semana

Se detallan en [`horas.md`](horas.md).

## 7. Incidencias y faltas

Ninguna

## 8. Próxima reunión

Lunes 23/11/2026: seguimiento de la Iteración 0 y arranque de los work items. Hora por fijar.

---

## Conformidad

Cada miembro marca su casilla **solo cuando ha leído el acta y está de acuerdo**, y anota la fecha.

| Nombre | Conforme | Fecha |
|---|---|---|
| Ibáñez Torres, Esteban | ☑ | 17/11/2026|
| Serrano Martínez, Alberto | ☑ | 17/11/2026 |
| López Torres, Gonzalo | ☑ |17/11/2026 |
| Márquez Ortega, Rubén | ☑ |17/11/2026 |
| Ronquillo Bernáldez, Mario | ☑ |17/11/2026 |
| Crespo Bravo, Antonio | ☑ |17/11/2026 |
