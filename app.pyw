import os, shelve, shutil
import PySimpleGUI as sg

class star_load:

    def __init__(self):

        self.data_arq = shelve.open('path_')
        choices = list(self.data_arq.keys())

        sg.theme('DarkBlue14')
        layout = [ [sg.Text('Filename')],
                [sg.Input(key='-IN-'), sg.FileBrowse()],
                [sg.Save(), sg.Cancel()],
                [sg.Text('Listas de arqs')],
                [sg.Listbox(choices, size=(50,10, len(choices)), key='-OUTPUT-')],
                [sg.Button('Excluir')] ]

        self.windows = sg.Window('Start Load', layout)
        
    def Iniciar(self):

        while True:
            events, values = self.windows.read()

            if events == sg.WIN_CLOSED:
                break
            elif events == 'Save':
                path_arq =str(values['Browse']).replace('/','\\')
                self.data_arq[os.path.basename(path_arq)] = path_arq
                self.windows['-OUTPUT-'].update(self.data_arq)
 
            elif events == 'Excluir':
                #print(self.datavalues['-OUTPUT-'][0])
                del self.data_arq[values['-OUTPUT-'][0]]
                self.windows['-OUTPUT-'].update(self.data_arq)

            elif events == None:
                    sg.popup('Não selecionou o arquivo')

        self.windows.close()


start = star_load()
start.Iniciar()


