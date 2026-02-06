"""Módulos."""

# pylint: disable=invalid-name,redefined-outer-name

import sys
import time

def archivo(archivo_path):
    "Leer Archivo."
    resultados = []
    try:
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                valor = linea.strip()
                if not valor:
                    continue
                try:
                    numero = int(valor)
                    valor_binario = binario(numero)
                    valor_hexadecimal = hexadecimal(numero)
                    linea_resultado = (f"Elemento: {numero}, Valor Binario: {valor_binario}, "
                                       f"Valor Hexadecimal: {valor_hexadecimal}")
                    resultados.append(linea_resultado)
                except ValueError:
                    print(f"Error en linea {numero_linea}: '{valor}'")
                    resultados.append(f"Valor Invalido: {valor}")
    except FileNotFoundError:
        print(f"Archivo {archivo_path} no encontrado.")
        sys.exit(1)

    return resultados


def binario(numero):
    "Convertir los números a formato binario."

    if numero == 0:
        return "0"

    numero_negativo = False
    if numero < 0:
        numero_negativo = True
        numero = abs(numero)

    str_binario = ""
    while numero > 0:
        residuo = numero % 2
        str_binario = str(residuo) + str_binario
        numero = numero // 2

    if numero_negativo:
        str_binario = "-" + str_binario

    return str_binario


def hexadecimal(numero):
    "Convertir los números a formato hexadecimal."

    if numero == 0:
        return "0"

    numero_negativo = False
    if numero < 0:
        numero_negativo = True
        numero = abs(numero)

    mapeo_hexadecimal = "0123456789ABCDEF"
    str_hexadecimal = ""

    while numero > 0:
        residuo = numero % 16
        char_hexadecimal = mapeo_hexadecimal[residuo]
        str_hexadecimal = char_hexadecimal + str_hexadecimal
        numero = numero // 16

    if numero_negativo:
        str_hexadecimal = "-" + str_hexadecimal

    return str_hexadecimal


inicio = time.time()

# Validar argumentos de entrada
if len(sys.argv) != 2:
    print("Uso incorrecto de ejecución: debe ser 'python convertNumbers.py P2/TC.txt'")
    sys.exit(1)

archivo_path = sys.argv[1]

resultados = archivo(archivo_path)

# Calcular Tiempo Transcurrido
final = time.time()
tiempo_transcurrido = final - inicio

tiempo_mensaje = f"\nTiempo Transcurrido: {tiempo_transcurrido:.5f} segundos."
resultados.append(tiempo_mensaje)
print(tiempo_mensaje)

# Guardar en Archivo
try:
    with open("ConvertionResults.txt", "w", encoding='utf-8') as archivo_resultados:
        for linea in resultados:
            archivo_resultados.write(linea + "\n")
    print("\nResultados guardados en ConvertionResults.txt")
except IOError as e:
    print(f"Error al escribir los resultados en el archivo: {e}")
