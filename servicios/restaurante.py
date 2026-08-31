from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self) -> None:

        self.archivo_servicio = ArchivoServicio()

        self._productos: list[Producto] = (
            self.archivo_servicio.cargar_productos()
        )

        self._usuarios: list[Usuario] = (
            self.archivo_servicio.cargar_usuarios()
        )

        self._ventas: list[Venta] = (
            self.archivo_servicio.cargar_ventas()
        )

    # ========================================
    # PRODUCTOS
    # ========================================

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not categoria.strip():
            raise ValueError(
                "La categoría no puede estar vacía."
            )

        if precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        producto.nombre = nombre.strip()
        producto.categoria = categoria.strip()
        producto.precio = precio
        producto.stock = stock

        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return True

    def listar_productos(self) -> list[Producto]:

        return self._productos

    # ========================================
    # USUARIOS
    # ========================================

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> bool:

        if self.buscar_usuario(identificacion) is not None:
            return False

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        self._usuarios.append(usuario)

        self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:

        return self._usuarios

    # ========================================
    # VENTAS
    # ========================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        self.archivo_servicio.guardar_ventas(
            self._ventas
        )

        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:

            if venta.usuario_id == identificacion_usuario:

                ventas_usuario.append(venta)

        return ventas_usuario