"Programa para la escuela Amadeo Sirolli"

import json
import os

ARCHIVO = "alumnos.json"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        if os.path.getsize(ARCHIVO) == 0: 
            return {"Alumnos": []}
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    else:
        return {"Alumnos": []}

def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)

def mostrar_alumnos(datos):
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
        return
    for i, alumno in enumerate(datos["Alumnos"], start=1):
        print(f"\nAlumno {i}:")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

def agregar_alumno(datos):
    nuevo = {
        "Nombre": input("Nombre del alumno: "),
        "Apellido": input("Apellido del alumno: "),
        "DNI": input("DNI del alumno: "),
        "Fecha de nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): "),
        "Tutor": input("Nombre completo del tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos["Alumnos"].append(nuevo)
    guardar_datos(datos)
    print("Alumno agregado correctamente.")

def modificar_alumno(datos):
    dni = input("Ingrese el DNI del alumno a modificar: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            print("Alumno encontrado.")
            for clave in alumno.keys():
                if clave in ["Notas", "Faltas", "Amonestaciones"]:
                    continue
                nuevo_valor = input(f"{clave} actual: {alumno[clave]} - Nuevo valor (enter para no cambiar): ")
                if nuevo_valor:
                    alumno[clave] = nuevo_valor
            guardar_datos(datos)
            print("Datos actualizados.")
            return
    print("Alumno no encontrado.")

def expulsar_alumno(datos):
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for i, alumno in enumerate(datos["Alumnos"]):
        if alumno["DNI"] == dni:
            confirmacion = input(f"¿Seguro que quiere expulsar a {alumno['Nombre']} {alumno['Apellido']}? (s/n): ")
            if confirmacion.lower() == 's':
                datos["Alumnos"].pop(i)
                guardar_datos(datos)
                print("Alumno expulsado.")
            else:
                print("Operación cancelada.")
            return
    print("Alumno no encontrado.")

def agregar_nota(datos):
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            try:
                nota = float(input("Ingrese la nota (0-10): "))
                if 0 <= nota <= 10:
                    alumno["Notas"].append(nota)
                    guardar_datos(datos)
                    print("Nota agregada.")
                else:
                    print("Nota fuera de rango.")
            except ValueError:
                print("Debe ingresar un número válido.")
            return
    print("Alumno no encontrado.")

def agregar_falta(datos):
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            alumno["Faltas"] += 1
            guardar_datos(datos)
            print("Falta registrada.")
            return
    print("Alumno no encontrado.")

def agregar_amonestacion(datos):
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            alumno["Amonestaciones"] += 1
            guardar_datos(datos)
            print("Amonestación registrada.")
            return
    print("Alumno no encontrado.")

def menu():
    while True:
        datos = cargar_datos()
        print("\n--- Gestión de Alumnos ---")
        print("1. Mostrar alumnos")
        print("2. Agregar alumno")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar alumno")
        print("5. Agregar nota")
        print("6. Registrar falta")
        print("7. Registrar amonestación")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_alumnos(datos)
        elif opcion == "2":
            agregar_alumno(datos)
        elif opcion == "3":
            modificar_alumno(datos)
        elif opcion == "4":
            expulsar_alumno(datos)
        elif opcion == "5":
            agregar_nota(datos)
        elif opcion == "6":
            agregar_falta(datos)
        elif opcion == "7":
            agregar_amonestacion(datos)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()

