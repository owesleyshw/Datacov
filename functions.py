import os
import requests

# Pega os dados do Brasil tudo atualizado
def dados():
    response = requests.get(os.environ.get('url_dados')).json()
    if response['planilha']:
        del response['planilha']
    if response['dt_updated']:
        del response['dt_updated']

    return response

# Pega a hora em que os dados foram atualizados
def dt_updated():
    headers = {
        'x-parse-application-id':'unAFkcaNDeXajurGB7LChj8SgQYS2ptm'
    }
    response = requests.get(os.environ.get('url_data'), headers=headers).json()

    return response['results'][0]['dt_atualizacao']

# Pega os dados da regiões, e seus respectivos estados
def regioes():
    headers = {
        'x-parse-application-id':'unAFkcaNDeXajurGB7LChj8SgQYS2ptm'
    }
    regiao = requests.get(os.environ.get('url_regioes'), headers=headers).json()[1]
    sul = requests.get(os.environ.get('url_sul'), headers=headers).json()
    sudeste = requests.get(os.environ.get('url_sudeste'), headers=headers).json()
    norte = requests.get(os.environ.get('url_norte'), headers=headers).json()
    nordeste = requests.get(os.environ.get('url_nordeste'), headers=headers).json()
    centro_oeste = requests.get(os.environ.get('url_centro_oeste'), headers=headers).json()
    
    pais = []
    regioes = []
    
    for i in regiao:
        if i['_id'] == "Brasil":
            pais.append(i)
        else:
            if i['_id'] == "Centro-Oeste":
                i['count'] = centro_oeste
                regioes.append(i)
            if i['_id'] == "Sudeste":
                i['count'] = sudeste
                regioes.append(i)
            if i['_id'] == "Sul":
                i['count'] = sul
                regioes.append(i)
            if i['_id'] == "Nordeste":
                i['count'] = nordeste
                regioes.append(i)
            if i['_id'] == "Norte":
                i['count'] = norte
                regioes.append(i)

    response = {'Brasil': pais,'Regioes': regioes}
    return response