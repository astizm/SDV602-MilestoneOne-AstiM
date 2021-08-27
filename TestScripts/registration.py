### Basic registration form for user input

#import requirements
from tkinter import Event
from tkinter.constants import CENTER, LEFT
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import MENU_SHORTCUT_CHARACTER, Element, MenuBar, read_all_windows
#Window requirements
sg.theme('LightBlue3')
layout = [[]]
register = sg.Window('Fishiees', element_justification=CENTER, text_justification=LEFT, size=(300,500))

#Create layout
layout = [ 
    [sg.Text('New User')],
    [sg.InputText('Email')], 
    [sg.InputText('Password')],
    [sg.InputText('Confirm password')],
    [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
    [sg.InputText('Name')], 
    [sg.InputText('Organisation')],
    [sg.InputText('Occupation')],
    
    [sg.Cancel(), sg.Submit()]
]
button, values = register.Layout(layout).Read()
print(sg.Window.get_screen_size())

#w,h = sg.Window.get_screen_dimensions()




