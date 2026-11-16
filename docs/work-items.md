# GymHub — Work items e historias de usuario

Documento de referencia del trabajo a desarrollar. Resume y detalla la sección 4 del [acta fundacional](diario/ACTA-2026-01-fundacional.md).

## Cómo se lee

- Cada **work item (WI)** agrupa varias **historias de usuario (HU)** con el formato **Como** (rol) **quiero** (funcionalidad) **para** (beneficio).
- Cada HU tiene **criterios de aceptación** comprobables. Una HU está terminada cuando sus criterios se cumplen, tiene pruebas y la CI está en verde.
- **Prioridad:** **Alta** = imprescindible para la entrega; **Media** = importante; **Baja** = solo si sobra tiempo.
- Cada HU se convierte en una o varias issues de GitHub, con el identificador en el título: `[WI-4][HU-4.5] Temporizador de descanso`.
- Roles: **visitante** (sin sesión iniciada) y **usuario** (con sesión iniciada). Cada usuario solo ve y modifica sus propios datos, salvo lo publicado en WI-6.

## Dependencias entre work items

```
WI-1 Perfil ──► WI-2 Ejercicios ──► WI-3 Rutinas ──► WI-4 Sesiones ──► WI-5 Progreso
   │                  │                  │                                  ▲
   │                  │                  └──────────► WI-6 Compartidas      │
   └──────────────────┴─────────────────────────────────────────────────────┘
   (WI-1 aporta al usuario y a sus objetivos en todos los demás)
```

| Work item | Necesita de | Aporta a |
|---|---|---|
| WI-1 Perfil y objetivos | — | Todos (el usuario propietario); WI-5 (objetivos) |
| WI-2 Catálogo de ejercicios | WI-1 | WI-3, WI-4, WI-5 |
| WI-3 Rutinas | WI-1, WI-2 | WI-4 (iniciar una sesión desde una rutina), WI-6 |
| WI-4 Registro de sesiones | WI-1, WI-2, WI-3 | WI-5 (datos de series) |
| WI-5 Progreso y estadísticas | WI-1, WI-2, WI-4 | — |
| WI-6 Rutinas compartidas | WI-1, WI-3 | — |

**Orden recomendado:** WI-1 y WI-2 primero (son la base). Después WI-3 y WI-4 en paralelo. WI-5 y WI-6 al final. Para no bloquearse, quien dependa de otro work item usa **datos de ejemplo** (seeders) hasta que esté listo.

## Entidades previstas (provisional)

| Entidad | Work item que la crea | Qué guarda |
|---|---|---|
| Usuario | WI-1 | Datos de acceso y de perfil |
| Objetivo | WI-1 | Objetivos de entrenamiento del usuario |
| Ejercicio | WI-2 | Nombre, grupo muscular, equipamiento, descripción; del catálogo común o de un usuario |
| Rutina y sus ejercicios | WI-3 | Plan con ejercicios, series, repeticiones y descanso |
| Sesión de entreno | WI-4 | Entreno en curso o terminado, con inicio y fin |
| Serie registrada | WI-4 | Peso, repeticiones y ejercicio dentro de una sesión |
| Publicación y copia de rutina | WI-6 | Rutina publicada y de qué rutina se copió |

---

## WI-1 · Perfil y objetivos

> **Como** persona que entrena, **quiero** crear mi cuenta y fijar mis objetivos de entrenamiento, **para** tener mis datos privados y saber si los cumplo.

**Módulos previstos:** `autenticacion`, `perfil`

### HU-1.1 · Registro · Prioridad Alta
**Como** visitante, **quiero** registrarme con mi correo y una contraseña, **para** tener una cuenta propia donde guardar mi entrenamiento.
- Con datos válidos se crea la cuenta y se inicia sesión.
- Un correo ya registrado muestra un error y no crea nada.
- La contraseña se guarda cifrada, nunca en claro.
- Los errores del formulario salen en español.

### HU-1.2 · Inicio y cierre de sesión · Prioridad Alta
**Como** usuario, **quiero** iniciar y cerrar sesión, **para** acceder a mis datos con seguridad desde cualquier dispositivo.
- Con credenciales correctas entro; con incorrectas veo un aviso sin saber qué falla.
- Las páginas de la aplicación redirigen al inicio de sesión si no la he iniciado.
- Al cerrar sesión no puedo volver a ver mis datos con el botón «atrás».

