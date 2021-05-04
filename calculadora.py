import PySimpleGUi as sg

sg.theme('random')

#TAMANHO DA TELA
WIN_W = 30
WIN_H = 50

#MENU LAYOUT
menu_layout = [['File', ['Save', 'Exit']],
                ['Tools', ['Waiting']],
                ['Help', ['About']]]

#ELEMENTOS DE DENTRO DA TELA ROW 1
layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'), #VISOR DA CALCULADORA
          sg.Button('Cc', font=('Consolas', 20), key='-BACKAROW-',20), #BOTAO DE APAGAR ULTIMA DIGITAÇÃO
          sg.Button('C', font=('Consolas', 20), key='-CLEAR-')], #BOTÃO PARA LIMPAR TUDO
#AQUI COMEÇA A ROW 2
         [sg.Button('7', font=('Consolas', 20), key='-SEVEN-'),
          sg.Button('8', font=('Consolas', 20), key='-EIGHT-'),
          sg.Button('9', font=('Consolas', 20), key='-NINE-'),
          sg.Button('+', font=('Consolas', 20), key='-PLUS-'),
          sg.Button('*', font=('Consolas', 20), key='-TIMES-')],
#AQUI COMEÇA A ROW 3
         [sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
          sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
          sg.Button('6', font=('Consolas', 20), key='-SIX-'),
          sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
          sg.Button('/', font=('Consolas', 20), key='-DIVIDED-')],
#AQUI COMEÇA A ROW 4
         [sg.Button('1', font=('Consolas', 20), key='-ONE-'),
          sg.Button('2', font=('Consolas', 20), key='-TWO-'),
          sg.Button('3', font=('Consolas', 20), key='-THREE-'),
          sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
          sg.Button('=', font=('Consolas', 20), key='-RESULT-')]]

         

