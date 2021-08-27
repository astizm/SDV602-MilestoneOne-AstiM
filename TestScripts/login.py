###basic login form

#import requirements
from tkinter import Event
from tkinter.constants import CENTER, LEFT
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import MENU_SHORTCUT_CHARACTER, Element, MenuBar, read_all_windows
#Window requirements
sg.theme('LightBlue3')
layout = [[]]
window = sg.Window('Fishiees', layout, size=(4000, 220))

#Assign variable to new flexform
login = sg.FlexForm(
    'Fishiees', element_justification=CENTER, text_justification=LEFT)

#Create layout
layout = [
    [sg.InputText('Email')],
    [sg.InputText('Password')],
    [sg.Cancel(), sg.Submit()],
    [sg.Button(button_text='Forgot Password')]
]
button, values = login.Layout(layout).Read()
#print(button, values)
