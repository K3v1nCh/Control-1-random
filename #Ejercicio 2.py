#Ejercicio 2 

import requests
import json


def georeference(n):

    response= requests.get( 'https://jsonplaceholder.typicode.com/users' )
    consulta = json.loads(response.text)
    resultado=[]
    resultado.append(consulta[n]['name'])
    resultado.append(consulta[n]['address']['geo']['lat'])
    resultado.append(consulta[n]['address']['geo']['lng'])
    
    
    return resultado
print(georeference(1))