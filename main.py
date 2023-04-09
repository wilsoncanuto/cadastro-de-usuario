# Wilson canuto - 2023
from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout = [
    [sg.Text("Usuário"), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text("Senha"), sg.Input(key='senha', password_char="*", size=(20, 1))],
    [sg.Checkbox("Salvar login?")],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window("SSSystem of bikes 2023", layout)
#ler eventon
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Entrar':
        if valores['usuario'] == 'Wilson' and valores['senha'] =='203040':
            print("Bem-Vindo ao Bicicletário Inteligente")
        else:
            print("Usuario Invalido")