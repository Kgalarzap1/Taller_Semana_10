import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

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

    # ========================================
    # PRODUCTOS
    # ========================================

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        try:
            datos = [
                producto.a_diccionario()
                for producto in productos
            ]

            with open(
                self.ruta_productos,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no tiene permisos para guardar "
                "productos.json."
            )

        except OSError as error:
            print(
                f"Error al guardar productos: {error}"
            )

    def cargar_productos(self) -> list[Producto]:

        try:
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos: list[Producto] = []

            for dato in datos:
                producto = Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["categoria"],
                    dato["precio"],
                    dato["stock"]
                )

                productos.append(producto)

            return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene "
                "un JSON inválido."
            )
            return []

        except KeyError as error:
            print(
                f"Error: falta la clave {error} "
                "en productos.json."
            )
            return []

        except ValueError as error:
            print(
                f"Error al reconstruir un producto: "
                f"{error}"
            )
            return []

        except PermissionError:
            print(
                "Error: no tiene permisos para leer "
                "productos.json."
            )
            return []

        except OSError as error:
            print(
                f"Error al cargar productos: {error}"
            )
            return []

    # ========================================
    # USUARIOS
    # ========================================

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        try:
            datos = [
                usuario.a_diccionario()
                for usuario in usuarios
            ]

            with open(
                self.ruta_usuarios,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no tiene permisos para guardar "
                "usuarios.json."
            )

        except OSError as error:
            print(
                f"Error al guardar usuarios: {error}"
            )

    def cargar_usuarios(self) -> list[Usuario]:

        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios: list[Usuario] = []

            for dato in datos:
                usuario = Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"]
                )

                usuarios.append(usuario)

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json contiene "
                "un JSON inválido."
            )
            return []

        except KeyError as error:
            print(
                f"Error: falta la clave {error} "
                "en usuarios.json."
            )
            return []

        except ValueError as error:
            print(
                f"Error al reconstruir un usuario: "
                f"{error}"
            )
            return []

        except PermissionError:
            print(
                "Error: no tiene permisos para leer "
                "usuarios.json."
            )
            return []

        except OSError as error:
            print(
                f"Error al cargar usuarios: {error}"
            )
            return []

    # ========================================
    # VENTAS
    # ========================================

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:

        try:
            datos = [
                venta.a_diccionario()
                for venta in ventas
            ]

            with open(
                self.ruta_ventas,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no tiene permisos para guardar "
                "ventas.json."
            )

        except OSError as error:
            print(
                f"Error al guardar ventas: {error}"
            )

    def cargar_ventas(self) -> list[Venta]:

        try:
            with open(
                self.ruta_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            ventas: list[Venta] = []

            for dato in datos:
                venta = Venta(
                    dato["usuario_id"],
                    dato["producto_codigo"],
                    dato["cantidad"]
                )

                ventas.append(venta)

            return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: ventas.json contiene "
                "un JSON inválido."
            )
            return []

        except KeyError as error:
            print(
                f"Error: falta la clave {error} "
                "en ventas.json."
            )
            return []

        except ValueError as error:
            print(
                f"Error al reconstruir una venta: "
                f"{error}"
            )
            return []

        except PermissionError:
            print(
                "Error: no tiene permisos para leer "
                "ventas.json."
            )
            return []

        except OSError as error:
            print(
                f"Error al cargar ventas: {error}"
            )
            return []