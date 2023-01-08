import sqlite3
from tkinter import *
import PySimpleGUI as sg
import pandas as pd
import os
#____connection to sqlite3_______
db=sqlite3.connect("data.db")
cr=db.cursor()
cr.execute('''create table if not exists "accounts" (ID integer ,user_name text ,password text )''')
#_____Make Gui Software______
root = Tk() 
root.geometry("370x133")  
root.title('Signup_Form')
lbl=Label(root, text="Developed by Ahmed Ramadan",relief="ridge", fg='Black', font=("ROMAN", 16))
lbl.place(x=0, y=100)
user_label = Label(root, text = 'Enter Username:') 
user_entry = Entry(root) 
pass_label = Label(root, text = 'Enter Password:') 
pass_entry = Entry(root,show='*')
id_label=Label(root,text="Enter ID:")
id_entry=Entry(root,show="*")
id_label.grid(row=2, column=0)  
id_entry.grid(row=2, column=1)
user_label.grid(row=0, column=0)  
user_entry.grid(row=0, column=1)  
pass_label.grid(row=1, column=0)  
pass_entry.grid(row=1, column=1)  
# Create a login button and place it in the third row of grid manager    
Button ( root , text="Signup" , command = lambda : checklogin1()).grid ( row = 25 ,columnspan = 500 )     
def checklogin1():
  #____check if your id found in database or not_____ 
 if user_entry.get()!="" and pass_entry.get()!="" and id_entry.get()!="":
        data=cr.execute(f'''select ID,user_name from accounts where ID="{id_entry.get()}" ''').fetchone()
        if data==None:
         data=cr.execute(f'''insert into accounts (ID,user_name,password) values("{id_entry.get()}","{user_entry.get()}","{pass_entry.get()}")''')
         sg.popup(f"{user_entry.get().upper()} Your Account Created Successfully Enjoy..")
         db.commit()
         #_______if your id found in database________
        else:
          sg.popup(f"Welcome {user_entry.get().upper()}")
        root.title("Login_Form")
        Button ( root , text="Login Now With Your Account" , command = lambda : logain()).grid ( row = 25 ,columnspan = 5 )   
        def logain():
         data=cr.execute(f'''SELECT password FROM accounts WHERE ID="{id_entry.get()}"''').fetchone()
         data1=cr.execute(f'''SELECT password FROM accounts WHERE user_name="{user_entry.get()}"''').fetchone()
         if not data1:
           sg.popup("Your User_Name Not Found In DataBase!!")
         elif not data:
           sg.popup("Your ID Not Found In DataBase!!") #User Name Not Found
           db.commit()
         elif data[0]==pass_entry.get():
          sg.popup(f"Hello {user_entry.get().upper()} In Our Program")
          root.withdraw()
          #____Access To Excel Sheets_____
          root1 = Tk() 
          root1.geometry("380x120")
          root1.title('Access To Program')
          lbl1=Label(root1, text="Developed by Ahmed Ramadan",relief="ridge", fg='Black', font=("ROMAN", 16))
          lbl1.place(x=0, y=90)
          user_label1= Label(root1, text = 'Username') 
          user_entry1 = Entry(root1) 
          pass_label1 = Label(root1, text = 'Password') 
          pass_entry1 = Entry(root1,show='*')
          id_label1=Label(root1, text = 'ID') 
          id_entry1 = Entry(root1,show="*") 
          id_label1.grid(row=2, column=0) 
          id_entry1.grid(row=2, column=1)  
          user_label1.grid(row=0, column=0)  
          user_entry1.grid(row=0, column=1)  
          pass_label1.grid(row=1, column=0)  
          pass_entry1.grid(row=1, column=1)  
          Button ( root1 , text="Login To Program With Your ID" , command = lambda : checklogin()).grid ( row = 70 ,columnspan = 100 )
          #________File Browser_________
          def checklogin():
           menu_def=[["Help",["About"]]] 
           sg.theme("SystemDefault")
           if user_entry1.get()==user_entry.get() and pass_entry1.get() == pass_entry.get() and id_entry1.get()==id_entry.get():
             root1.withdraw()
             sg.popup(f"Login Successfully {user_entry.get()} Enjoy")             
             root1.title("Login Successfully")
             layout = [[sg.MenubarCustom(menu_def,tearoff=False)],[sg.T("")], [sg.Text("CHOOSE EXCEL FILE: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(button_color="tomato",key="-IN-",file_types={("EXCEL FILE","*.xlsx*")})],[sg.Button("Submit",s=16,button_color="tomato")]]
             window = sg.Window('FILE BROWSER 💾',layout,default_element_size=(10,0))
              #_______running software________
             while True:
              event, values = window.read()
              if event == sg.WIN_CLOSED or event=="Exit":
               break  
              if event=="About":
               window.disappear()
               sg.popup("Version 2.0","Access Excel File..","BY_AHMED_RAMADAN",grab_anywhere=True)
               window.reappear()
              if event == "Submit":
               x=values["-IN-"]    
               read_excel_file = pd.read_excel(str(x))
               window.close()
               sg.popup("preparing app.")
               window.close()
               #_________components of software_________
              layout = [
              [sg.Text("BY AHMED RAMADAN",relief="ridge")],
              [sg.Text('Please fill out the following fields:')],
              [sg.Text('ID', size=(15, 1)), sg.Spin(
              [i for i in range(1, 10000001)], initial_value=0, key='ID')],
              [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],
              [sg.Text('Type', size=(15, 1)),sg.Checkbox('Man', key='Man'),
              sg.Checkbox('Woman',     key='Woman')],
              [sg.Text('Administration', size=(15, 1)), sg.InputText(key='Administration')],
              [sg.Text('Occupation', size=(15, 1)), sg.InputText(key='Occupation')],
              [sg.Text('Data of Birth', size=(15, 1)), sg.InputText(key='Data of Birth')],
              [sg.Text('Email', size=(15, 1)), sg.InputText(key='Email')],
              [sg.Text('phone number', size=(15, 1)), sg.InputText(key="phone number")],
              [sg.Text('City', size=(15, 1)), sg.InputText(key='City')],
              [sg.Text('Favorite Color', size=(15, 1)), sg.Combo(
              ['Green', 'Blue', 'Red', "black", "yellow"], key='Favorite Color')],
              [sg.Text('Language', size=(15, 1)),
              sg.Checkbox('German', key='German'),
              sg.Checkbox('Spanish', key='Spanish'),
              sg.Checkbox('English', key='English'),
              sg.Checkbox("Arabic",key="Arabic")],
              [sg.Text('Social Situation', size=(15,1)),sg.Checkbox('Married', key='Married'),
              sg.Checkbox('Unmarried', key='Unmarried')],
              [sg.Text('No. of Children', size=(15, 1)), sg.Spin(
              [i for i in range(0, 20)], initial_value=0, key='Children')],
              [sg.Submit(s=16,button_color="tomato"), sg.Button('Clear',size=16,button_color="tomato"), sg.Exit(s=16,button_color="tomato")]]   
             window = sg.Window(' EXCEL SHEETS ACCESS 💾',
                   layout,
                   default_element_size=(50, 60),
                   resizable=False, finalize=True,use_custom_titlebar=True)
             def clear_input():
              for key in values:
               window[key]('')
              return NONE
               #_________read excel file______________
             while True:
              event, values = window.read()
              if event == sg.WIN_CLOSED or event == 'Exit':
               sg.popup("Thanks For Using Program..☺")
               break
              if event == 'Clear':
               clear_input()
               sg.popup("data cleared") 
              if event == 'Submit':
               new_record = pd.DataFrame(values, index=[0])
               read_excel_file = pd.concat([read_excel_file, new_record], ignore_index=True)
               read_excel_file.to_excel(x, index=False)
               sg.popup('Data inserted!!')
               clear_input()
             window.close()
               #_________check conditions one__________
           elif user_entry1.get()=="":
             sg.popup("Enter User_Name")  
           elif pass_entry1.get()=="":
             sg.popup("Enter Password") 
           elif id_entry1.get()=="":
             sg.popup("Enter ID") 
           else:   
            sg.popup("Enter Correct Information!!")
         else:
          sg.popup("Your Password Not Found In DataBase!!")
           #______check conditions two________ 
 elif user_entry.get()!="" and pass_entry.get()!="":
     sg.popup("Enter ID Please")
 elif pass_entry.get()!="" and id_entry.get()!="":
     sg.popup("Enter User_Name Please")
 else:
     sg.popup("Please Fill The Following Fields ")

root.mainloop()
#________Ending Of The Program____________ 
