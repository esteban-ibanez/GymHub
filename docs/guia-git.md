# GymHub — Guía de Git (EGCFlow)

Esta guía explica cómo usamos Git en GymHub. Sigue el modelo **EGCFlow** (apuntes de la asignatura, apartado 3.5.3), que encaja con equipos que trabajan «a ráfagas»: ni se integra todos los días de forma estricta ni se dejan ramas vivas durante semanas, para no descubrir problemas de integración justo antes de la entrega.

> **Cómo se lee.** Lo que viene de los apuntes y del acta es **norma**. Lo marcado como **Propuesta** es una decisión nuestra que el equipo debe aprobar (está recogida al final).

## 1. Las ramas

```
main    solo entregas, cada una con su etiqueta (1.0, 2.0, 2.1…)
  ▲
  │  se lleva a main un estado estable de trunk
  │
trunk   integración del equipo (siempre en un estado razonable)
  ▲  │
  │  │  se trae trunk a la rama para mantenerla cerca
  │  ▼
tarea   una rama por tarea: nace de trunk, vuelve a trunk y se borra
```

| Rama | Para qué sirve | Reglas |
|---|---|---|
| `main` | Línea de **entregas**. | Solo recibe estados estables de `trunk`, y cada uno se marca con una **etiqueta**. **Nadie trabaja directamente en ella.** |
| `trunk` | Línea de **integración** del equipo. | No tiene que estar perfecta, pero debe mantenerse en un **estado razonable**: construye, pasan las pruebas básicas y el resto puede seguir trabajando a partir de ella. |
| Rama de tarea | Un cambio con un propósito claro: una funcionalidad, una corrección, documentación, una refactorización. | Nace de `trunk`, se mantiene cerca de ella, se integra al terminar y **se borra**. |

`main` y `trunk` **no se destruyen nunca**. `trunk` es la rama por defecto del repositorio, para que todos empiecen siempre en ella.

## 2. Nombres de ramas

El nombre dice **qué se hace**, nunca quién lo hace. Todo en minúsculas, con guiones y sin tildes.

| Tipo | Patrón | Ejemplos |
|---|---|---|
| Funcionalidad | `<tema>` | `registro`, `temporizador-descanso`, `rutinas-publicas` |
| Corrección | `fix-<tema>` | `fix-series`, `fix-filtro-musculo` |
| Documentación | `docs-<tema>` | `docs-acta`, `docs-despliegue` |
| Refactorización | `refactor-<tema>` | `refactor-servicios-rutinas` |

**Mal:** `esteban`, `rama-de-alberto`, `prueba`, `nueva`, `cambios`. Tampoco valen los nombres automáticos de herramientas de IA (`claude/…`): hay que renombrar la rama o crearla con un nombre correcto desde el principio.

## 3. Commits

- Cada persona hace commits **siempre con su mismo usuario y desde su ordenador**, nunca desde la web de GitHub. Se configura una vez:

```bash
git config user.name "Nombre Apellido"
git config user.email "correo-de-tu-cuenta-de-github"
```

- **Propuesta: formato del mensaje.** Una primera línea con la **issue**, un verbo en imperativo y qué se ha hecho, en español y sin punto final:

```
#23 Añade el temporizador de descanso
#31 Corrige el cálculo del volumen al borrar una serie
#8 Documenta el arranque con Docker
```

  Máximo unos 72 caracteres en la primera línea. Si hace falta explicar el porqué, se deja una línea en blanco y se escribe en el cuerpo. El `#23` enlaza el commit con su issue en GitHub y nos da la trazabilidad que pide la asignatura.
