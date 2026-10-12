"""
Escribe un programa que use los módulos platform y os para,
 Mostrar el procesador donde se ejecuta el programa.
 Mostrar el sistema operativo y versión donde se ejecuta el programa.
 Mostrar el nombre el host donde se ejecuta el programa.
 Mostrar el directorio actual.
"""

from platform import processor, system, version, node

from os import getcwd

procesador = processor()
print(f"Procesador: {procesador}")
sistemaOperativo = system()
print(f"Sistema Operativo: {sistemaOperativo}")
vers = version()
print(f"Version: {vers}")
nombre = node()
print(f"Host: {nombre}")

dirActual = getcwd()
print(f"Directorio actual: {dirActual}")