from pyexpat import ErrorString
import PySimpleGUI as sg
import requests
import json

class TelaInicial:
    def __init__(self):
        
        layout=[
                 
                [sg.Text('CEP'),sg.Input(size = (25,0), key='CEP')],
                [sg.Button('Buscar')],
                ##[sg.Output(size=(40,10))]
        
        ]
        
        self.tela=sg.Window('Busca CEP',layout)
        
    def consultaCep(self,cep):
        url= requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if url.status_code == 200:
            print("Requisição feita com sucesso")
        elif url.status_code == 400:
            print("Bad Request 400")

        endereco = url.json()

        return endereco

    def controllerStart(self):
        while True:
            self.button, self.values = self.tela.Read()
            if self.event == sg.WIN_CLOSED:
                break
            val = self.consultaCep(self.values['CEP'])
            for k, v in val.items():
                print(k.upper() , ':' ,v)
                
iniciar = TelaInicial()
iniciar.controllerStart()