# GymHub — Acta fundacional del equipo

**ACTA 2026-01** · Primera entrada del diario del equipo

| | |
|---|---|
| **Versión** | 2.0 (revisión tras la primera tutoría) |
| **Fecha del acta original** | 09/10/2026 |
| **Fecha de esta revisión** | 16/11/2026 |
| **Estado** | Borrador de revisión, pendiente de aprobación y firma de los 6 miembros |
| **Asignatura** | Ingeniería del Software · Grado en Inteligencia Artificial · Curso 2026/2027 |
| **Tipo de proyecto** | Single |
| **Entrega final** | 16/12/2026 |

### Historial de revisiones

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 09/10/2026 | Acta fundacional original. |
| 2.0 | 16/11/2026 | Work items reformulados como historias de usuario («Como… quiero… para…») por indicación del tutor. WI-4 rediseñado como sesión de entreno abierta con temporizador de descanso. Se añaden objetivos y alcance, planificación, definición de hecho, convenciones, entregables, riesgos y firmas. Flujo de Git ampliado según EGCFlow (apuntes, 3.5.3). |

---

## 1. El proyecto

**GymHub** es una aplicación web para llevar el control de lo que hacemos en el gimnasio: los ejercicios, las rutinas y cómo progresamos. Igual que GitHub guarda el registro de un proyecto, GymHub guarda el registro del progreso en el gimnasio: cada serie que se apunta es como un *commit* y cada récord, una nueva versión de ti.

**Para quién:** personas que entrenan en un gimnasio y quieren dejar de apuntar sus marcas en papel o en notas del móvil.

**Qué queremos conseguir**

1. Que apuntar una serie durante el entreno sea rápido: sin recargar la página y con descanso cronometrado.
2. Que el usuario vea que mejora: historial, récords y evolución por ejercicio.
3. Que las rutinas se puedan compartir y copiar, como quien hace un *fork*.
4. Aplicar en un proyecto real lo visto en la asignatura: control de versiones, integración continua, contenedores, pruebas y gestión de tareas.

**Dentro del alcance:** los seis work items de la sección 4.
**Fuera del alcance** (si sobra tiempo, se hablará con el tutor): aplicación móvil nativa, pagos, chat entre usuarios, integración con dispositivos o relojes, rutinas generadas con IA.

El proyecto se desarrolla **desde cero**. La arquitectura se inspira en Listo, el proyecto de las prácticas. Todo código o texto que se reutilice de otra fuente se cita con su licencia (sección 11).

---

## 2. Equipo

| Apellidos, nombre | Usuario de GitHub | Rol | Work item principal |
|---|---|---|---|
| Ibáñez Torres, Esteban | `esteban-ibanez` | Coordinador y desarrollador | Por asignar |
| Serrano Martínez, Alberto | `albsermar` | Coordinador y desarrollador | Por asignar |
| López Torres, Gonzalo | `gonzalolt7` | Desarrollador | Por asignar |
| Márquez Ortega, Rubén | `rubenmarquez0131` | Desarrollador | Por asignar |
| Ronquillo Bernáldez, Mario | `mariorb05` | Desarrollador | Por asignar |
| Crespo Bravo, Antonio | **Pendiente: crear cuenta** | Desarrollador | Por asignar |

**Coordinación.** Esteban Ibáñez y Alberto Serrano llevan el calendario, convocan las reuniones, siguen los plazos y hablan con el tutor y con otros equipos. Coordinar no significa mandar: su papel es que el equipo funcione.

**Desarrollo.** Todos programamos, coordinadores incluidos. Cada miembro es responsable de **al menos un work item principal**, que puede dividirse en tareas más pequeñas. Se puede cargar más desarrollo en unas personas que en otras, pero a nadie se le quita de esta labor. El reparto se acuerda entre todos según interés y disponibilidad y se anota en el diario.

**Bajas.** Si un miembro abandona, se comunica al coordinador de la asignatura y se anota en el diario con la firma de los restantes miembros y, si es posible, de quien se va.

---

## 3. Planificación

