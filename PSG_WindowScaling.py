# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:48:17 2021

@author: Steve (orig from Jason Yang of PSG)
"""

import PySimpleGUI as sg

def new_window(win, scale=None):
    if win:
        if scale is not None:
            win.TKroot.tk.call('tk', 'scaling', scale)
        win.close()
    layout = [
        [sg.Text("Text Line here"), sg.Button("POPUP")],
        [sg.Canvas(size=(110, 110), background_color='blue', key='GRAPH')],
        [sg.Button(item) for item in ("DOWN", "NORMAL", "UP")],
    ]
    window = sg.Window('Title', layout, finalize=True)
    window['GRAPH'].Widget.configure(width='110p', height='110p')
    window['GRAPH'].Widget.create_oval('5p', '5p', '105p', '105p', fill='green', outline='white', width='5p')
    return window

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 16))

window = new_window(None, None)
dpi = window.TKroot.winfo_fpixels('1i')
now = dpi/72
inUse = now
scales = {"DOWN":inUse/1.5, "NORMAL":now, "UP":inUse*1.5}

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event in scales:
        scale = scales[event]
        window = new_window(window, scale)
    elif event == 'POPUP':
        sg.popup_ok("Hello World !")

window.close()