import csv
import os

ARCHIVO_CSV = "empresas.csv"

COLUMNAS_CSV = ["RUC", "Razón Social", "Dirección"]


def cargar_empresas():
    empresas = {}

    if not os.path.exists(ARCHIVO_CSV):
        return empresas

    with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            ruc = fila["RUC"].strip()
            empresas[ruc] = {
                "razon_social": fila["Razón Social"].strip(),
                "direccion": fila["Dirección"].strip()
            }

    return empresas


def guardar_empresas(empresas):
    with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS_CSV)
        escritor.writeheader()

        for ruc, info in empresas.items():
            escritor.writerow({
                "RUC": ruc,
                "Razón Social": info["razon_social"],
                "Dirección": info["direccion"]
            })


empresas = cargar_empresas()