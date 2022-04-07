#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:36:14 2022

@author: gimsa
"""


from flask import  Flask
from calculadora import Calcular
import json 


# metas_niveles= {
#     'A': 5,
#     'B': 10,
#     'C': 15,
#     'Cuauh': 20}

#Importar jsons

data = json.load(open('jugadores.json', 'r'))
metas_niveles = json.load(open('equipos_metas.json', 'r'))

app = Flask(__name__)


@app.route('/calcular')
def calcular():
    result = Calcular(metas_niveles, data)
    result = json.dumps({"jugadores": result})
    return result

@app.route('/jugadores')
def jugadores():
    return data

@app.route('/metas')
def metas():
    return metas_niveles


if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
    