### HU-1.3 · Perfil · Prioridad Media
**Como** usuario, **quiero** editar mi perfil (nombre, peso, altura, nivel de experiencia y unidad kg o lb), **para** que la aplicación se adapte a mí.
- Puedo ver y modificar mis datos y los cambios se guardan.
- No se aceptan valores absurdos (peso negativo, altura de 10 m).
- La unidad elegida se usa donde se muestran pesos.

### HU-1.4 · Objetivos de entrenamiento · Prioridad Alta
**Como** usuario, **quiero** fijar mis objetivos (entrenos por semana y una meta como ganar fuerza o músculo, o perder grasa), **para** saber si los estoy cumpliendo.
- Puedo crear, editar y eliminar mis objetivos.
- WI-5 usa los entrenos por semana para mostrar el cumplimiento.

### HU-1.5 · Peso corporal · Prioridad Baja
**Como** usuario, **quiero** registrar mi peso corporal con su fecha, **para** ver cómo evoluciona.
- Puedo añadir una medida y ver la lista ordenada por fecha.
- WI-5 puede mostrar la gráfica de esa evolución.

---

## WI-2 · Catálogo de ejercicios

> **Como** usuario, **quiero** consultar los ejercicios por grupo muscular y crear los míos, **para** encontrar rápido qué entrenar y registrar lo que no está en el catálogo.

**Módulo previsto:** `ejercicios`

### HU-2.1 · Consultar el catálogo · Prioridad Alta
**Como** usuario, **quiero** ver el catálogo de ejercicios filtrado por grupo muscular, **para** encontrar rápido qué entrenar.
- Existe un catálogo inicial de ejercicios cargado con datos de ejemplo (unos 40, repartidos por todos los grupos musculares).
- Al elegir un grupo muscular solo salen sus ejercicios.
- Si no hay resultados, se muestra un mensaje claro.

### HU-2.2 · Buscar y ver el detalle · Prioridad Media
**Como** usuario, **quiero** buscar por nombre y abrir la ficha de un ejercicio (músculo principal y secundarios, equipamiento, descripción), **para** ejecutarlo bien.
- La búsqueda no distingue mayúsculas ni tildes.
- La ficha muestra todos los datos del ejercicio.

### HU-2.3 · Crear ejercicios propios · Prioridad Alta
**Como** usuario, **quiero** crear mis propios ejercicios, **para** registrar los que no están en el catálogo.
- Mis ejercicios solo los veo yo y aparecen junto a los del catálogo.
- El nombre y el grupo muscular son obligatorios.
- No puedo crear dos ejercicios míos con el mismo nombre.

### HU-2.4 · Editar y eliminar ejercicios propios · Prioridad Media
**Como** usuario, **quiero** editar y borrar mis ejercicios, **para** mantener mi lista ordenada.
- No puedo modificar ni borrar los del catálogo ni los de otros usuarios.
- Si un ejercicio ya se ha usado en una sesión registrada, se archiva en lugar de borrarse, para no perder mi historial.

---

## WI-3 · Rutinas

> **Como** usuario, **quiero** montar rutinas con ejercicios, series y repeticiones, **para** tener un plan de entreno definido.

**Módulo previsto:** `rutinas`

### HU-3.1 · Crear y listar rutinas · Prioridad Alta
**Como** usuario, **quiero** crear una rutina con un nombre y ver todas las mías, **para** organizar mi entrenamiento (por ejemplo, «Pecho y tríceps»).
- El nombre es obligatorio.
- Veo solo mis rutinas.

### HU-3.2 · Añadir ejercicios a la rutina · Prioridad Alta
**Como** usuario, **quiero** añadir ejercicios del catálogo a una rutina indicando series, repeticiones objetivo y tiempo de descanso, **para** tener un plan definido.
- Puedo añadir ejercicios del catálogo y los míos.
- Las series, repeticiones y descanso deben ser números positivos.
- El descanso por ejercicio lo usa el temporizador de WI-4.

### HU-3.3 · Ordenar y quitar ejercicios · Prioridad Media
**Como** usuario, **quiero** reordenar y quitar ejercicios de una rutina, **para** ajustarla a como entreno.
- El orden se conserva al volver a abrir la rutina.

