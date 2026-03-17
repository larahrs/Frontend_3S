import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_rOI782M7el2W7BcWUfYxMzun7BK7QIGiUIS4fkzvSlv9Ljr06mBc5X20mOfSziB7"
    }

    resposta = requests.get(url,headers=headers)

    return resposta.json()


def get_breeds():
    url = f"{base_url}/breeds"
    resposta = requests.get(url)

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)

    return resposta.json()[0]