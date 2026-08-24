from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self) -> None:

        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    # ==========================
    # PRODUCTOS
    # ==========================

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:
        """Busca un producto por su código."""

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """Actualiza los datos de un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto_actualizado = Producto(
            codigo=producto.codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )

        producto.nombre = producto_actualizado.nombre
        producto.categoria = producto_actualizado.categoria
        producto.precio = producto_actualizado.precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su código."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)

        return True

    def listar_productos(self) -> list[Producto]:
        """Devuelve la lista de productos."""

        return self.productos

    def cargar_productos(
        self,
        productos: list[Producto]
    ) -> None:
        """Carga una lista de productos en el restaurante."""

        self.productos = productos

    # ==========================
    # USUARIOS
    # ==========================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""

        for usuario_registrado in self.usuarios:

            if (
                usuario_registrado.identificacion
                == usuario.identificacion
            ):
                return False

        self.usuarios.append(usuario)

        return True

    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""

        return self.usuarios

    # ==========================
    # CATEGORÍAS
    # ==========================

    def obtener_categorias(self) -> set[str]:
        """Obtiene las categorías sin elementos duplicados."""

        categorias: set[str] = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias