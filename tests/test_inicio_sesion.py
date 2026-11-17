"""Pruebas de iniciar_sesion()."""

from ayudas import BIENVENIDA, INCORRECTO
from main import iniciar_sesion

VARIOS_USUARIOS = "Lee,124\nSan,412\nana,1234\n"


def test_da_la_bienvenida_con_datos_correctos(usuarios, escribir, capsys):
    usuarios("ana,1234\n")
    escribir("ana", "1234")

    iniciar_sesion()

    assert BIENVENIDA in capsys.readouterr().out


def test_con_varios_usuarios_un_login_correcto_no_dice_incorrecto(usuarios, escribir, capsys):
    usuarios(VARIOS_USUARIOS)
    escribir("San", "412")

    iniciar_sesion()

    salida = capsys.readouterr().out
    assert BIENVENIDA in salida
    assert INCORRECTO not in salida


def test_datos_incorrectos_avisan_una_sola_vez(usuarios, escribir, capsys):
    usuarios(VARIOS_USUARIOS)
    escribir("San", "999")

    iniciar_sesion()

    salida = capsys.readouterr().out
    assert salida.count(INCORRECTO) == 1
    assert BIENVENIDA not in salida


def test_la_contrasena_de_otro_usuario_no_sirve(usuarios, escribir, capsys):
    usuarios(VARIOS_USUARIOS)
    escribir("Lee", "412")  # 412 es la contraseña de San, no la de Lee

    iniciar_sesion()

    assert BIENVENIDA not in capsys.readouterr().out


def test_el_ultimo_usuario_del_archivo_puede_entrar(usuarios, escribir, capsys):
    # Como el usuarios.txt del repositorio: la última línea no termina en salto de línea.
    usuarios("Lee,124\nSan,412")
    escribir("San", "412")

    iniciar_sesion()

    assert BIENVENIDA in capsys.readouterr().out


def test_sin_archivo_de_usuarios_no_se_cae(carpeta, escribir, capsys):
    escribir("ana", "1234")

    iniciar_sesion()  # sin usuarios.txt: no debe lanzar una excepción

    assert BIENVENIDA not in capsys.readouterr().out
