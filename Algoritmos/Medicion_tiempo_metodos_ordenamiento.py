#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 19:22:37 2025

@author: ssc
"""

# benchmark_ordenamientos.py
import metodos_ordenamiento
import random as rn
from time import perf_counter
import os

# Diccionario: nombre → función del módulo
METODOS = {
    "burbuja": metodos_ordenamiento.burbuja,
    "inserccion": metodos_ordenamiento.insercion,
    "mezcla": metodos_ordenamiento.mezcla,
    "quicksort": metodos_ordenamiento.quikcsort,
    "seleccion": metodos_ordenamiento.seleccion
}

def crear_lista(longitud, limite_valor=200):
    """Genera lista de enteros aleatorios"""
    return [rn.randint(0, limite_valor) for _ in range(longitud)]

def pedir_entero(mensaje, default):
    """Pide un número entero al usuario con valor por defecto"""
    try:
        entrada = input(f"{mensaje} [{default}]: ").strip()
        return int(entrada) if entrada else default
    except ValueError:
        print(f"Entrada inválida, usando {default}")
        return default

if __name__ == "__main__":
    print("== Benchmark de algoritmos de ordenamiento ==")
    print("Métodos disponibles:", ", ".join(METODOS.keys()))

    # pedir método
    metodo_nombre = input("Elige un método: ").strip().lower()
    if metodo_nombre not in METODOS:
        print("Método inválido. Usa uno de:", ", ".join(METODOS.keys()))
        exit(1)

    metodo_funcion = METODOS[metodo_nombre]

    # pedir tamaño máximo de lista
    max_size = pedir_entero("Tamaño máximo de la lista", 5000)
    # pedir paso
    step = pedir_entero("Paso entre pruebas", 1000)
    if step <= 0:
        print("Paso inválido. Se usará 1000 por defecto.")
        step = 1000

    # pedir nombre archivo
    archivo_nombre = input(f"Nombre del archivo CSV [{metodo_nombre}.csv]: ").strip()
    if not archivo_nombre:
        archivo_nombre = f"{metodo_nombre}.csv"

    # generar lista
    print(f"\nGenerando lista base de {max_size} elementos aleatorios...")
    lista = crear_lista(max_size)

    # medir tiempos
    with open(archivo_nombre, "w", newline="") as archivo:
        archivo.write("N;Tiempo\n")
        for n in range(step, max_size + 1, step):
            lista_nueva = lista[:n]  # sublista de tamaño n
            inicio = perf_counter()
            metodo_funcion(lista_nueva)
            tiempo = perf_counter() - inicio
            archivo.write(f"{n};{tiempo:.5f}\n")
            print(f"{metodo_nombre:10s}  N={n:6d}  tiempo={tiempo:.5f} s")

    print(f"\n✅ Resultados guardados en: {os.path.abspath(archivo_nombre)}")
    
"""Llamada dela funcion para graficar rn TK donce comparara diferentes metodos de ordenamineto"""

resp = input("\n¿Quieres graficar resultados ahora? (s/n): ").strip().lower()
if resp == "s":
    import Graficador_datos_vs_tiempo
    Graficador_datos_vs_tiempo.iniciar_graficador()

    