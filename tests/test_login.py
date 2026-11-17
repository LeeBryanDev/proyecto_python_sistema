"""Pruebas de iniciar_sesion()."""

from helpers import WELCOME_TEXT, WRONG_LOGIN_TEXT
from main import iniciar_sesion

SEVERAL_USERS = "Lee,124\nSan,412\nana,1234\n"


def test_welcomes_a_user_with_the_right_credentials(users_file, typed_input, capsys):
    users_file("ana,1234\n")
    typed_input("ana", "1234")

    iniciar_sesion()

    assert WELCOME_TEXT in capsys.readouterr().out


def test_a_right_login_with_several_users_does_not_say_wrong(users_file, typed_input, capsys):
    users_file(SEVERAL_USERS)
    typed_input("San", "412")

    iniciar_sesion()

    output = capsys.readouterr().out
    assert WELCOME_TEXT in output
    assert WRONG_LOGIN_TEXT not in output


def test_wrong_credentials_are_reported_only_once(users_file, typed_input, capsys):
    users_file(SEVERAL_USERS)
    typed_input("San", "999")

    iniciar_sesion()

    output = capsys.readouterr().out
    assert output.count(WRONG_LOGIN_TEXT) == 1
    assert WELCOME_TEXT not in output


def test_another_users_password_does_not_work(users_file, typed_input, capsys):
    users_file(SEVERAL_USERS)
    typed_input("Lee", "412")  # 412 es la contraseña de San, no la de Lee

    iniciar_sesion()

    assert WELCOME_TEXT not in capsys.readouterr().out


def test_the_last_user_in_the_file_can_log_in(users_file, typed_input, capsys):
    # Como el usuarios.txt del repositorio: la última línea no termina en salto de línea.
    users_file("Lee,124\nSan,412")
    typed_input("San", "412")

    iniciar_sesion()

    assert WELCOME_TEXT in capsys.readouterr().out


def test_a_missing_users_file_does_not_crash(workdir, typed_input, capsys):
    typed_input("ana", "1234")

    iniciar_sesion()  # sin usuarios.txt: no debe lanzar una excepción

    assert WELCOME_TEXT not in capsys.readouterr().out
