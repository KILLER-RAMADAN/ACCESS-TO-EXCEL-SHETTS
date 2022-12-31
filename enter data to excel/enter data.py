import PySimpleGUI as sg
import pandas as pd
from tkinter import *
import os
sg.theme("DarkBlack")
sg.theme('DarkBlack')
# file location..
root = Tk()
root.withdraw()
root.title('File Explorer BY AHMED RAMADAN') # Set window title
layout = [[sg.T("")], [sg.Text("CHOOSE EXCEL FILE: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-IN-",file_types={("ALL FILES","*.*"),("PNG", "*.png"),("JPEG", "*.jpg"),("EXCEL FILE","*.xlsx*")})],[sg.Button("Submit")]]
###Building Window
window = sg.Window('FILE BROWSER BY AHMED RAMADAN 🐱‍👤', layout, size=(600,120))   
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
     x=values["-IN-"]    
     read_excel_file = pd.read_excel(str(x))
     window.close()
    else:
        os.startfile(values["-IN-"])  
#layout Appearance
    layout = [
     [sg.Text('Please fill out the following fields:')],
     [sg.Text('ID', size=(15, 1)), sg.Spin(
        [i for i in range(1, 10001)], initial_value=0, key='ID')],
     [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],
     [sg.Text('phone number', size=(15, 1)), sg.InputText(key="phone number")],
     [sg.Text('City', size=(15, 1)), sg.InputText(key='City')],
     [sg.Text('Favorite Color', size=(15, 1)), sg.Combo(
        ['Green', 'Blue', 'Red', "black", "yellow"], key='Favorite Color')],
     [sg.Text('I speak', size=(15, 1)),
     sg.Checkbox('German', key='German'),
     sg.Checkbox('Spanish', key='Spanish'),
     sg.Checkbox('English', key='English'),
     sg.Checkbox("Arabic",key="Arabic")],
     [sg.Text('No. of Children', size=(15, 1)), sg.Spin(
        [i for i in range(0, 20)], initial_value=0, key='Children')],
     [sg.Submit(), sg.Button('Clear'), sg.Exit()]
  ]
# window preferences
window = sg.Window('ADD DATA TO EXCEL SHEETS BY "AHMED RAMADAN" 🐱‍🏍',
                   layout,
                   default_element_size=(50, 60),
                   resizable=True, finalize=True)

# to clear every thing when you submit 
def clear_input():
    for key in values:
        window[key]('')
    return NONE
9
# all functions here
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        read_excel_file = pd.concat([read_excel_file, new_record], ignore_index=True)
        read_excel_file.to_excel(x, index=False)
        sg.popup('Data inserted!!')
        clear_input()
window.close()

