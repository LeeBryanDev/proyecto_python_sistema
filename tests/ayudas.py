"""Constantes y errores que comparten las pruebas.

Si cambias los mensajes del programa, cambia aquí los textos que buscan las pruebas.
"""

BIENVENIDA = "Bienvenido"
INCORRECTO = "incorrecto"  # parte de "El nombre o la contraseña son incorrectos"


class EntradasAgotadas(Exception):
    """El programa pidió más datos con input() de los que la prueba preparó."""