### HU-3.4 · Editar, duplicar y eliminar rutinas · Prioridad Media
**Como** usuario, **quiero** editar, duplicar y eliminar mis rutinas, **para** crear variantes sin empezar de cero.
- Al duplicar se copian todos sus ejercicios con sus series y repeticiones.
- Al eliminar una rutina no se pierden las sesiones ya registradas con ella.
- Se pide confirmación antes de eliminar.

---

## WI-4 · Registro de sesiones

> **Como** usuario, **quiero** abrir una sesión de entreno y apuntar en ella cada serie, con un temporizador que me avise cuando haya descansado, **para** registrar mi entreno en directo sin perder el ritmo ni recargar la página.

**Módulo previsto:** `sesiones`

**Idea.** Es una **sesión abierta**: la empiezo al llegar al gimnasio y la voy rellenando mientras entreno. Se guarda en el servidor, así que sigue abierta si recargo la página, cierro el navegador o cambio de dispositivo, hasta que la finalizo.

### HU-4.1 · Abrir una sesión · Prioridad Alta
**Como** usuario, **quiero** abrir una sesión vacía o a partir de una de mis rutinas, **para** empezar a registrar sin preparar nada más.
- Solo puedo tener **una sesión abierta** a la vez.
- Si la abro desde una rutina, sus ejercicios aparecen ya en la sesión con sus series y repeticiones objetivo.
- Si ya tengo una abierta, la aplicación me lleva a ella en lugar de crear otra.

### HU-4.2 · Añadir ejercicios sobre la marcha · Prioridad Media
**Como** usuario, **quiero** añadir ejercicios a la sesión abierta, **para** entrenar algo que no estaba planificado.
- Puedo elegir cualquier ejercicio del catálogo o propio.

### HU-4.3 · Apuntar una serie sin recargar · Prioridad Alta
**Como** usuario, **quiero** apuntar el peso y las repeticiones de cada serie sin recargar la página, **para** registrar rápido entre series.
- Al pulsar «Apuntar serie» aparece en la lista al instante, sin recargar.
- Peso y repeticiones son obligatorios y válidos (repeticiones ≥ 1, peso ≥ 0).
- Si falla el servidor, se avisa y la serie no se da por guardada.
- Se puede usar bien desde el móvil (botones grandes, teclado numérico).

### HU-4.4 · Corregir una serie · Prioridad Media
**Como** usuario, **quiero** editar o borrar una serie ya apuntada, **para** corregir errores.
- Los cambios se reflejan sin recargar la página.

### HU-4.5 · Temporizador de descanso · Prioridad Alta
**Como** usuario, **quiero** que al apuntar una serie arranque un temporizador de descanso y me avise cuando termine, **para** empezar la siguiente serie a tiempo.
- El tiempo por defecto es el descanso de ese ejercicio en la rutina; si no hay rutina, un valor general que puedo cambiar.
- Se ve la cuenta atrás y puedo **pausar, sumar o restar 15 s y saltarlo**.
- Al llegar a cero aviso con **sonido, vibración (si el dispositivo la tiene) y un cambio visual** claro. Opcionalmente, una notificación del navegador si el usuario da permiso.
- El temporizador **sigue siendo correcto** si cambio de pestaña o recargo la página. Para ello se guarda el instante de fin y no se cuenta segundo a segundo.
- Apuntar otra serie reinicia el temporizador.

### HU-4.6 · Duración y volumen de la sesión · Prioridad Media
**Como** usuario, **quiero** ver cuánto llevo entrenando y el volumen acumulado (peso × repeticiones), **para** controlar el esfuerzo.
- El cronómetro de la sesión corre mientras está abierta y es correcto tras recargar.
- El volumen se actualiza al apuntar, editar o borrar series.

### HU-4.7 · Repetir o precargar la serie anterior · Prioridad Baja
**Como** usuario, **quiero** que el formulario proponga el peso y repeticiones de la serie anterior o de mi última sesión con ese ejercicio, **para** apuntar con un solo toque.
- Hay un botón «Repetir serie».
- Los valores propuestos se pueden cambiar.

