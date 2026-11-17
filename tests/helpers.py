"""Constantes y errores que comparten las pruebas.

Si cambias los mensajes del programa, cambia aquí los textos que buscan las pruebas.
"""

WELCOME_TEXT = "Bienvenido"
WRONG_LOGIN_TEXT = "incorrecto"  # parte de "El nombre o la contraseña son incorrectos"
MENU_TITLE = "Menu"  # parte de "========== Menu =========="


class InputExhausted(Exception):
    """El programa pidió más datos con input() de los que la prueba preparó."""
