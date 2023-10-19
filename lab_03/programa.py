import sys

# Función para aplicar las transformaciones a una línea
def transform_line(line):
    if line and line[0].isalpha():
        return line[0].upper() + line[1:] + "0"
    elif line and line[0].isdigit():
        return ""
    else:
        return line

# Verificar si se proporcionó el nombre del archivo en la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python programa.py nombre_del_archivo")
    sys.exit(1)

# Obtener el nombre del archivo de la línea de comandos
nombre_archivo = sys.argv[1]

# Nombre del archivo de salida
nombre_archivo_salida = "rockyou_mod.dic"

lineas_procesadas = 0  # Contador de líneas procesadas

try:
    with open(nombre_archivo, "r", encoding="ISO-8859-1") as archivo_entrada, open(nombre_archivo_salida, "w") as archivo_salida:

        for linea in archivo_entrada:
            linea_transformada = transform_line(linea.strip())  # Eliminar espacios en blanco alrededor
            if linea_transformada:
                archivo_salida.write(linea_transformada + "\n")
                lineas_procesadas += 1
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")

print(f"Transformación completada. Resultado guardado en 'rockyou_mod.dic'.")
print(f"Líneas procesadas: {lineas_procesadas}")
