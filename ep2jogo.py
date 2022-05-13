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
    
    