**Dedicación acordada:** 45 horas por persona, 270 horas en total.

**Indicadores mínimos del enunciado** (orientativos), para 45 h por persona:

| | Por persona | Equipo (6) |
|---|---|---|
| Líneas de código | 450 | 2.700 |
| Commits | 9 | 54 |
| Incidencias (issues) | 5 | 27 |

**Hitos externos:** entrega final el **16/12/2026**. *Los hitos intermedios de la asignatura están pendientes de confirmar.*

**Iteraciones internas** (semanales, propuesta inicial):

| Iteración | Fechas | Objetivo |
|---|---|---|
| 0 | 16/11 – 22/11 | Repositorio, esqueleto de la aplicación, CI, Docker y arranque de WI-1 y WI-2 (las demás se apoyan en ellos). |
| 1 | 23/11 – 29/11 | WI-1 y WI-2 terminados. WI-3 y WI-4 en marcha. |
| 2 | 30/11 – 06/12 | WI-3 y WI-4 terminados. WI-5 y WI-6 en marcha. |
| 3 | 07/12 – 13/12 | WI-5 y WI-6 terminados, integración, pruebas y despliegue. |
| Cierre | 14/12 – 16/12 | Documento del proyecto, vídeo, empaquetado y entrega. |

---

## 4. Work items

Cada work item se formula como historia de usuario: **Como** (rol) **quiero** (funcionalidad) **para** (beneficio). El desglose en historias, los criterios de aceptación y las dependencias están en [`docs/work-items.md`](../work-items.md).

| WI | Nombre | Historia de usuario principal | Depende de |
|---|---|---|---|
| WI-1 | Perfil y objetivos | **Como** persona que entrena, **quiero** crear mi cuenta y fijar mis objetivos de entrenamiento, **para** tener mis datos privados y saber si los cumplo. | — |
| WI-2 | Catálogo de ejercicios | **Como** usuario, **quiero** consultar los ejercicios por grupo muscular y crear los míos, **para** encontrar rápido qué entrenar y registrar lo que no está en el catálogo. | WI-1 |
| WI-3 | Rutinas | **Como** usuario, **quiero** montar rutinas con ejercicios, series y repeticiones, **para** tener un plan de entreno definido. | WI-1, WI-2 |
| WI-4 | Registro de sesiones | **Como** usuario, **quiero** abrir una sesión de entreno y apuntar en ella cada serie, con un temporizador que me avise cuando haya descansado, **para** registrar mi entreno en directo sin perder el ritmo ni recargar la página. | WI-1, WI-2, WI-3 |
| WI-5 | Progreso y estadísticas | **Como** usuario, **quiero** ver mi historial, mis récords y la evolución de cada ejercicio, **para** comprobar que estoy mejorando. | WI-1, WI-2, WI-4 |
| WI-6 | Rutinas compartidas | **Como** usuario, **quiero** publicar mis rutinas y copiar las de otros, **para** aprovechar planes ya probados sin empezar de cero. | WI-1, WI-3 |

Los work items están **encadenados a propósito**: WI-1 y WI-2 son la base y, en cuanto están, WI-3 y WI-4 avanzan en paralelo y alimentan a WI-5 y WI-6. Cada work item desarrolla al menos una historia de usuario que se puede probar en el sistema.

Los cambios se hacen con cuidado: pocos y bien hechos mejor que muchos sin valor.

---

## 5. Tecnología y convenciones

**Tecnologías** (las vistas en clase): Python 3.13 y Flask, SQLAlchemy, MariaDB, Flask-Login y Flask-WTF, HTML con Jinja y Bootstrap 5, JavaScript sin frameworks (`fetch` para la API JSON), pytest y ruff, Docker Compose y GitHub Actions. Cualquier librería nueva se acuerda en reunión y se anota en el diario.

**Convenciones**

