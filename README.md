
El objetivo es crear un programa que simule un sistema de registro e inicio de sesión.

El programa deberá permitir:
Registrar nuevos usuarios.
Guardar nombres de usuario y contraseñas.
Iniciar sesión con una cuenta existente.
Comprobar que los datos introducidos sean correctos.
Mostrar un mensaje de bienvenida al iniciar sesión.
Requisitos adicionales:
Organizar correctamente el código.
Controlar los posibles errores.
Documentar el funcionamiento del programa.
Subir el proyecto a GitHub.
Utilizar commits siguiendo convenciones como feat, fix, docs y chore.
Pista: podéis utilizar listas, diccionarios, funciones y condicionales. En JavaScript podéis utilizar estructuras equivalentes.

Recordad enviar vuestros proyectos y repositorios por este mismo chat.

## Pruebas

El proyecto tiene pruebas automáticas con [pytest](https://docs.pytest.org/) en la carpeta `tests/`. Así no hace falta probar a mano cada cambio: corres las pruebas y te dicen qué funciona y qué no.

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

Las pruebas trabajan en una carpeta temporal, así que no tocan tu `usuarios.txt`. Necesitas Python 3.10 o superior.
