import PySimpleGUI as sg
import pandas as pd
from tkinter import *
from tkinter import filedialog
# Add color to the window
sg.theme('Dark2')
# file location..
root = Tk()
root.withdraw()
root.title('File Explorer') # Set window title
filename = filedialog.askopenfilename(initialdir = "\\",initialfile='hello',title = "Select a File",filetypes ={("excel files","*.xlsx*"),("all files","*.*"),("PNG", "*.png"),("JPEG", "*.jpg")})
print(filename)
x=str(filename)
df = pd.read_excel(str(x))
#layout Appearance
layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('ID', size=(15, 1)), sg.Spin(
        [i for i in range(1, 20)], initial_value=0, key='ID')],
    [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],
    [sg.Text('phone number', size=(15, 1)), sg.InputText(key="phone number")],
    [sg.Text('City', size=(15, 1)), sg.InputText(key='City')],
    [sg.Text('Favorite Color', size=(15, 1)), sg.Combo(
        ['Green', 'Blue', 'Red', "black", "yellow"], key='Favorite Color')],
    [sg.Text('I speak', size=(15, 1)),
     sg.Checkbox('German', key='German'),
     sg.Checkbox('Spanish', key='Spanish'),
     sg.Checkbox('English', key='English')],
    [sg.Text('No. of Children', size=(15, 1)), sg.Spin(
        [i for i in range(0, 20)], initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]
# window preferences
window = sg.Window('ADD DATA TO EXCEL SHEETS BY AHMED RAMADAN 😃',
                   layout,
                   default_element_size=(50, 20),
                   resizable=True, finalize=True)

# to clear every thing when you submit 
def clear_input():
    for key in values:
        window[key]('')
    return None

# all functions here
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(x, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()

