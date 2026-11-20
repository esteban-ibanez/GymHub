from app.features.ejercicios.services import crear_ejercicio


def test_catalogo_muestra_todos_los_ejercicios(cliente):
    crear_ejercicio("Sentadilla", "piernas")
    crear_ejercicio("Press de banca", "pecho")

    respuesta = cliente.get("/ejercicios/")

    assert respuesta.status_code == 200
    html = respuesta.get_data(as_text=True)
    assert "Sentadilla" in html
    assert "Press de banca" in html


def test_catalogo_filtrado_solo_muestra_ese_grupo(cliente):
    crear_ejercicio("Sentadilla", "piernas")
    crear_ejercicio("Press de banca", "pecho")

    html = cliente.get("/ejercicios/?grupo=pecho").get_data(as_text=True)

    assert "Press de banca" in html
    assert "Sentadilla" not in html


def test_catalogo_sin_resultados_muestra_mensaje(cliente):
    crear_ejercicio("Sentadilla", "piernas")

    html = cliente.get("/ejercicios/?grupo=cardio").get_data(as_text=True)

    assert "No hay ejercicios para este grupo muscular." in html
    assert "Sentadilla" not in html


def test_catalogo_con_grupo_inexistente_muestra_mensaje(cliente):
    crear_ejercicio("Sentadilla", "piernas")

    respuesta = cliente.get("/ejercicios/?grupo=inventado")

    assert respuesta.status_code == 200
    assert "No hay ejercicios para este grupo muscular." in respuesta.get_data(as_text=True)


def test_menu_enlaza_al_catalogo(cliente):
    html = cliente.get("/").get_data(as_text=True)

    assert 'href="/ejercicios/"' in html
