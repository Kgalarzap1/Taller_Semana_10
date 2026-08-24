import json

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(
        self,
        ruta_archivo: str
    ) -> None:

        self.ruta_archivo = ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        """Carga los productos desde el archivo JSON."""

        try:

            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                productos: list[Producto] = []

                for registro in datos:

                    try:

                        producto = Producto(
                            codigo=registro["codigo"],
                            nombre=registro["nombre"],
                            categoria=registro["categoria"],
                            precio=float(
                                registro["precio"]
                            )
                        )

                        productos.append(producto)

                    except KeyError:

                        print(
                            "Advertencia: se encontró un "
                            "producto con datos incompletos."
                        )

                    except ValueError as error:

                        print(
                            "Advertencia: se encontró un "
                            f"producto con datos inválidos: {error}"
                        )

                return productos

        except FileNotFoundError:

            print(
                "No existe el archivo de productos. "
                "Se iniciará con una lista vacía."
            )

            return []

        except json.JSONDecodeError:

            print(
                "Error: el archivo JSON tiene un "
                "formato inválido."
            )

            return []

        except PermissionError:

            print(
                "Error: no existen permisos para "
                "leer el archivo de productos."
            )

            return []

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:
        """Guarda los productos en el archivo JSON."""

        try:

            datos = []

            for producto in productos:

                datos.append(
                    producto.a_diccionario()
                )

            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:

            print(
                "Error: no existen permisos para "
                "guardar el archivo de productos."
            )

            return False