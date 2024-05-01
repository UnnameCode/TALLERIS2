# Definir una lista para almacenar las tareas
tareas = []

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

# Función para ver todas las tareas en la lista
def ver_tareas():
    if tareas:
        print("Lista de tareas:")
        for index, tarea in enumerate(tareas, start=1):
            print(f"{index}. {tarea}")
    else:
        print("No hay tareas en la lista.")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    ver_tareas()
    if tareas:
        tarea_index = int(input("Ingrese el número de la tarea a eliminar: "))
        if tarea_index > 0 and tarea_index <= len(tareas):
            tarea_eliminada = tareas.pop(tarea_index - 1)
            print(f"Se ha eliminado la tarea: {tarea_eliminada}")
        else:
            print("Número de tarea inválido.")
    else:
        print("No hay tareas para eliminar.")

# Función principal para ejecutar la aplicación
def main():
    while True:
        print("\n--- Aplicación de Lista de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()