import os
import shutil
import time

# Directorio destino donde se copiarán los archivos
destination_directory = "C:/User/destination_folder/"

# Función para copiar archivos desde un dispositivo USB/CD a la PC
def copy_files(source):
    # Crear el directorio destino si no existe
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Copiar archivos
    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination_directory)

# Función para apagar el sistema
def shutdown_system(delay_seconds=10):
    print(f"Apagando el sistema en {delay_seconds} segundos...")
    time.sleep(delay_seconds)
    os.system("shutdown /s /t 1")

# Función principal
def main():
    print("Esperando la conexión de un dispositivo USB o CD...")
    # Simulación de la inserción del dispositivo
    source = input("Ingrese la ruta del dispositivo USB/CD conectado: ")

    print(f"Copiando archivos desde {source} a {destination_directory}")
    copy_files(source)

    # Apagar el sistema después de la copia
    shutdown_system(10)  # Ajusta este valor según lo prefieras

# Ejecutando la función principal
if __name__ == "__main__":
    main()
