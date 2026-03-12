from time import sleep
from src.datos import empresas, guardar_empresas
from src.utils import pausa, titulo, limpiar
from src.decoradores import pantalla


@pantalla("REGISTRAR EMPRESA")
def registrar_empresa():
    ruc = input("INGRESE RUC: ").strip()
    razon_social = input("INGRESE RAZÓN SOCIAL: ").strip()
    direccion = input("INGRESE DIRECCIÓN: ").strip()

    if not ruc:
        print("El RUC no puede estar vacío.")
        return

    if ruc in empresas:
        print("Ya existe una empresa con ese RUC.")
        return

    empresas[ruc] = {
        "razon_social": razon_social,
        "direccion": direccion
    }

    print("EMPRESA REGISTRADA EXITOSAMENTE.")


@pantalla("MOSTRAR DATOS")
def mostrar_empresas():
    if not empresas:
        print("No hay empresas registradas.")
        return

    for ruc, info in empresas.items():
        print(f"RUC: {ruc}")
        print(f"RAZÓN SOCIAL: {info['razon_social']}")
        print(f"DIRECCIÓN: {info['direccion']}")
        print("*" * 50)


@pantalla("ACTUALIZAR EMPRESA")
def actualizar_empresa():
    ruc = input("INGRESE EL RUC DE LA EMPRESA: ").strip()

    if ruc not in empresas:
        print("EMPRESA NO ENCONTRADA.")
        return

    print(f"EMPRESA ENCONTRADA: {empresas[ruc]['razon_social']}")
    print("Ingrese nuevos datos o presione ENTER para conservar los anteriores.")

    nueva_razon_social = input(
        f"Nueva Razón Social ({empresas[ruc]['razon_social']}): "
    ).strip()

    nueva_direccion = input(
        f"Nueva Dirección ({empresas[ruc]['direccion']}): "
    ).strip()

    if nueva_razon_social:
        empresas[ruc]["razon_social"] = nueva_razon_social

    if nueva_direccion:
        empresas[ruc]["direccion"] = nueva_direccion

    print("EMPRESA ACTUALIZADA.")


@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("INGRESE RUC DE LA EMPRESA: ").strip()

    if ruc in empresas:
        del empresas[ruc]
        print("EMPRESA ELIMINADA.")
    else:
        print("EMPRESA NO ENCONTRADA.")


def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
[1] REGISTRAR EMPRESA
[2] MOSTRAR EMPRESAS
[3] ACTUALIZAR EMPRESA
[4] ELIMINAR EMPRESA
[5] SALIR
""")

        try:
            opcion = int(input("INGRESE OPCIÓN: ").strip())
        except ValueError:
            print("Debe ingresar un número válido.")
            pausa()
            continue

        if opcion == 1:
            registrar_empresa()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresa()
            pausa()
        elif opcion == 4:
            eliminar_empresa()
            pausa()
        elif opcion == 5:
            guardar_empresas(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("Datos guardados en empresas.csv")
            sleep(2)
            break
        else:
            print("Opción no válida.")
            pausa()