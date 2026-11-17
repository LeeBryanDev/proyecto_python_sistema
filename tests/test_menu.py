"""Pruebas del programa completo: se corre main.py y se le escribe en la consola, como una persona."""

from ayudas import BIENVENIDA


def test_la_opcion_3_cierra_el_programa(ejecutar):
    resultado = ejecutar("3\n")

    assert resultado.returncode == 0
    assert "Saliendo" in resultado.stdout


def test_registrarse_y_luego_iniciar_sesion(ejecutar):
    resultado = ejecutar("1\nana\n1234\n2\nana\n1234\n3\n")

    assert resultado.returncode == 0
    assert BIENVENIDA in resultado.stdout


def test_una_opcion_que_no_existe_vuelve_al_menu(ejecutar):
    resultado = ejecutar("7\n3\n")

    assert resultado.returncode == 0
    assert resultado.stdout.count("Menu") == 2


def test_una_letra_en_el_menu_no_cierra_el_programa(ejecutar):
    resultado = ejecutar("a\n3\n")

    assert "Traceback" not in resultado.stderr
    assert resultado.returncode == 0
    assert resultado.stdout.count("Menu") == 2


def test_iniciar_sesion_sin_usuarios_registrados_no_cierra_el_programa(ejecutar):
    resultado = ejecutar("2\nana\n1234\n3\n")

    assert "Traceback" not in resultado.stderr
    assert resultado.returncode == 0
