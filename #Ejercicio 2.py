#Ejercicio 2 

import requests
import json


def georeference(n):

    response= requests.get( 'https://jsonplaceholder.typicode.com/users' )
    consulta = json.loads(response.text)
    R=[]
    R.append(consulta[n]['name'])
    R.append(consulta[n]['address']['geo']['lat'])
    R.append(consulta[n]['address']['geo']['lng'])
    
    
    return R
print(georeference(1))
