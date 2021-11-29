# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:17:23 2020

@author: Steve
"""


import time
import PySimpleGUI as sg

def message(text):
    status.update(text)
    window.refresh()

font = ('Helvetica', 16)
layout = [
    [sg.Text("", size=(80, 1), font=font, key='-STATUS-', text_color='white',
        background_color='green', border_width=None)],
    [sg.Button('UPDATE', font=font, key='-UPDATE-')],
]

window = sg.Window('Element Update', layout, finalize=True)
status = window['-STATUS-']

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-UPDATE-':
        message("Data preparing ...")
        time.sleep(1)
        message("Data writing ...")
        time.sleep(1)
        message("Data Saved ...")

window.close()