- **Un commit, un cambio lógico.** Mensajes como «cambios» o «arreglo» no sirven.
- **No se suben** contraseñas, el `.env` ni la configuración del IDE. El `.gitignore` incluye como mínimo: `.env`, `.venv/`, `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, `.coverage`, `htmlcov/`, `instance/`, `.vscode/` y `.idea/`.
- Si usas Claude Code, **ejecútalo en tu ordenador** (terminal o editor) y no en una sesión remota en la nube: así los commits salen de tu máquina y con tu usuario.

## 4. El ciclo de una tarea

Cada tarea sale de una **issue**. Estos son los pasos, de principio a fin.

**1. Crea la rama desde `trunk` actualizada**

```bash
git switch trunk
git pull
git switch -c temporizador-descanso
```

**2. Trabaja con commits pequeños.** Al terminar la primera sesión de trabajo, sube la rama para que no viva solo en tu ordenador y para que tu revisor pueda verla:

```bash
git push -u origin temporizador-descanso
```

**3. Mantén la rama cerca de `trunk`.** Al empezar cada sesión de trabajo, trae a tu rama lo nuevo de `trunk`. Los conflictos se resuelven aquí, en tu rama, y no en `trunk`:

```bash
git fetch origin
git merge origin/trunk
```

**4. Comprueba antes de integrar:**

```bash
ruff check . && ruff format --check . && pytest -q
```

**5. Revisión.** Tu revisor comprueba la rama (apartado 6) y lo anota en la issue.

**6. Integra en `trunk`.** Trae `trunk`, mezcla tu rama (**Propuesta:** con `--no-ff`, para que quede un commit de fusión por tarea), **vuelve a comprobar el resultado** y sube:

```bash
git switch trunk
git pull
git merge --no-ff temporizador-descanso
ruff check . && ruff format --check . && pytest -q
git push
```

Si el `git push` falla porque otra persona ha subido antes, haz `git pull`, comprueba otra vez y vuelve a subir.

**7. Borra la rama**, en tu ordenador y en GitHub:

```bash
git branch -d temporizador-descanso
git push origin --delete temporizador-descanso
```

**8. Cierra la issue** cuando se cumpla la definición de hecho del acta.

## 5. Conflictos

Un conflicto aparece cuando dos personas han tocado las mismas líneas. No es un error, es normal. Pasos:

1. `git merge origin/trunk` dice que hay conflictos. `git status` muestra los ficheros afectados.
2. Abre cada fichero. Verás marcas `<<<<<<<`, `=======` y `>>>>>>>` con las dos versiones. Deja el resultado correcto y borra las marcas.
3. `git add <fichero>` para cada uno y `git commit` para terminar la mezcla.
4. Ejecuta `ruff` y `pytest`: que no haya marcas ni errores.
5. Si te pierdes, `git merge --abort` deja todo como estaba y puedes pedir ayuda a un compañero.

Si el conflicto afecta al trabajo de otra persona, habladlo antes de resolverlo.

## 6. Revisión sin pull requests

Cada issue tiene un **revisor**, que es un compañero. Como no hay pull requests, la revisión se hace con Git:

```bash
git fetch origin
git switch temporizador-descanso
pytest -q                                  # y ruff
git diff origin/trunk...HEAD               # lo que aporta la rama
```

El revisor lee los cambios, prueba la funcionalidad, comprueba que cada criterio de aceptación de la historia se cumple y **anota en la issue** el resultado y qué ha revisado. Si hay algo que cambiar, se lo dice al responsable en la issue. **Propuesta:** la revisión se hace antes de integrar en `trunk`, para que `trunk` reciba trabajo ya revisado.

## 7. Entregas: `main` y etiquetas

Cuando un estado de `trunk` es suficientemente estable para entregar, se lleva a `main` y se marca con una etiqueta. Así cada entrega tiene una referencia trazable en el repositorio.

```bash
git switch trunk
git pull
ruff check . && ruff format --check . && pytest -q
git switch main
git pull
git merge --no-ff trunk
git tag -a 1.0 -m "Entrega 1.0: descripción breve"
git push
git push origin 1.0
git switch trunk
```

- Etiquetas: `1.0`, `2.0`… para entregas y `1.1`, `2.1`… para correcciones posteriores. Sin prefijo `v`.
- La entrega final es el **16/12/2026**.
- **Propuesta:** las entregas las hacen los coordinadores, tras acordarlo en la reunión, y se anotan en el diario con la etiqueta y qué contiene.

## 8. Ramas que sobran

Las ramas que dejan de usarse **se destruyen**: si una sigue existiendo, el equipo debe saber por qué, qué contiene y qué tiene que pasar para cerrarla.

- **Propuesta:** una rama no pasa más de **una semana sin integrarse**. Si la tarea es más grande, se divide en issues más pequeñas. Cada semana, en la reunión, se revisan las ramas abiertas:

```bash
git fetch --prune
git branch -r                       # ramas que existen en GitHub
git branch -r --merged origin/trunk # ya integradas: se pueden borrar
```

## 9. Pull requests: solo entre equipos

Dentro del equipo **no usamos pull requests**. La razón es didáctica: queremos aprender a traer cambios, mezclar ramas, resolver conflictos y comprobar el resultado con Git, sin que el proceso quede oculto detrás de un botón.

Los pull requests se reservan para **proponer cambios al proyecto de otro equipo**, donde sí hay una frontera clara entre proyectos y el equipo receptor decide si acepta o no.

## 10. CI y protecciones en GitHub

- La CI (GitHub Actions) se ejecuta en **cada push**, a cualquier rama: `ruff check`, `ruff format --check` y `pytest`. Si `trunk` se pone en rojo, **arreglarla es lo primero**, la haya roto quien la haya roto.
- Como no hay pull requests, **no se activa** la regla de «exigir pull request antes de fusionar» ni los *required status checks* de las prácticas.
- **Propuesta:** proteger `main` y `trunk` solo contra borrado y `push --force`.
- **Propuesta:** cada miembro instala el hook `pre-push` de las prácticas (`.git/hooks/pre-push` con las tres comprobaciones y `chmod +x`). No se sube a GitHub, así que lo instala cada uno en su ordenador.

## 11. Lo que no se hace

- Trabajar o hacer commits directamente en `main`. Y en `trunk`, solo se entra con la integración de una rama de tarea.
- Ramas con el nombre de una persona, ramas sin propósito o ramas abandonadas.
- `git push --force`, `git reset --hard` sobre ramas compartidas o `--no-verify`, sin acordarlo antes.
- Commits desde la web de GitHub.
- Subir `.env`, contraseñas o configuración del IDE.
- Integrar en `trunk` sin pasar `ruff` y `pytest`.

## 12. Puesta en marcha del repositorio (coordinadores, una sola vez)

1. Crear el repositorio en GitHub, con README y `.gitignore` de Python, en una cuenta u organización del equipo.
2. Añadir a los 6 miembros como colaboradores con permiso de escritura. Antonio Crespo necesita antes su cuenta de GitHub.
3. Crear `trunk` desde `main` y establecerla como **rama por defecto** (Settings → Branches).
4. Añadir a `trunk` el esqueleto del proyecto (`ci.yml`, `.gitignore`, `.env.example`, estructura de carpetas) en una rama de tarea, como cualquier otra tarea.
5. Crear las etiquetas (tipo, estado, prioridad y work item) y las issues de la Iteración 0 con `python scripts/preparar_repositorio.py --issues`. Antes se puede probar con `--simulacro`.
6. Aplicar las protecciones del apartado 10, si el equipo las aprueba.

## Decisiones propuestas pendientes de aprobar

| Tema | Propuesta |
|---|---|
| Formato de commit | `#<issue> Verbo en imperativo y descripción` |
| Mezcla a `trunk` y `main` | `git merge --no-ff` (un commit de fusión por tarea) |
| Momento de la revisión | Antes de integrar en `trunk` |
| Vida máxima de una rama | Una semana sin integrar |
| Quién hace las entregas a `main` | Los coordinadores, tras acordarlo en reunión |
| Protección en GitHub | `main` y `trunk` contra borrado y `push --force` |
| Hook `pre-push` | Recomendado para todos |
