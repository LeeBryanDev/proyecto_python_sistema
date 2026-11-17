"""Fixtures compartidas por todas las pruebas (pytest carga este archivo solo, sin import).

Cada prueba trabaja en una carpeta temporal: tu usuarios.txt real nunca se toca.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

from helpers import InputExhausted

PROJECT_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = "usuarios.txt"


@pytest.fixture
def workdir(tmp_path, monkeypatch):
    """Una carpeta temporal y vacía, que pasa a ser la carpeta actual de la prueba."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def users_file(workdir):
    """users_file("Lee,124\\nSan,412\\n") crea usuarios.txt con ese contenido exacto."""

    def write(content: str) -> None:
        (workdir / USERS_FILE).write_text(content, encoding="utf-8", newline="")

    return write


@pytest.fixture
def read_users(workdir):
    """Devuelve las líneas de usuarios.txt (lista vacía si el archivo no existe)."""

    def read() -> list[str]:
        path = workdir / USERS_FILE
        return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

    return read


@pytest.fixture
def typed_input(monkeypatch):
    """typed_input("ana", "1234") hace que cada input() devuelva esos textos, en orden.

    Si el programa pide más datos de los preparados, lanza InputExhausted
    (por ejemplo, cuando vuelve a preguntar después de rechazar un dato).
    """

    def prepare(*answers: str) -> None:
        pending = iter(answers)

        def fake_input(prompt: str = "") -> str:
            try:
                return next(pending)
            except StopIteration:
                raise InputExhausted(f"input() pidió otro dato: {prompt!r}") from None

        monkeypatch.setattr("builtins.input", fake_input)

    return prepare


@pytest.fixture
def run_app(workdir):
    """Corre `python main.py` como lo haría una persona y le escribe `keyboard` en la consola."""

    def run(keyboard: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(PROJECT_DIR / "main.py")],
            input=keyboard,
            cwd=workdir,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )

    return run
