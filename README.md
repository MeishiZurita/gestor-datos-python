# Gestor de Datos en Python

Este programa permite gestionar registros con información de *nombre, edad, fecha y matrícula*.  
Cuenta con funciones para *agregar, listar, buscar y eliminar registros* mediante un *menú interactivo*.

## Instrucciones para ejecutar el programa

### 1. Requisitos
- Tener *Python 3* instalado en tu computadora.  
- Tener el archivo gestor-datos-python.py en la carpeta del proyecto.  

Puedes verificar que Python está instalado ejecutando:

```bash
python --version
```

### 2. Abrir la terminal

Windows: presiona Windows + R, escribe cmd y presiona Enter.

Linux/Mac: abre la terminal de tu sistema.

Opcional: también puedes usar un editor como VS Code y abrir la terminal integrada.


### 3. Navegar a la carpeta del proyecto

Usa el comando cd para entrar a la carpeta donde guardaste gestor.py.
Ejemplo:
cd C:\Users\TuUsuario\Documentos\gestor-datos-python
o en Linux/Mac:
cd ~/Documentos/gestor-datos-Python


### 4. Ejecutar el programa
python gestor.py
Se abrirá un menú interactivo con opciones numeradas


### 5. Uso del menú
Menú de opciones:
1. Agregar registro
2. Listar registros
3. Buscar registro por nombre
4. Buscar registro por matrícula
5. Eliminar registro por matrícula
6. Eliminar registro por índice
7. Salir

Escribe el número de la opción que quieres realizar y presiona Enter.

Ejemplos:

Para agregar un registro, escribe 1 y sigue las instrucciones.

Para buscar un registro por nombre, escribe 3 y proporciona el nombre.

Para eliminar un registro por matrícula, escribe 5 y proporciona la matrícula.

Para salir, selecciona la opción 7.


### 6. Funcionalidades

Agregar registros con nombre, edad, fecha y matrícula.

Listar todos los registros guardados.

Buscar registros por nombre o matrícula.

Eliminar registros por matrícula o índice.

Manejo de errores:

Edad inválida.

Registro no encontrado.


### 7. Notas importantes

Los cambios se realizan en memoria, es decir, si cierras el programa, los registros se perderán.

Se recomienda seguir estrictamente el formato de fecha: año-mes-día (ejemplo: 2025-09-18).

Mensajes de error guiarán al usuario en caso de ingreso inválido o registro inexistente.