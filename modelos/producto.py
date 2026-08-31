class Producto:

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:

        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock cuando se realiza una venta válida."""

        if cantidad <= 0:
            raise ValueError(
                "La cantidad a vender debe ser mayor que cero."
            )

        if cantidad > self.stock:
            raise ValueError(
                "No existe suficiente stock para realizar la venta."
            )

        self.stock -= cantidad

    def a_diccionario(self) -> dict[str, str | float | int]:
        """Convierte el objeto Producto en un diccionario."""

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    def __str__(self) -> str:

        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )