"""Módulos."""

# pylint: disable=invalid-name,redefined-outer-name

import sys
import time

def archivo(archivo_path):
    "Leer Archivo."

    frecuencia = {}

    try:
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            for _, linea in enumerate(archivo, start=1):
                linea = linea.strip()

                if not linea:
                    continue

                palabras = linea.split()

                for palabra in palabras:
                    palabra_minusculas = palabra.lower()

                    if palabra_minusculas in frecuencia:
                        frecuencia[palabra_minusculas] += 1
                    else:
                        frecuencia[palabra_minusculas] = 1
    except FileNotFoundError:
        print(f"Archivo {archivo_path} no encontrado.")
        sys.exit(1)

    return frecuencia


inicio = time.time()

# Validar argumentos de entrada
if len(sys.argv) != 2:
    print("Uso incorrecto de ejecución: debe ser 'python convertNumbers.py P2/TC.txt'")
    sys.exit(1)

archivo_path = sys.argv[1]

# Procesar Archivo
diccionario_resultados = archivo(archivo_path)

# Lista Resultados
resultados = []

if diccionario_resultados:
    palabras_ordenadas = sorted(diccionario_resultados.keys())

    for palabra in palabras_ordenadas:
        conteo = diccionario_resultados[palabra]
        linea = f"{palabra}: {conteo}"
        resultados.append(linea)
else:
    resultados.append("Datos No Validos.")

# Calcular Tiempo Transcurrido
final = time.time()
tiempo_transcurrido = final - inicio

tiempo_mensaje = f"\nTiempo Transcurrido: {tiempo_transcurrido:.5f} segundos."
resultados.append(tiempo_mensaje)

# Imprimir Resultados
SALIDA_DATOS = "\n".join(resultados)
print(SALIDA_DATOS)

# Guardar en Archivo
try:
    with open("WordCountResults.txt", "w", encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(SALIDA_DATOS)
    print("\nResultados guardados en WordCountResults.txt")
except IOError as e:
    print(f"Error al escribir los resultados en el archivo: {e}")
