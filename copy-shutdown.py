import os
import shutil
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Directorio destino donde se copiarán los archivos
destination_directory = "C:/User/destination_folder/"

def gui_app():
    root = tk.Tk()
    root.title("Copy and Auto Shutdown")

    # Área de texto para mostrar mensajes al usuario
    text_widget = tk.Text(root, height=15, width=50)
    text_widget.pack(pady=10)

    # Función para copiar archivos con GUI
    def copy_files_gui():
        source = filedialog.askdirectory(title="Seleccione la unidad de almacenamiento")
        if not source:
            text_widget.insert(tk.END, "No se seleccionó ninguna unidad de almacenamiento.\n")
            return

        global destination_directory
        destination_directory = filedialog.askdirectory(title="Seleccione la carpeta de destino")
        if not destination_directory:
            text_widget.insert(tk.END, "No se seleccionó ninguna carpeta de destino.\n")
            return

        try:
            file_list = os.listdir(source)
            text_widget.insert(tk.END, "Listado de archivos en el dispositivo:\n")
            for filename in file_list:
                text_widget.insert(tk.END, f"{filename}\n")

            user_choice = messagebox.askyesno("Confirmación", "¿Desea copiar estos archivos?")
            if not user_choice:
                text_widget.insert(tk.END, "Operación cancelada por el usuario.\n")
                return

            text_widget.insert(tk.END, "Copiando archivos:\n")
            for filename in file_list:
                file_path = os.path.join(source, filename)
                if os.path.isfile(file_path):
                    shutil.copy(file_path, destination_directory)
                    text_widget.insert(tk.END, f"Copiando: {filename}\n")

            text_widget.insert(tk.END, "Archivos copiados con éxito. Apagando la PC en 10 segundos...\n")
            root.after(10000, shutdown_system)  # Llamada a la función shutdown_system después de 10 segundos
        except Exception as e:
            text_widget.insert(tk.END, f"Ocurrió un error al copiar los archivos: {e}\n")

    def shutdown_system():
        try:
            text_widget.insert(tk.END, "Apagando la PC...\n")
            # Puedes agregar aquí la lógica para apagar la PC en lugar del mensaje
            os.system("shutdown /s /t 1")
        except Exception as e:
            text_widget.insert(tk.END, f"Ocurrió un error al apagar la PC: {e}\n")

    ttk.Button(root, text="Seleccionar Unidad y Carpeta para Copiar Archivos", command=copy_files_gui).pack(pady=10)

    # Función para cerrar la aplicación
    def close_app():
        if messagebox.askokcancel("Cerrar", "¿Está seguro de que desea cerrar el programa?"):
            root.destroy()

    ttk.Button(root, text="Cerrar", command=close_app).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    gui_app()
