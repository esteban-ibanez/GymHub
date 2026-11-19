"""Datos de ejemplo del módulo de ejercicios: el catálogo inicial (HU-2.1).

Solo para desarrollo y pruebas: nunca se cargan en producción.
"""

from app.features.ejercicios.services import crear_ejercicio, listar_ejercicios

# (nombre, grupo muscular, músculos secundarios, equipamiento, descripción)
EJERCICIOS_CATALOGO = [
    # Pecho
    (
        "Press de banca",
        "pecho",
        "tríceps, hombros",
        "Barra y banco plano",
        "Tumbado en el banco, baja la barra al pecho y empújala hasta estirar los brazos.",
    ),
    (
        "Press inclinado con mancuernas",
        "pecho",
        "hombros, tríceps",
        "Mancuernas y banco inclinado",
        "Con el banco a unos 30 grados, empuja las mancuernas hacia arriba y bájalas despacio.",
    ),
    (
        "Aperturas con mancuernas",
        "pecho",
        "hombros",
        "Mancuernas y banco plano",
        "Con los codos algo flexionados, abre los brazos en arco y vuelve a juntarlos.",
    ),
    (
        "Fondos en paralelas",
        "pecho",
        "tríceps, hombros",
        "Paralelas",
        "Inclina el tronco hacia delante, baja flexionando los codos y sube empujando.",
    ),
    (
        "Flexiones",
        "pecho",
        "tríceps, hombros, abdomen",
        "Peso corporal",
        "Con el cuerpo recto, baja el pecho hasta casi tocar el suelo y empuja.",
    ),
    # Espalda
    (
        "Dominadas",
        "espalda",
        "bíceps",
        "Barra de dominadas",
        "Colgado con agarre prono, sube hasta pasar la barbilla por encima de la barra.",
    ),
    (
        "Remo con barra",
        "espalda",
        "bíceps, hombros",
        "Barra",
        "Con el tronco inclinado y la espalda recta, lleva la barra hacia el abdomen.",
    ),
    (
        "Jalón al pecho",
        "espalda",
        "bíceps",
        "Polea alta",
        "Sentado, tira de la barra hacia la parte alta del pecho juntando las escápulas.",
    ),
    (
        "Remo con mancuerna",
        "espalda",
        "bíceps",
        "Mancuerna y banco",
        "Apoyado en el banco con una mano, lleva la mancuerna hacia la cadera.",
    ),
    (
        "Peso muerto",
        "espalda",
        "glúteos, piernas",
        "Barra",
        "Con la espalda recta, levanta la barra del suelo extendiendo caderas y rodillas.",
    ),
    # Hombros
    (
        "Press militar",
        "hombros",
        "tríceps",
        "Barra",
        "De pie, empuja la barra desde los hombros hasta estirar los brazos sobre la cabeza.",
    ),
    (
        "Elevaciones laterales",
        "hombros",
        None,
        "Mancuernas",
        "Con los brazos casi rectos, sube las mancuernas por los lados hasta los hombros.",
    ),
    (
        "Elevaciones frontales",
        "hombros",
        "pecho",
        "Mancuernas",
        "Sube las mancuernas por delante del cuerpo hasta la altura de los ojos.",
    ),
    (
        "Pájaros",
        "hombros",
        "espalda",
        "Mancuernas",
        "Con el tronco inclinado, abre los brazos hacia los lados apretando los hombros.",
    ),
    # Bíceps
    (
        "Curl con barra",
        "bíceps",
        None,
        "Barra",
        "De pie y con los codos pegados al cuerpo, sube la barra flexionando los brazos.",
    ),
    (
        "Curl con mancuernas",
        "bíceps",
        None,
        "Mancuernas",
        "Sube las mancuernas alternando los brazos y girando la muñeca hacia arriba.",
    ),
    (
        "Curl martillo",
        "bíceps",
        "antebrazo",
        "Mancuernas",
        "Sube las mancuernas con las palmas mirándose entre sí.",
    ),
    (
        "Curl en banco Scott",
        "bíceps",
        None,
        "Barra Z y banco Scott",
        "Con los brazos apoyados en el banco, sube la barra sin despegar los codos.",
    ),
    # Tríceps
    (
        "Press francés",
        "tríceps",
        None,
        "Barra Z y banco plano",
        "Tumbado, baja la barra hacia la frente flexionando solo los codos y súbela.",
    ),
    (
        "Extensión en polea",
        "tríceps",
        None,
        "Polea alta",
        "De pie, empuja la cuerda o la barra hacia abajo hasta estirar los brazos.",
    ),
    (
        "Fondos entre bancos",
        "tríceps",
        "hombros, pecho",
        "Dos bancos",
        "Con las manos en un banco detrás de ti, baja flexionando los codos y sube.",
    ),
    (
        "Patada de tríceps",
        "tríceps",
        None,
        "Mancuerna",
        "Con el tronco inclinado, estira el brazo hacia atrás manteniendo el codo fijo.",
    ),
    # Piernas
    (
        "Sentadilla",
        "piernas",
        "glúteos, abdomen",
        "Barra",
        "Con la barra en la espalda, baja hasta que los muslos queden paralelos al suelo y sube.",
    ),
    (
        "Prensa de piernas",
        "piernas",
        "glúteos",
        "Máquina de prensa",
        "Sentado en la máquina, empuja la plataforma sin bloquear del todo las rodillas.",
    ),
    (
        "Zancadas",
        "piernas",
        "glúteos",
        "Mancuernas",
        "Da un paso largo hacia delante, baja la rodilla de atrás casi hasta el suelo y vuelve.",
    ),
    (
        "Extensión de cuádriceps",
        "piernas",
        None,
        "Máquina de extensiones",
        "Sentado, estira las piernas hasta dejarlas rectas y bájalas despacio.",
    ),
    (
        "Curl femoral",
        "piernas",
        None,
        "Máquina de curl femoral",
        "Tumbado boca abajo, flexiona las rodillas llevando los talones hacia los glúteos.",
    ),
    (
        "Elevación de talones",
        "piernas",
        None,
        "Máquina o peso corporal",
        "De pie, sube sobre la punta de los pies y baja despacio.",
    ),
    # Glúteos
    (
        "Hip thrust",
        "glúteos",
        "piernas",
        "Barra y banco",
        "Con la espalda apoyada en el banco, sube la cadera empujando la barra hasta alinearla.",
    ),
    (
        "Puente de glúteos",
        "glúteos",
        "piernas",
        "Peso corporal",
        "Tumbado boca arriba con las rodillas flexionadas, sube la cadera y aprieta los glúteos.",
    ),
    (
        "Patada de glúteo en polea",
        "glúteos",
        None,
        "Polea baja",
        "Con el tobillo enganchado a la polea, lleva la pierna hacia atrás sin arquear la espalda.",
    ),
    (
        "Peso muerto rumano",
        "glúteos",
        "piernas, espalda",
        "Barra",
        "Con las rodillas casi rectas, baja la barra pegada a las piernas y sube con la cadera.",
    ),
    # Abdomen
    (
        "Plancha",
        "abdomen",
        "hombros",
        "Peso corporal",
        "Apoyado en antebrazos y puntas de los pies, mantén el cuerpo recto el tiempo indicado.",
    ),
    (
        "Crunch",
        "abdomen",
        None,
        "Peso corporal",
        "Tumbado boca arriba, despega los hombros del suelo contrayendo el abdomen.",
    ),
    (
        "Elevación de piernas colgado",
        "abdomen",
        None,
        "Barra de dominadas",
        "Colgado de la barra, sube las piernas hasta la horizontal sin balancearte.",
    ),
    (
        "Rueda abdominal",
        "abdomen",
        "hombros, espalda",
        "Rueda abdominal",
        "De rodillas, rueda hacia delante con el abdomen firme y vuelve a la posición inicial.",
    ),
    # Cardio
    (
        "Carrera en cinta",
        "cardio",
        "piernas",
        "Cinta de correr",
        "Corre a ritmo constante o alternando ritmos durante el tiempo indicado.",
    ),
    (
        "Bicicleta estática",
        "cardio",
        "piernas",
        "Bicicleta estática",
        "Pedalea a una intensidad que puedas mantener durante el tiempo indicado.",
    ),
    (
        "Remo en máquina",
        "cardio",
        "espalda, piernas",
        "Máquina de remo",
        "Empuja con las piernas y tira con los brazos en un movimiento continuo.",
    ),
    (
        "Comba",
        "cardio",
        "piernas",
        "Comba",
        "Salta la cuerda con saltos cortos sobre la punta de los pies.",
    ),
]


def cargar_ejercicios_ejemplo():
    """Carga el catálogo inicial si está vacío y devuelve cuántos ejercicios ha creado.

    Si ya hay ejercicios no hace nada, para poder ejecutar `flask seed-db` varias
    veces sin duplicar el catálogo.
    """
    if listar_ejercicios():
        return 0
    for nombre, grupo, secundarios, equipamiento, descripcion in EJERCICIOS_CATALOGO:
        crear_ejercicio(nombre, grupo, secundarios, equipamiento, descripcion)
    return len(EJERCICIOS_CATALOGO)