### HU-4.8 · Finalizar o descartar la sesión · Prioridad Alta
**Como** usuario, **quiero** finalizar la sesión y ver un resumen (duración, ejercicios, series y volumen) o descartarla, **para** que quede en mi historial o no deje rastro.
- Al finalizar, la sesión pasa al historial y ya no puedo añadirle series, salvo corregirlas desde el historial.
- Descartar pide confirmación y borra la sesión.
- Una sesión finalizada sin ninguna serie no se guarda.

---

## WI-5 · Progreso y estadísticas

> **Como** usuario, **quiero** ver mi historial, mis récords y la evolución de cada ejercicio, **para** comprobar que estoy mejorando.

**Módulo previsto:** `progreso`

### HU-5.1 · Historial de sesiones · Prioridad Alta
**Como** usuario, **quiero** ver mis sesiones pasadas y abrir el detalle de cada una, **para** recordar qué hice.
- La lista va de la más reciente a la más antigua.
- El detalle muestra ejercicios, series, pesos y repeticiones.
- Se puede filtrar por rango de fechas o por ejercicio.

### HU-5.2 · Récords personales · Prioridad Alta
**Como** usuario, **quiero** ver mis récords por ejercicio (mayor peso, mayor 1RM estimado y mayor volumen), **para** saber cuáles son mis marcas.
- El 1RM estimado se calcula con una fórmula documentada (por ejemplo, Epley).
- Los récords se actualizan solos al registrar sesiones.

### HU-5.3 · Evolución de un ejercicio · Prioridad Alta
**Como** usuario, **quiero** ver una gráfica de la evolución de un ejercicio en el tiempo, **para** comprobar que progreso.
- Puedo elegir el ejercicio y la métrica (peso máximo, 1RM estimado o volumen).
- Con pocos datos se muestra un mensaje en vez de una gráfica vacía.

### HU-5.4 · Aviso de récord · Prioridad Media
**Como** usuario, **quiero** que se me avise cuando bato un récord, **para** motivarme.
- Al finalizar una sesión (WI-4), el resumen destaca los récords batidos.

### HU-5.5 · Cumplimiento de objetivos y constancia · Prioridad Media
**Como** usuario, **quiero** ver cuántos entrenos llevo esta semana frente a mi objetivo y mi racha de semanas cumplidas, **para** mantener la constancia.
- Usa los objetivos de WI-1 y las sesiones finalizadas de WI-4.
- Si no he fijado objetivo, se invita a crearlo.

---

## WI-6 · Rutinas compartidas

> **Como** usuario, **quiero** publicar mis rutinas y copiar las de otros, **para** aprovechar planes ya probados sin empezar de cero.

**Módulo previsto:** `comunidad`

### HU-6.1 · Publicar y retirar una rutina · Prioridad Alta
**Como** usuario, **quiero** publicar una de mis rutinas y poder retirarla, **para** que otros la vean y la usen.
- Solo yo puedo publicar o retirar mis rutinas.
- Al retirarla deja de verse, pero las copias que ya hicieron otros se mantienen.

### HU-6.2 · Explorar rutinas públicas · Prioridad Alta
**Como** usuario, **quiero** explorar las rutinas publicadas y buscarlas por nombre o grupo muscular, **para** encontrar planes ya hechos.
- Veo el nombre, el autor, los ejercicios y cuántas veces se ha copiado.
- Puedo ordenar por más copiadas o por más recientes.

### HU-6.3 · Copiar una rutina («fork») · Prioridad Alta
**Como** usuario, **quiero** copiar una rutina pública a mi cuenta, **para** modificarla a mi gusto sin afectar al original.
- La copia aparece entre mis rutinas, editable, y recuerda de cuál procede.
- Si la rutina usa ejercicios propios de su autor, se copian también a mi cuenta.
- Si el autor cambia o retira el original, mi copia no se ve afectada.

### HU-6.4 · Estadísticas de mis rutinas publicadas · Prioridad Baja
**Como** autor, **quiero** ver cuántas veces se ha copiado cada una de mis rutinas, **para** saber si resulta útil.

---

## Cómo trabajar con este documento

- **Antes de empezar una HU:** crear la issue en GitHub con la plantilla del equipo, con el identificador en el título y los criterios de aceptación copiados.
- **Mientras se hace:** una rama por tarea, tests de cada criterio y commits que indiquen la issue.
- **Al terminar:** cumplir la definición de hecho del acta (sección 7).
- Si una HU cambia de alcance, se actualiza este documento y se anota en el diario.
