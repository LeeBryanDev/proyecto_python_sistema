"""Pruebas de registrar_nuevos_usuarios()."""

from contextlib import suppress

import pytest

from ayudas import EntradasAgotadas
from main import registrar_nuevos_usuarios


def test_guarda_el_usuario_y_la_contrasena(carpeta, escribir, leer_usuarios):
    escribir("ana", "1234")

    registrar_nuevos_usuarios()

    assert leer_usuarios() == ["ana,1234"]


def test_agrega_al_final_sin_borrar_a_los_demas(usuarios, escribir, leer_usuarios):
    usuarios("Lee,124\n")
    escribir("ana", "1234")

    registrar_nuevos_usuarios()

    assert leer_usuarios() == ["Lee,124", "ana,1234"]


def test_no_pega_el_usuario_nuevo_a_la_ultima_linea(usuarios, escribir, leer_usuarios):
    # Como el usuarios.txt del repositorio: la última línea no termina en salto de línea.
    usuarios("Lee,124\nSan,412")
    escribir("ana", "1234")

    registrar_nuevos_usuarios()

    assert leer_usuarios() == ["Lee,124", "San,412", "ana,1234"]


def test_no_registra_un_usuario_que_ya_existe(usuarios, escribir, leer_usuarios):
    usuarios("ana,1234\n")
    escribir("ana", "otra")

    with suppress(EntradasAgotadas):  # vale rechazarlo y volver a preguntar
        registrar_nuevos_usuarios()

    assert leer_usuarios() == ["ana,1234"]


@pytest.mark.parametrize(
    ("nombre", "contra"),
    [
        pytest.param("", "1234", id="nombre-vacio"),
        pytest.param("   ", "1234", id="nombre-solo-espacios"),
        pytest.param("ana", "", id="contrasena-vacia"),
        pytest.param("ana,lopez", "1234", id="nombre-con-coma"),  # la coma separa nombre y contraseña en el archivo
    ],
)
def test_no_registra_datos_invalidos(carpeta, escribir, leer_usuarios, nombre, contra):
    escribir(nombre, contra)

    with suppress(EntradasAgotadas):  # vale rechazarlo y volver a preguntar
        registrar_nuevos_usuarios()

    assert leer_usuarios() == []
