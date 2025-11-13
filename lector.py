from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def root():
   markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
   return render_template('index.html',markers=markers )
if __name__ == '__main__':
   app.run(host="localhost", port=8081, debug=True)

import csv
from Multilista import Multilista

def construir(ruta_csv):
    pais = Multilista()
    nodo_colombia = pais.insertar("Colombia", "País")

    with open(ruta_csv, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            departamento = fila['Departamento']
            municipio = fila['Municipio']

            
            if not nodo_colombia.sub_list:
                nodo_colombia.sub_list = Multilista()
            lista_departamentos = nodo_colombia.sub_list

            nodo_depto = lista_departamentos.buscar(departamento)
            if not nodo_depto:
                nodo_depto = lista_departamentos.insertar(departamento, "Departamento")

            # Agregar municipio al departamento
            if not nodo_depto.sub_list:
                nodo_depto.sub_list = Multilista()
            lista_municipios = nodo_depto.sub_list
            if not lista_municipios.buscar(municipio):
                lista_municipios.insertar(municipio, "Municipio")

    return pais