- **Idioma:** todo en español: código (funciones, variables, clases, rutas y tests), comentarios, commits, issues y documentación. Se mantiene en inglés solo lo que impone el lenguaje o el framework (`render_template`, `__init__`…). Los identificadores no llevan tildes ni `ñ`.
- **Estructura:** una carpeta por funcionalidad. Las rutas son cortas y solo los servicios hablan con la base de datos.
- **Calidad:** el código pasa `ruff check`, `ruff format --check` y `pytest` antes de cada integración. La CI hace lo mismo en cada push.
- **Secretos:** las contraseñas, el `.env` y la configuración del IDE no se suben al repositorio.

---

## 6. Reuniones y comunicación

Nos reunimos **una vez a la semana**, en persona o por videollamada. Quien no pueda ir avisa con al menos un día de antelación y luego se pone al día con lo decidido. De cada reunión se deja constancia en el diario: fecha, asistentes, decisiones, tareas y horas.

| Necesidad | Herramienta |
|---|---|
| Comunicación del día a día | WhatsApp y Discord |
| Reuniones | En persona o Discord |
| Tareas | Issues de GitHub |
| Código | GitHub |
| Diario del equipo | GitHub |

Nos comprometemos a **responder a los mensajes del proyecto en menos de 48 horas**. Cada decisión importante se apunta en el diario como un acta nueva (ACTA 2026-02, 2026-03…).

---

## 7. Gestión de tareas y control de versiones

### Issues

Cada tarea es una issue de GitHub con la misma plantilla:

| Campo | Valores |
|---|---|
| Tipo | Historia de usuario · Error · Tarea técnica · Documentación |
| Estado | Por hacer · En curso · En revisión · Hecha |
| Prioridad | Alta · Media · Baja |
| Responsable | Quien la hace |
| Revisor | Un compañero que la revisa antes de darla por terminada |

Toda issue indica el work item y la historia a la que pertenece.

### Definición de hecho

Una issue se da por terminada cuando:

1. Cumple los criterios de aceptación de su historia.
2. Tiene pruebas y la CI está en verde.
3. El revisor la ha comprobado y lo ha anotado en la issue.
4. Está integrada en `trunk` y su rama borrada.
5. No incluye secretos ni configuración personal.

### Flujo de Git (EGCFlow, apartado 3.5.3 de los apuntes)

EGCFlow se pensó para equipos que trabajan «a ráfagas», como nosotros: ni integramos todos los días de forma estricta ni dejamos ramas vivas semanas para descubrir los problemas justo antes de la entrega.

- **`main`** es la línea de **entregas**. Cuando un estado de `trunk` es suficientemente estable, se lleva a `main` y se marca con una etiqueta (1.0, 2.0, 3.1…), para que cada entrega tenga una referencia trazable. Nadie trabaja directamente en ella.
- **`trunk`** es la línea de **integración** del equipo. No tiene que estar perfecta, pero debe mantenerse en un estado razonable: **construye, pasan las pruebas básicas** y el resto puede seguir trabajando a partir de ella.
- **Cada tarea se hace en su propia rama**, con un propósito claro y un nombre que diga qué se hace (`rutinas`, `fix-series`, `docs-acta`), nunca el nombre de una persona. La rama puede durar algo más que en un modelo estricto, pero no se abandona: se **mantiene cerca de `trunk`**, se **integra en `trunk` al terminar y se borra**. Si una rama sigue existiendo, el equipo debe saber por qué.
- **Dentro del equipo no usamos pull requests.** La razón es didáctica: queremos aprender a traer cambios, mezclar ramas, resolver conflictos y comprobar el resultado directamente con Git. Los pull requests se reservan para **proponer cambios al proyecto de otro equipo**.
- Cada uno hace commits **siempre con su mismo usuario y desde su ordenador**, nunca desde la web de GitHub.
- Los mensajes de commit siguen un mismo formato e **indican la issue** a la que corresponden.
- Si la CI se pone en rojo, arreglarla es lo primero, la haya roto quien la haya roto.

El detalle (formato de los commits, nombres de ramas, etiquetas y pasos de integración y de revisión) se recoge en [`docs/guia-git.md`](../guia-git.md).

---

## 8. Toma de decisiones y conflictos

