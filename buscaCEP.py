import requests
import json
import telaInicial

def consultaCep(self,cep):
    url= requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    if url.status_code == 200:
        print("Requisição feita com sucesso")
    if url.status_code == 400:
        print("Bad Request 400")

    endereco = url.json()
    
    return endereco