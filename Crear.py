def test_crear_tarea():
    tarea = crear_tarea("Estudiar para el examen de matemáticas", "2024-02-20")
    assert tarea.nombre == "Estudiar para el examen de matemáticas"
    assert tarea.fecha_entrega == "2024-02-20"
