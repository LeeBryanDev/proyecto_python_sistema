"""Pruebas de registrar_nuevos_usuarios()."""

from contextlib import suppress

import pytest

from helpers import InputExhausted
from main import registrar_nuevos_usuarios


def test_saves_the_username_and_password(workdir, typed_input, read_users):
    typed_input("ana", "1234")

    registrar_nuevos_usuarios()

    assert read_users() == ["ana,1234"]


def test_appends_without_removing_existing_users(users_file, typed_input, read_users):
    users_file("Lee,124\n")
    typed_input("ana", "1234")

    registrar_nuevos_usuarios()

    assert read_users() == ["Lee,124", "ana,1234"]


def test_does_not_glue_the_new_user_to_the_last_line(users_file, typed_input, read_users):
    # Como el usuarios.txt del repositorio: la última línea no termina en salto de línea.
    users_file("Lee,124\nSan,412")
    typed_input("ana", "1234")

    registrar_nuevos_usuarios()

    assert read_users() == ["Lee,124", "San,412", "ana,1234"]


def test_rejects_a_username_that_already_exists(users_file, typed_input, read_users):
    users_file("ana,1234\n")
    typed_input("ana", "otra")

    with suppress(InputExhausted):  # vale rechazarlo y volver a preguntar
        registrar_nuevos_usuarios()

    assert read_users() == ["ana,1234"]


@pytest.mark.parametrize(
    ("username", "password"),
    [
        pytest.param("", "1234", id="empty-username"),
        pytest.param("   ", "1234", id="blank-username"),
        pytest.param("ana", "", id="empty-password"),
        pytest.param("ana,lopez", "1234", id="username-with-comma"),  # la coma separa nombre y contraseña en el archivo
    ],
)
def test_rejects_invalid_data(workdir, typed_input, read_users, username, password):
    typed_input(username, password)

    with suppress(InputExhausted):  # vale rechazarlo y volver a preguntar
        registrar_nuevos_usuarios()

    assert read_users() == []
