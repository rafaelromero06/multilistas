from lector import construir

if __name__ == "__main__":
    ruta_csv = "divipola.csv"
    multilista = construir(ruta_csv)
    print("Estructura jerárquica DIVIPOLA:")
    multilista.mostrar()