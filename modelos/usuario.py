class Usuario:

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        if not identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def a_diccionario(self) -> dict[str, str]:
        """Convierte el objeto Usuario en un diccionario."""

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def __str__(self) -> str:

        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )