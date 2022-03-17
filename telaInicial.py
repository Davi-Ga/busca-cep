import PySimpleGUI as sg

class TelaInicial:
    def __init__(self):
        
        layout=[
                [sg.Text('Insira o cep desejado:'),sg.InputText()],
                [sg.Button('Ok')]
        ]
        
        self.tela=sg.Window('Busca CEP',layout)
        
    