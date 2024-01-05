import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(api_url_categories) # GET
    print(r.status_code) # imprime el status code
    print(r.text) # imprime el texto de la respuesta
    print(type(r.text)) # imprime el tipo de dato de la respuesta
    categories = r.json() # convierte el texto de la respuesta en un diccionario
    for category in categories:
        print(category['name']) # imprime el nombre de cada categoria