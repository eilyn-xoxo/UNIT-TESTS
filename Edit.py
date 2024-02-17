def test_editar_tarea():
    tarea = crear_tarea("Estudiar para el examen de matemáticas", "2024-02-20")
    editar_tarea(tarea, nombre="Estudiar para el examen de física")
    assert tarea.nombre == "Estudiar para el examen de física"
