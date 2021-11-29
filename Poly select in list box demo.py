# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:16:21 2020

@author: steve
"""

import PySimpleGUI as sg

"""
    Demo - Fill a listbox with list of files FilesBrowse button and use of Listbox.get method
"""


layout = [  [sg.Listbox([f'Item {i}' for i in range(20)], size=(30,10), select_mode=sg.SELECT_MODE_EXTENDED, key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    print(f'get = {window["-FILESLB-"].get()}')
    # When choice has been made, then fill in the listbox with the choices
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
window.close()