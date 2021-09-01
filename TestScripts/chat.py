#import requirements
from tkinter import Event
from tkinter.constants import CENTER, LEFT
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import MENU_SHORTCUT_CHARACTER, Element, MenuBar, Window, read_all_windows
#Window requirements
sg.theme('LightBlue3')
layout = [[]]
window = sg.Window('Fishiees Chat', element_justification=CENTER,
                     text_justification=LEFT)
# layout = [
#         [sg.Text('Test',size=(40,1))],
#         [sg.Output(size=(110,20))],
#         [sg.Multiline(size=(70,5), enter_submits=False, key='-QUERY-', do_not_clear=False)],
#         sg.Button('Send', button_color=(sg.GREENS[0], sg.BLUES[0]), bind_return_key=True),
#         sg.Button('Exit', button_color=(sg.YELLOWS[0], sg.BLUES[0]))]

 
# window.close()


# def get_layout(cls):
#     return sg.Column(
#         [
#             [
#                 sg.Multiline(
#                     key='logger',
#                     font=('Courier New', 9),
#                     autoscroll=True,
#                     size=(92, 34),
#                     pad=(0, (15, 0)),
#                     background_color='grey20',
#                     disabled=False)],
#             [
#                 cls.generate_clear_btn('logger')
#             ]
#         ],
#         key='gui_tab_log',
#         size=cls.PRIMARY_COL_TAB_SIZE,
#         visible=False
#     )