Decidimos por consenso. Si no hay manera, votamos y se hace lo que decida la mayoría. Si surge un problema, primero lo hablan los implicados. Si no se arregla, intervienen los coordinadores. Si es serio, acudimos cuanto antes al profesorado para que nos ayude a mediar. Los conflictos relevantes se anotan en el diario.

Si alguien se atasca o ve que no llega a un plazo, lo dice en cuanto lo sepa para buscar una solución juntos.

---

## 9. Compromisos

Nos comprometemos a:

- Cumplir los plazos acordados.
- Venir a las reuniones o avisar.
- Hacer nuestras tareas con cuidado y con sus pruebas.
- Mantener una actitud profesional.
- Ayudarnos: quien sepa más de un tema ayuda a quien sepa menos, porque enseñando también se aprende.

---

## 10. Incumplimientos y sanciones

| Nivel | Cuándo | Qué hacemos |
|---|---|---|
| Leve | Entregar tarde sin motivo, faltar a una reunión sin avisar o pasar 48 horas sin contestar | Se le avisa y queda apuntado en el diario |
| Reincidencia | Dos faltas leves en tres semanas | Reunión para hablarlo y se tendrá en cuenta en su grado de implicación |
| Grave | Tres faltas leves o dos semanas sin dar señales de vida | Se informa al coordinador de la asignatura |

---

## 11. Implicación, horas y uso de IA

**Horas.** Cada semana se apuntan en el diario las horas y lo que ha hecho cada uno (`docs/diario/horas.md`). Se anotan las horas reales, también las de quien dedique menos o más.

**Implicación.** Al final valoramos juntos la implicación de cada miembro del 1 al 10, entendida como el porcentaje del tiempo acordado que ha dedicado, **no como una nota**. Si no se indica lo contrario, se considera que todos han aportado por igual.

**Uso de IA.** Podemos usar herramientas de IA, pero:

- Se explica para qué se ha usado cada vez, en `docs/uso-ia.md`.
- **Cada miembro debe poder explicar y defender todo lo que haya generado la IA.** Si no se entiende, no se integra.
- No se pega en la IA ninguna contraseña ni dato personal.

**Plagio.** No se copia texto ni código sin citar la fuente. Las citas literales van entre comillas y en cursiva con su referencia, y el código reutilizado se usa solo si su licencia lo permite.

---

## 12. Entregables

| Entregable | Contenido |
|---|---|
| Documento del proyecto | Con la portada y la estructura que marca la wiki de la asignatura. |
| Entornos de despliegue | La aplicación completa, accesible o reproducible con Docker Compose. |
| Acta fundacional y diario del equipo | Actas de reuniones, decisiones, horas y grado de implicación. |
| Vídeo de demostración | Según las instrucciones de la asignatura. |

---

## 13. Riesgos

| Riesgo | Cómo lo reducimos |
|---|---|
| Solo queda un mes y hay dependencias entre work items | Empezar por WI-1 y WI-2 y dejar listo el esqueleto en la primera semana |
| Poca experiencia programando y mucho código generado por IA | Cambios pequeños, revisión por un compañero y registro del uso de IA |
| Conflictos de Git al trabajar seis a la vez sin pull requests | Ramas cortas, integrar a menudo y una carpeta por funcionalidad |
| Un miembro sin cuenta de GitHub | Crearla esta semana |
| Repartos de carga desiguales | Revisar las horas cada semana en la reunión |

---

## 14. Conformidad

Los miembros del equipo aceptan esta acta. Se revisará de forma excepcional y con el acuerdo de todos, y cada revisión queda reflejada en el historial de arriba.

| Nombre | Conforme | Fecha |
|---|---|---|
| Ibáñez Torres, Esteban | ☐ | |
| Serrano Martínez, Alberto | ☐ | |
| López Torres, Gonzalo | ☐ | |
| Márquez Ortega, Rubén | ☐ | |
| Ronquillo Bernáldez, Mario | ☐ | |
| Crespo Bravo, Antonio | ☐ | |
