import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"
    resposta = requests.get(url)

    return resposta.json()


def get_breeds():
    url = f"{base_url}/breeds"
    resposta = requests.get(url)
