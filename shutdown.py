import os
import shutil
import time

# Directorio destino donde se copiarán los archivos
destination_directory = "C:/User/destination_folder/"

# Función para copiar archivos desde un dispositivo de almacenamiento externo a la PC
def copy_files(source):
    # Verificar si el directorio fuente existe
    if not os.path.exists(source):
        print(f"No se encontró el dispositivo en {source}. Por favor, verifique la ruta y vuelva a intentarlo.")
        return False

    # Crear el directorio destino si no existe
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Intentar copiar archivos
    try:
        for filename in os.listdir(source):
            file_path = os.path.join(source, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, destination_directory)
        return True
    except Exception as e:
        print(f"Ocurrió un error al copiar los archivos: {e}")
        return False

# Función para apagar el sistema
def shutdown_system(delay_seconds=10):
    print(f"Apagando el sistema en {delay_seconds} segundos...")
    time.sleep(delay_seconds)
    os.system("shutdown /s /t 1")

# Función principal
def main():
    print("Esperando la conexión de un dispositivo USB o CD...")
    source = input("Ingrese la ruta del dispositivo USB/CD conectado: ")

    if copy_files(source):
        print(f"Archivos copiados con éxito desde {source} a {destination_directory}")
        # Apagar el sistema después de la copia
        shutdown_system(10)  # Ajusta este valor
    else:
        print("La copia de archivos no se completó con éxito.")

# Ejecutando la función principal
if __name__ == "__main__":
    main()
