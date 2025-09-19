# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 21:14:35 2025

@author: meish
"""

# Estructura de datos
registros = []

# Funciones
def agregar_registro():
    try:
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa la edad: "))
        fecha = input("Ingresa la fecha (año-mes-dia): ")
        matricula = input("Ingresa la matrícula: ")
        registro = {
            "nombre": nombre,
            "edad": edad,
            "fecha": fecha,
            "matricula": matricula
        }
        registros.append(registro)
        print("Registro agregado")
        print("Función agregar ejecutada correctamente")
    except ValueError:
        print("Error: Edad no valida")

def listar_registros():
    try:
        if not registros:
            raise ValueError("No hay registros")
        for i, registro in enumerate(registros):
            print(f"Registro {i+1}:")
            print(f"Nombre: {registro['nombre']}")
            print(f"Edad: {registro['edad']}")
            print(f"Fecha: {registro['fecha']}")
            print(f"Matrícula: {registro['matricula']}")
            print("------------------------")
    except ValueError as e:
        print(f"Error: {e}")

def buscar_registro_por_nombre():
    try:
        print("Ejecutando búsqueda por nombre")
        nombre = input("Ingrese el nombre que desea buscar: ")
        resultados = [registro for registro in registros if registro["nombre"].lower() == nombre.lower()]
        if not resultados:
            raise ValueError("No se encontro ningún registro")
        for registro in resultados:
            print(f"Nombre: {registro['nombre']}")
            print(f"Edad: {registro['edad']}")
            print(f"Fecha: {registro['fecha']}")
            print(f"Matrícula: {registro['matricula']}")
            
            print("Función buscar registro por nombre ejecutada correctamente")
            print("------------------------")
    except ValueError as e:
        print(f"Error: {e}")

def buscar_registro_por_matricula():
    try:
        print("Ejecutando búsqueda por matrícula")
        matricula = input("Ingresa la matrícula a buscar: ")
        resultados = [registro for registro in registros if registro["matricula"].lower() == matricula.lower()]
        if not resultados:
            raise ValueError("No se encontraron registros")
        for registro in resultados:
            print(f"Nombre: {registro['nombre']}")
            print(f"Edad: {registro['edad']}")
            print(f"Fecha: {registro['fecha']}")
            print(f"Matrícula: {registro['matricula']}")
            
            print("Función buscar registro por matrícula ejecutada correctamente")
            print("------------------------")
    except ValueError as e:
        print(f"Error: {e}")

def eliminar_registro_por_matricula():
    try:
        matricula = input("Ingresa la matrícula a eliminar: ")
        for registro in registros:
            if registro["matricula"].lower() == matricula.lower():
                registros.remove(registro)
                print("Ejecutando función eliminar por matrícula...")
                print("Registro eliminado con éxito")
                print("Función eliminar por matrícula finalizada")
                return
        raise ValueError("No se encontró el registro")
    except ValueError as e:
        print(f"Error: {e}")

def eliminar_registro_por_indice():
    try:
        indice = int(input("Ingresa el índice del registro a eliminar: "))
        if indice < 0 or indice >= len(registros):
            raise ValueError("Índice inválido")
        del registros[indice]
        print("Ejecutando función eliminar por índice...")
        print("Registro eliminado con éxito")
        print("Función eliminar por índice finalizada")
    except ValueError as e:
        print(f"Error: {e}")

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Agregar registro")
    print("2. Listar de registros")
    print("3. Buscar registro por nombre")
    print("4. Buscar registro por matrícula")
    print("5. Eliminar registro por matrícula")
    print("6. Eliminar registro por índice")
    print("7. Salir")
    
    opcion = input("Ingrese la opción a realizar: ")
    
    if opcion == "1":
        agregar_registro()
    elif opcion == "2":
        listar_registros()
    elif opcion == "3":
        buscar_registro_por_nombre()
    elif opcion == "4":
        buscar_registro_por_matricula()
    elif opcion == "5":
        eliminar_registro_por_matricula()
    elif opcion == "6":
        eliminar_registro_por_indice()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intentalo nuevamente.")