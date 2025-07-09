import subprocess
import os

def obtener_metadatos(ruta_archivo):
    try:
        resultado = subprocess.run(
            ["exiftool", ruta_archivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if resultado.returncode == 0:
            print("📄 Metadatos encontrados:\n")
            print(resultado.stdout)
        else:
            print("⚠️ Error al obtener metadatos:")
            print(resultado.stderr)
    except FileNotFoundError:
        print("❌ ExifTool no está instalado o no se encuentra en el PATH del sistema.")

def seleccionar_archivo():
    ruta = input("📁 Ingresa la ruta del archivo: ").strip('"')
    if os.path.isfile(ruta):
        obtener_metadatos(ruta)
    else:
        print("❌ Archivo no encontrado.")

if __name__ == "__main__":
    print("🔍 Visualizador de metadatos con ExifTool instalado en el sistema")
    seleccionar_archivo()
    input("\nPresiona ENTER para salir...")