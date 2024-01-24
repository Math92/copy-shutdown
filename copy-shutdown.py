import os
import shutil
import time

# Directorio destino donde se copiarán los archivos
destination_directory = "C:/User/destination_folder/"

# Función para mostrar las unidades de almacenamiento disponibles
def list_available_drives():
    drives = [f"{chr(65 + drive)}:" for drive in range(26) if os.path.exists(f"{chr(65 + drive)}:")]
    if not drives:
        print("No se encontraron unidades de almacenamiento disponibles.")
    else:
        print("Unidades de almacenamiento disponibles:")
        for i, drive in enumerate(drives, start=1):
            print(f"{i}. {drive}")
    return drives

# Función para obtener la opción del usuario
def get_user_choice(options):
    while True:
        try:
            choice = int(input("Seleccione una opción: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para copiar archivos desde un dispositivo de almacenamiento externo a la PC
def copy_files(source):
    # Verificar si el directorio fuente existe
    if not os.path.exists(source):
        print(f"No se encontró el dispositivo en {source}. Por favor, verifique la ruta y vuelva a intentarlo.")
        return False

    # Crear el directorio destino si no existe
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Obtener la lista de archivos en el directorio fuente
    file_list = os.listdir(source)

    # Mostrar el listado de archivos
    print("Listado de archivos en el dispositivo:")
    for filename in file_list:
        print(filename)

    # Preguntar al usuario si desea continuar con la copia
    user_choice = input("¿Desea copiar estos archivos? (Sí/No): ").lower()
    if user_choice != 'si':
        print("Operación cancelada por el usuario.")
        return False

    # Copiar archivos y mostrar el listado mientras se copian
    print("Copiando archivos:")
    try:
        for filename in file_list:
            file_path = os.path.join(source, filename)
            if os.path.isfile(file_path):
                print(f"Copiando: {filename}")
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
    exit()  # Añadido para asegurarse de que el script finalice después de iniciar el apagado

# Función principal
def main():
    print("Esperando la conexión de un dispositivo USB o CD...")
    
    # Mostrar opciones de unidades de almacenamiento
    available_drives = list_available_drives()
    if not available_drives:
        return
    
    # Permitir al usuario elegir una unidad de almacenamiento
    source_drive = get_user_choice(available_drives)
    source = f"{source_drive}/"

    # Permitir al usuario elegir la carpeta de destino
    global destination_directory
    destination_directory = input("Ingrese la carpeta de destino para guardar los archivos: ")

    if copy_files(source):
        print(f"Archivos copiados con éxito desde {source} a {destination_directory}")
        # Apagar el sistema después de la copia
        shutdown_system(10)  # Ajusta este valor
    else:
        print("La copia de archivos no se completó con éxito.")

# Ejecutando la función principal
if __name__ == "__main__":
    main()
