"""Módulos."""

# pylint: disable=invalid-name,redefined-outer-name,no-else-return

import sys
import time

def leer_archivo(archivo_path):
    "Leer Archivo."
    datos = []
    try:
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                valor = linea.strip()
                if not valor:
                    continue
                try:
                    numero = float(valor)
                    datos.append(numero)
                except ValueError:
                    print(f"Error en linea {numero_linea}: '{valor}'")
    except FileNotFoundError:
        print(f"Archivo {archivo_path} no encontrado.")
        sys.exit(1)

    return datos


def calcular_media(datos):
    """Calcular Promedio."""
    if not datos:
        return 0.0

    return sum(datos)/len(datos)


def calcular_mediana(datos):
    """Calcular Mediana."""
    if not datos:
        return 0.0

    datos_ordenados = sorted(datos)
    cantidad_elementos = len(datos_ordenados)
    mediana = cantidad_elementos // 2

    if cantidad_elementos % 2 == 1:
        return datos_ordenados[mediana]
    else:
        return (datos_ordenados[mediana - 1] + datos_ordenados[mediana]) / 2.0


def calcular_moda(datos):
    """Calcular Moda."""
    if not datos:
        return 0.0

    frecuencia = {}
    for numero in datos:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1

    max_count = 0
    moda = datos[0]

    for key, count in frecuencia.items():
        if count > max_count:
            max_count = count
            moda = key

    return moda


def calcular_varianza(datos, media):
    """Calcular Varianza."""
    if len(datos) < 2:
        return 0.0

    suma_diff_cuadrados = 0.0
    for numero in datos:
        suma_diff_cuadrados += (numero - media) ** 2

    return suma_diff_cuadrados / len(datos)


def calcular_desviacion_estandar(varianza):
    """Calcular Desviación Estandar."""
    return varianza ** 0.5


inicio = time.time()

# Validar argumentos de entrada
if len(sys.argv) != 2:
    print("Uso incorrecto de ejecución: debe ser 'python computeStatistics.py P1/TC.txt'")
    sys.exit(1)

archivo_path = sys.argv[1]

# Lectura de Datos
datos = leer_archivo(archivo_path)

if not datos:
    print("No hay datos válidos para procesar.")
    sys.exit(1)

CONTEO = len(datos)

# Realizar Cálculos
media = calcular_media(datos)
mediana = calcular_mediana(datos)
moda = calcular_moda(datos)
varianza = calcular_varianza(datos, media)
desviacion_estandar = calcular_desviacion_estandar(varianza)

# Calcular Tiempo Transcurrido
final = time.time()
tiempo_transcurrido = final - inicio

# Imprimir Valores
print(f"\nMedia: {media:.5f}\n")
print(f"Mediana: {mediana:.5f}\n")
print(f"Moda: {moda:.5f}\n")
print(f"Varianza: {varianza:.5f}\n")
print(f"Desviación Estandar: {desviacion_estandar:.5f}\n")

print(f"Tiempo Transcurrido: {tiempo_transcurrido:.5f} segundos.'\n")

# Formateo Resultados
resultados = []
resultados.append(f"Cantidad de Numeros: {CONTEO}")
resultados.append(f"Media: {media:.5f}")
resultados.append(f"Mediana: {mediana:.5f}")
resultados.append(f"Moda: {moda:.5f}")
resultados.append(f"Varianza: {varianza:.5f}")
resultados.append(f"Desviación Estandar: {desviacion_estandar:.5f}")

resultados.append(f"Tiempo Transcurrido: {tiempo_transcurrido:.5f} segundos.")

SALIDA_DATOS = "\n".join(resultados)

# Guardar en Archivo
try:
    with open("StatisticsResults.txt", "w", encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(SALIDA_DATOS)
    print("\nResultados guardados en StatisticsResults.txt")
except IOError as e:
    print(f"Error al escribir los resultados en el archivo: {e}")
