### Basic registration form for user input

#import requirements
import textwrap
from tkinter import Event, Menu
from tkinter.constants import CENTER, LEFT, RIGHT, VERTICAL
from typing import Sized
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import BLUES, GREENS, MENU_SHORTCUT_CHARACTER, ButtonMenu, Element, Exit, MenuBar, VerticalSeparator, button_color_to_tuple, main, read_all_windows
#Window requirements
sg.theme('LightBlue3')
layout = [[]]
register = sg.Window('Fishiees', element_justification=CENTER,
                     text_justification=LEFT, size=(300, 500))
logo = [[sg.Image(r'C:\Users\ASUS\OneDrive - NMIT\Documents\Sem2 2021\SDV602\SDV602-MilestoneOne-AstiM\Documentation\src\fish-multiple.png')]]
menu_def = ['Login'], ['Register']

layout_menu = [
    [sg.Menu(menu_def,
             background_color='grey',
             pad=(40,0)
             )]
    ]
### Main Text
layout_column = [ 
    [sg.Text(text="fishiees",
             size=(100, 1),
             font='Consolas',
             text_color='Yellow',
             justification=CENTER,
             pad=(0, 160)
             )],
]
#Assemble layout
layout = [
    [sg.Column(layout_menu)],
    [sg.Column(layout_column)],
    [sg.Frame('',  # empty frame
              logo,  # logo image
              size=(200, 5),
              element_justification=CENTER
              )]
    ]
button, values = register.Layout(layout).Read()

#
# while True:
#       event, values = window.read()
#       if event == sg.WIN_CLOSED or event == 'Exit':
#           break
#       print('Button = ', event)
#       if event == 'Login':
#           sg.popup('Login')
#       elif event == 'Register':
#           filename = sg.popup_get_file('login.py', no_window=True)
#           print(filename)     

