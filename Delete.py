def test_eliminar_tarea():
    tarea = crear_tarea("Estudiar para el examen de matemáticas", "2024-02-20")
    eliminar_tarea(tarea)
    assert tarea not in lista_de_tareas
