#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:15:28 2022

@author: Daegas

Problema:
El sueldo de los jugadores del Resuelve FC se compone de dos partes un sueldo fijo y un bono variable, la suma de estas dos partes es el sueldo de un jugador. El bono variable se compone de dos partes meta de goles individual y meta de goles por equipo cada una tiene un peso de 50%.

Tu programa deberá hacer el cálculo del sueldo de los jugadores del Resuelve FC.

¿Cómo se calculan los alcances de meta y bonos?
La meta individual de goles por jugador depende del nivel que tenga asignado:

Nivel	Goles/mes
A	5
B	10
C	15
Cuauh	20
Ejemplo: Los jugadores Juan, Pedro, Martín y Luis anotaron así durante el mes:

Jugador	Nivel	Goles anotados en el mes/mínimo requerido
Juan	A	6/5
Pedro	B	7/10
Martín	C	16/15
Luis	Cuauh	19/20
total		48/50
En el bono por equipo tendrían un alcance de 96% Luis tendría un alcance individual de 95% para un alcance total de 95.5% El suelo fijo de Luis es de 50,000.00 y su bono es de 10,000.00 por lo que su sueldo final será $59,550.00
"""

import json 
import numpy as np

#Metas por nivel del jugador
metas_niveles = {
    'A': 5,
    'B': 10,
    'C': 15,
    'Cuauh': 20}

#Importar json
data = json.load(open('jugadores.json', 'r'))

#number of players
n= len(data['jugadores'])

#Arreglo de coordenadas (anotados,meta) individual
goles = []
metas = []

#Calcular el total del equipo
for i in range(n):
    jugador = data['jugadores'][i]
    goles.append(jugador['goles'])
    metas.append(metas_niveles[jugador['nivel']]) 
    
p_grupal = sum(goles) /sum(metas)

#Calcular porcentaje individual
goles = np.array(goles)
metas = np.array(metas)
p_individual = np.divide(goles,metas)

#Calcular bonos
sueldo = 0
for i in range(n):
    jugador = data['jugadores'][i]
    sueldo = jugador['sueldo']
    p_total = (p_grupal + p_individual[i])/2
    sueldo += jugador['bono'] * p_total
    jugador['sueldo_completo']= sueldo
    
# Pretty Print JSON
pretty = json.dumps(data, indent=4)
print(pretty)    
    
    
    
    
    
    
    
    
    