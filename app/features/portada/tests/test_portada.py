def test_portada_responde_200_con_bienvenida(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert "Bienvenido a GymHub" in respuesta.get_data(as_text=True)
