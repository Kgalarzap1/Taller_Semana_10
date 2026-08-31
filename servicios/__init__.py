def __init__(self) -> None:

    carpeta_proyecto = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    self.carpeta_datos = os.path.join(
        carpeta_proyecto,
        "datos"
    )

    self.ruta_productos = os.path.join(
        self.carpeta_datos,
        "productos.json"
    )

    self.ruta_usuarios = os.path.join(
        self.carpeta_datos,
        "usuarios.json"
    )

    self.ruta_ventas = os.path.join(
        self.carpeta_datos,
        "ventas.json"
    )

    os.makedirs(
        self.carpeta_datos,
        exist_ok=True
    )