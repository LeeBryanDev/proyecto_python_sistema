"""Pruebas del programa completo: se corre main.py y se le escribe en la consola, como una persona."""

from helpers import MENU_TITLE, WELCOME_TEXT


def test_option_3_exits_the_program(run_app):
    result = run_app("3\n")

    assert result.returncode == 0
    assert "Saliendo" in result.stdout


def test_register_and_then_log_in(run_app):
    result = run_app("1\nana\n1234\n2\nana\n1234\n3\n")

    assert result.returncode == 0
    assert WELCOME_TEXT in result.stdout


def test_an_unknown_option_shows_the_menu_again(run_app):
    result = run_app("7\n3\n")

    assert result.returncode == 0
    assert result.stdout.count(MENU_TITLE) == 2


def test_a_letter_in_the_menu_does_not_crash(run_app):
    result = run_app("a\n3\n")

    assert "Traceback" not in result.stderr
    assert result.returncode == 0
    assert result.stdout.count(MENU_TITLE) == 2


def test_logging_in_with_no_registered_users_does_not_crash(run_app):
    result = run_app("2\nana\n1234\n3\n")

    assert "Traceback" not in result.stderr
    assert result.returncode == 0
