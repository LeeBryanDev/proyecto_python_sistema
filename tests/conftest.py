"""Ayudas compartidas por todas las pruebas (pytest las carga solo, sin import).

Cada prueba trabaja en una carpeta temporal: tu usuarios.txt real nunca se toca.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

from ayudas import EntradasAgotadas

PROYECTO = Path(__file__).resolve().parent.parent


@pytest.fixture
def carpeta(tmp_path, monkeypatch):
    """Una carpeta temporal y vacía, que pasa a ser la carpeta actual de la prueba."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def usuarios(carpeta):
    """usuarios("Lee,124\\nSan,412\\n") crea usuarios.txt con ese contenido exacto."""

    def crear(contenido: str) -> None:
        (carpeta / "usuarios.txt").write_text(contenido, encoding="utf-8", newline="")

    return crear


@pytest.fixture
def leer_usuarios(carpeta):
    """Devuelve las líneas de usuarios.txt (lista vacía si el archivo no existe)."""

    def leer() -> list[str]:
        archivo = carpeta / "usuarios.txt"
        return archivo.read_text(encoding="utf-8").splitlines() if archivo.exists() else []

    return leer


@pytest.fixture
def escribir(monkeypatch):
    """escribir("ana", "1234") hace que cada input() devuelva esos textos, en orden.

    Si el programa pide más datos de los preparados, lanza EntradasAgotadas
    (por ejemplo, cuando vuelve a preguntar después de rechazar un dato).
    """

    def preparar(*textos: str) -> None:
        pendientes = iter(textos)

        def input_falso(mensaje: str = "") -> str:
            try:
                return next(pendientes)
            except StopIteration:
                raise EntradasAgotadas(f"input() pidió otro dato: {mensaje!r}") from None

        monkeypatch.setattr("builtins.input", input_falso)

    return preparar


@pytest.fixture
def ejecutar(carpeta):
    """Corre `python main.py` como lo haría una persona y le escribe `teclado` en la consola."""

    def correr(teclado: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(PROYECTO / "main.py")],
            input=teclado,
            cwd=carpeta,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )

    return correr
