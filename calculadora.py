import PySimpleGUI

sg.theme('random')

# Tamanho Da Tela
WIN_w = 30
WIN_h = 50

# Menu layout
menu_layout = [['File', ['Save', 'Exit']],
               ['Tools', ['Waiting']],
               ['Help', ['About']]]

# Elementos dentro da nossa - ROW 1
layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'),
           sg.Button('<-', font=('Consolas', 20), key='-BACKARROW-'),
           sg.Button('C', font=('Consolas', 20), key='-CLEAR-')],
# Aqui começa a ROW 2
          [sg.Button('7', font=('Consolas', 20), key='-SEVEN-'),
           sg.Button('8', font=('Consolas', 20), key='-EIGHT-'),
           sg.Button('9', font=('Consolas', 20), key='-NINE-'),
           sg.Button('+', font=('Consolas', 20), key='-PLUS-'),
           sg.Button('*', font=('Consolas', 20), key='-TIMES-')],
# Aqui começa a ROW 3
          [sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
           sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
           sg.Button('6', font=('Consolas', 20), key='-SIX-'),
           sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
           sg.Button('/', font=('Consolas', 20), key='DIVIDED')],
# Aqui começa a ROW 4
          [sg.Button('1', font=('Consolas', 20), key='-ONE-'),
           sg.Button('2', font=('Consolas', 20), key='-TWO-'),
           sg.Button('3', font=('Consolas', 20), key='-THREE-'),
           sg.button('0', font=('Consolas', 20), key='-RESULT-')]]