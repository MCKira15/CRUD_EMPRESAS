import os

ANCHO = 50


def limpiar():
    os.system("cls")


def pausa():
    input("Presione ENTER para continuar...")


def titulo(texto):
    print("=" * ANCHO)
    print(" " * 10 + texto)
    print("=" * ANCHO)