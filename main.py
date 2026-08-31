from servicios.restaurante import Restaurante


def mostrar_menu() -> None:

    print("\n" + "=" * 50)
    print("       SISTEMA DE GESTIÓN DEL RESTAURANTE")
    print("=" * 50)

    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Mostrar categorías")
    print("9. Realizar venta")
    print("10. Consultar ventas de un usuario")
    print("11. Salir")


def registrar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- REGISTRAR PRODUCTO ---")

    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock disponible: "))

        registrado = restaurante.registrar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if registrado:
            print("Producto registrado correctamente.")
        else:
            print(
                "No se pudo registrar el producto. "
                "El código ya existe."
            )

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- ACTUALIZAR PRODUCTO ---")

    try:
        codigo = input("Código del producto a actualizar: ")

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return

        print("\nIngrese los nuevos datos:")

        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock disponible: "))

        actualizado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("No se pudo actualizar el producto.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Código del producto a eliminar: ")

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(
    restaurante: Restaurante
) -> None:

    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(
    restaurante: Restaurante
) -> None:

    print("\n--- REGISTRAR USUARIO ---")

    try:
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        registrado = restaurante.registrar_usuario(
            identificacion,
            nombre,
            correo
        )

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print(
                "No se pudo registrar el usuario. "
                "La identificación ya existe."
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(
    restaurante: Restaurante
) -> None:

    print("\n--- CATEGORÍAS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    categorias: set[str] = set()

    for producto in productos:
        categorias.add(producto.categoria)

    for categoria in categorias:
        print(f"- {categoria}")


def realizar_venta(
    restaurante: Restaurante
) -> None:

    print("\n--- REALIZAR VENTA ---")

    try:
        identificacion_usuario = input(
            "Identificación del usuario: "
        )

        codigo_producto = input(
            "Código del producto: "
        )

        cantidad = int(
            input("Cantidad a vender: ")
        )

        usuario = restaurante.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            print("Error: el usuario no existe.")
            return

        producto = restaurante.buscar_producto(
            codigo_producto
        )

        if producto is None:
            print("Error: el producto no existe.")
            return

        if cantidad <= 0:
            print(
                "Error: la cantidad debe ser "
                "mayor que cero."
            )
            return

        if producto.stock < cantidad:
            print(
                f"Error: stock insuficiente. "
                f"Stock disponible: {producto.stock}"
            )
            return

        venta_realizada = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )

        if venta_realizada:
            print("\nVenta realizada correctamente.")
            print(
                f"Stock restante de "
                f"{producto.nombre}: "
                f"{producto.stock}"
            )
        else:
            print("No se pudo realizar la venta.")

    except ValueError:
        print(
            "Error: la cantidad debe ser "
            "un número entero válido."
        )


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    print("\n--- CONSULTAR VENTAS DE USUARIO ---")

    identificacion_usuario = input(
        "Identificación del usuario: "
    )

    usuario = restaurante.buscar_usuario(
        identificacion_usuario
    )

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion_usuario
    )

    if not ventas:
        print(
            f"El usuario {usuario.nombre} "
            "no tiene ventas registradas."
        )
        return

    print(
        f"\nVentas realizadas por: "
        f"{usuario.nombre}"
    )

    for venta in ventas:

        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            nombre_producto = producto.nombre
        else:
            nombre_producto = "Producto no disponible"

        print(
            f"Producto: {venta.producto_codigo} - "
            f"{nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )


def main() -> None:

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            buscar_producto(restaurante)

        elif opcion == "3":
            actualizar_producto(restaurante)

        elif opcion == "4":
            eliminar_producto(restaurante)

        elif opcion == "5":
            listar_productos(restaurante)

        elif opcion == "6":
            registrar_usuario(restaurante)

        elif opcion == "7":
            listar_usuarios(restaurante)

        elif opcion == "8":
            mostrar_categorias(restaurante)

        elif opcion == "9":
            realizar_venta(restaurante)

        elif opcion == "10":
            consultar_ventas_usuario(restaurante)

        elif opcion == "11":
            print(
                "\nPrograma finalizado correctamente."
            )
            break

        else:
            print(
                "Opción inválida. "
                "Intente nuevamente."
            )


if __name__ == "__main__":
    main()