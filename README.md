# restaurante_app - Semana 10

## Estudiante

Kleber Galarza

## Descripción

Sistema para la administración de productos y usuarios de un restaurante,
desarrollado en Python aplicando programación orientada a objetos,
organización modular y persistencia de datos en formato JSON.

El sistema permite registrar, buscar, actualizar, eliminar y listar
productos. Además, permite registrar y listar usuarios, así como mostrar
las categorías de los productos sin elementos duplicados.

Los productos se guardan de forma persistente en el archivo
`datos/productos.json`, por lo que la información se conserva incluso
después de cerrar y volver a ejecutar el programa.

## Funcionalidades

El sistema permite:

- Registrar productos.
- Buscar productos por código.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorías sin elementos duplicados.
- Guardar productos en un archivo JSON.
- Cargar automáticamente los productos al iniciar el programa.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
│
└── README.md