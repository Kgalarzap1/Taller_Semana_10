from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# TUpla: información estable del sistema
OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("       SISTEMA DE RESTAURANTE")
    print("=" * 40)

    for numero, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion}")

    print("=" * 40)


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Error: ya existe un producto con ese código.")

    except ValueError:
        print("Error: el precio debe ser un número.")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto actual: {producto}")

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

        if restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        ):
            print("Producto actualizado correctamente.")

    except ValueError:
        print("Error: el precio debe ser un número.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip()

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    usuario = Usuario(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Error: ya existe un usuario con esa identificación.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- CATEGORÍAS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def main() -> None:

    restaurante = Restaurante()

    # DICCIONARIO:
    # número de opción -> función que debe ejecutarse
    acciones = {
        1: lambda: registrar_producto(restaurante),
        2: lambda: buscar_producto(restaurante),
        3: lambda: actualizar_producto(restaurante),
        4: lambda: eliminar_producto(restaurante),
        5: lambda: listar_productos(restaurante),
        6: lambda: registrar_usuario(restaurante),
        7: lambda: listar_usuarios(restaurante),
        8: lambda: mostrar_categorias(restaurante),
    }

    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 9:
                print("\nGracias por utilizar el sistema.")
                break

            accion = acciones.get(opcion)

            if accion is None:
                print("Opción inválida.")

            else:
                accion()

        except ValueError:
            print("Error: debe ingresar un número.")


if __name__ == "__main__":
    main()