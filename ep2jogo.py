#Normalizando Base de Países
def normaliza(d1):
    d2 = {}
    
    for cont in d1:
        for pais in d1[cont]:
            d2[pais] = d1[cont][pais]
            d2[pais]['continente'] = cont
    return d2

#Sorteando Países
import random

def sorteia_pais(d1):
    listatop = list(d1.keys())
    ps = random.choice(listatop)

    return ps

#dist haversine
from math import*
def haversine(r, la, lo, la1 ,lo1):
    dist = 2*r*asin((sin(((la1 - la)/2)*(pi/180))**2 + cos(la*(pi/180)) * sin(((lo1 - lo)/2)*(pi/180))**2 * cos(la1*(pi/180)))**0.5)

    return dist

#adiciona em ordem
def adiciona_em_ordem(paises,dist,lista):
    x=0
    for i in range (0, len (lista)):
        if lista[i][1] < dist:
            x = i + 1
    lista. insert (x, [paises,dist])
    return lista






    