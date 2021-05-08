import PySimpleGUI as sg

sg.theme('DarkBlue5')

#TAMANHO DA TELA
WIN_W = 30
WIN_H = 50

#MENU LAYOUT
menu_layout =   [['File', ['Save', 'Exit']],
                ['Tools', ['Waiting']],
                ['Help', ['About']]]

#ELEMENTOS DE DENTRO DA TELA ROW 1
layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'), #VISOR DA CALCULADORA
          sg.Button('<-', font=('Consolas', 20), key='-BACKARROW-'), #BOTAO DE APAGAR ULTIMA DIGITAÇÃO
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

         
#CLASS WITH THE APP INSIDE
class App():
    def __init__(self):
        self.window = sg.Window('PyCalculator', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)

# FUNCTION IN THE  MENU_LAYOUT
    def about(self):
        sg.popup('About', 'Just an example', 'contact me')

#RESULS OF CALCULATOR 
    def result(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['-BOX-'])
        if self.oper == '-':
            return float(self.result) - float(self.values['-BOX-'])
        if self.oper == '*':
            return float(self.result) * float(self.values['-BOX-'])
        if self.oper == '/':
            return float(self.result) / float(self.values['-BOX-'])

# THIS FUNCTION KEEP THE APLICATION WORKING
    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

# IF U CLICK ON 'ABOUT' THIS FUNCTION WILL START
        if event in ('About'):
            self.about()

        if event in ('-ONE-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].upade(values='1')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')


        if event in ('-TWO-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='2')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')


        if event in ('-THREE-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='3')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')


        if event in ('-FOUR-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='4')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')


        if event in ('-FIVE-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='5')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')

        if event in ('-SIX-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='6')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')

        if event in ('-SEVEN-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].updae(values='7')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')

        if event in ('-EIGHT'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='8')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')

        if event in ('-NINE-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='9')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')

        if event in ('-ZERO-'):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].update(values='0')
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')

#HERE WILL BE THE FUNCTIONS OF CLEAR AND CLEAR ALL
        if event in ('-CLEAR-'):
            self.result = 0
            self.window['-BOX-'].update(value=self.result)

        if event in ('-BACKARROW-'):
            self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

#FUNCTIONS  + - / * =
        if event in ('-PLUS-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '+'
                self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

        if event in ('-MINUS-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '-'
                self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

        if event in ('-DIVIDED-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '/'
                self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

        if event in ('-TIMES'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '*'
                self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

        if event in ('-RESULT-'):
                self.result = self.resulter()
                self.window['-BOX-'].update(value=self.result)
                self.result = 0
                self.oper = ''

App().start()

        

