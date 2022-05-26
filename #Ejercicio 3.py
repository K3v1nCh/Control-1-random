#Ejercicio 3 


import requests
import json

def comment(n):
    
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    dic = {'comentario' : consulta[n]['body']}
    return dic
print(comment(10))
