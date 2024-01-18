=====Script de Copia y Apagado Automático=====

//
Descripción
Este script de Python detecta la inserción de un dispositivo USB, copia archivos específicos de ese dispositivo a la PC y, a continuación, apaga automáticamente la computadora.

Requisitos Previos
Python: Debe estar instalado en su sistema Windows 10. Puede descargarlo de https://www.python.org/downloads/release/python-3121/  
Elige la version segun tu sistema (Windows installer (32 -bit),Windows installer (64-bit),	Windows install(ARM64))


Privilegios de Administrador: Para que el script pueda apagar su sistema, necesita ser ejecutado con privilegios de administrador.

Configuración Inicial
Descargar el Script: Descargue el script shutdown.py a su computadora.

Modificar el Directorio Destino (Opcional): Si desea cambiar el directorio donde se copiarán los archivos, edite la variable destination_directory en el script.


//
Ejecución del Script
Abrir el Símbolo del Sistema con Privilegios de Administrador:

-Busque "cmd" en el menú de inicio, haga clic derecho en "Símbolo del sistema" y seleccione "Ejecutar como administrador".
Navegar hasta el Directorio del Script:

-Utilice el comando cd para cambiar al directorio donde guardó shutdown.py.
Por ejemplo: 'cd C:\Users\TuNombre\Descargas'
Ejecutar el Script:

-Ejecute el script con el comando desde la carpeta raiz: 'python3 shutdown.py'
Siga las instrucciones en pantalla para ingresar la ruta del dispositivo USB/CD.
Finalización:

-Después de copiar los archivos, el script esperará 10 segundos (o el tiempo que haya configurado) y luego apagará la computadora.
Notas Adicionales


//
Seguridad de Datos: Asegúrese de que los archivos que desea copiar no contengan información sensible o confidencial, ya que el script no discrimina el tipo de archivo.
Prueba del Script: Es recomendable probar primero el script en un entorno seguro para asegurarse de que funciona como se espera.


//
Detención de Emergencia: Si necesita detener el apagado después de ejecutar el script, puede cancelarlo ejecutando 'shutdown -a' en una ventana de comando.










                                                                            --Mathias Santos