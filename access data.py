import sqlite3
from tkinter import *
import tkinter as tk
import PySimpleGUI as sg
import pandas as pd
import os
from PIL import ImageTk, Image
import string
sg.theme("DarkGrey15")
#____connection to sqlite3_______#
db=sqlite3.connect("data.db")
cr=db.cursor()
cr.execute('''create table if not exists "accounts" (ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,user_name TEXT NOT NULL ,password VARCHAR(10) )''')
sg.popup_auto_close("successfully connect to database.. ")
#_____make a function to close your window______
def quit():
    global root
    root.quit() 
def char():
  a=string.ascii_uppercase
  for c in a:
    return c + id_entry.get()
#________login function _________#
#/////////////////////////////////////////////////////////////////////////////////////////////////////////// 
def login():
         data=cr.execute(f'''SELECT password FROM accounts WHERE user_name="{user_entry.get()}"''').fetchone()#>>to check your pass is correct..??
         data2=cr.execute(f'''SELECT user_name FROM accounts WHERE password="{pass_entry.get()}"''').fetchone()
         data1=cr.execute(f'''SELECT user_name FROM accounts WHERE ID="{id_entry.get()}"''').fetchone()#>>to check your id is correct??
         if not data1:
           sg.popup("Your ID Not Found In DataBase!!")#if do not found..
         elif not data:
           sg.popup("Your user_name Not Found In DataBase!!") #if do not found..
           db.commit()
         elif not data2:
           sg.popup("Enter Correct Password MAN!!") #if do not found..
           db.commit()
         elif data[0]==pass_entry.get():
          sg.popup(f"Ahllan {user_entry.get()} In our program")#if founded you can access to program...
          root.withdraw()
          root1 =tk.Tk() 
          root1.geometry("505x135+500+300")
          root1.iconbitmap('among.ico')
          root1.title(f"Ahllan {user_entry.get()}")
          lbl1=Label(root1, text=f"AHLLAN||{user_entry.get()}", fg='black', font="Times 20 italic bold")
          lbl1.place(x=185, y=3)
          user_label1= Label(root1, text = 'Username',fg='black') 
          user_entry1 = Entry(root1) 
          pass_label1 = Label(root1, text = 'Password',fg='black') 
          pass_entry1 = Entry(root1,show='*')
          id_label1=Label(root1, text = 'ID',fg='black') 
          id_entry1 = Entry(root1,show="*") 
          id_label1.grid(row=2, column=0) 
          id_entry1.grid(row=2, column=1)  
          user_label1.grid(row=0, column=0)  
          user_entry1.grid(row=0, column=1)  
          pass_label1.grid(row=1, column=0)  
          pass_entry1.grid(row=1, column=1) 
          Button ( root1 , text="Login To Program With Your ID" , bg='white',activebackground='green' ,fg='black',command = lambda : checklogin()).place(x=50, y=70) 
          Button(root1, text="Quit", bg='red', fg='white',command=quit,activebackground='red',width=10).place(x=190, y=40) 
          #________File Browser_________
          
          
          def checklogin():
           menu_def=[["Help",["About"]],["User",["USER_NAME"]]] 
           if user_entry1.get()==user_entry.get() and pass_entry1.get() ==char() and id_entry1.get()==id_entry.get():
             root1.withdraw()
             sg.popup(f"Login Successfully {user_entry.get()} Enjoy")             
             root1.title("Login Successfully")
             layout = [[sg.MenubarCustom(menu_def,tearoff=False)],[sg.T("")], [sg.Text("ENTER FILE LOCATION:"), sg.Input(key="-CHOOSE-" ,change_submits=True), sg.FileBrowse(button_color="tomato",key="-IN-",file_types={("EXCEL FILE","*.xlsx")})],[sg.Button("Submit",s=16,button_color="tomato")]]
             window = sg.Window('FILE BROWSER 💾',
                   layout,
                   default_element_size=(50, 60),
                   resizable=False, finalize=True,use_custom_titlebar=True)
              #_______running software________
             while True:
              event, values = window.read()
              if event==sg.WIN_CLOSED:
               quit()   
               break 
              if values['-CHOOSE-']=="":
                sg.popup("PLEASE ENTER LOCATION")
                continue
              if event=="EXIT" :
                sg.popup("Thanks..")
                break 
              if event=="About":
               window.disappear()
               sg.popup("Version 2.0","Access Excel File..","BY_AHMED_RAMADAN",grab_anywhere=True)
               window.reappear()
              if event=="USER_NAME":
               window.disappear()
               sg.popup(f"USER:{user_entry.get().upper()}",grab_anywhere=True)
               window.reappear()
              if event == "Submit":
               x=values["-IN-"]    
               read_excel_file = pd.read_excel(str(x))
               window.close()
               sg.popup("preparing app.")
               window.close()
               #_________components of software_________
               menu_def=[["Help",["About"]],["User",["USER_NAME"]]] 
              layout = [[sg.MenubarCustom(menu_def,tearoff=False)],
              [sg.Text("BY AHMED RAMADAN",relief="ridge")],
              [sg.Text('Please fill out the following fields:')],
              [sg.Text('ID', size=(15, 1)), sg.Spin(
              [i for i in range(1, 10000001)], initial_value=0, key='ID')],
              [sg.Text('Name', size=(15, 1)), sg.InputText(key='NAME')],
              [sg.Text('Type', size=(15, 1)),sg.Checkbox('Man', key='Man'),
              sg.Checkbox('Woman',     key='-Woman-')],
              [sg.Text('Administration', size=(15, 1)), sg.InputText(key='Administration')],
              [sg.Text('Occupation', size=(15, 1)), sg.InputText(key='Occupation')],
              [sg.Text('Data of Birth', size=(15, 1)), sg.InputText(key='Data of Birth')],
              [sg.Text('Email', size=(15, 1)), sg.InputText(key='Email')],
              [sg.Text('phone number', size=(15, 1)), sg.InputText(key="PHONE NUMBER")],
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
                   default_element_size=(100, 60),
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
               quit()  
               break
              if values['NAME']=="":
                sg.popup("PLEASE ENTER INFORMATION")
                continue
              if values['ID']=="":
                sg.popup("PLEASE ENTER INFORMATION")
                continue
              if values['PHONE NUMBER']=="":
                sg.popup("PLEASE ENTER INFORMATION")
                continue
              if event == 'Clear':
               clear_input()
               sg.popup("data cleared")
              if event=="About":
               window.disappear()
               sg.popup("Version 2.0","Access Excel File..","BY_AHMED_RAMADAN",grab_anywhere=True)
               window.reappear() 
              if event=="USER_NAME":
               window.disappear()
               sg.popup(f"USER:{user_entry.get().upper()}",grab_anywhere=True)
               window.reappear()
              if event == 'Submit':
               new_record = pd.DataFrame(values, index=[0])
               read_excel_file = pd.concat([read_excel_file, new_record], ignore_index=True)
               read_excel_file.to_excel(x, index=False)
               sg.popup('Data inserted!!')
               clear_input()
             window.close()
               #_________check conditions one_________
           elif user_entry1.get()=="":
             sg.popup("Enter User_Name")  
           elif user_entry1.get()!=user_entry.get():
             sg.popup("Enter Correct User_Name:") 
           elif pass_entry1.get()=="":
             sg.popup("Enter Password") 
           elif pass_entry1.get()!="u19":
             sg.popup("Enter Correct Password:") 
           elif id_entry1.get()=="":
             sg.popup("Enter ID") 
           elif id_entry1.get()!=pass_entry.get():
             sg.popup("Enter Correct ID:") 
           else:   
            sg.popup("Enter Correct Information!!")
         else:
          sg.popup("Your Password Not Found In DataBase!!")
           #______check conditions two________ 
#////////////////////////////////////////////////////////////////////////////////////////////////
#_______signup or login form________
root = tk.Tk() 
root.geometry("505x135+500+300")#>>> first window to check you are user or not??
root.iconbitmap('among.ico')
root.title('Signup & Login_Form')
lbl=Label(root, text="Note:If you want to signup please use specific name..",relief="ridge", fg='black', font=(16))
lbl.place(x=0, y=100)
lbl1=Label(root,text=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>").place(x=240,y=40)
lbl3=Label(root,text="hello user:)",font="Times 20 italic bold").place(x=240,y=11)
lbl2=Label(root,text=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>").place(x=240,y=0)
user_label = Label(root, text = 'Enter Username:',fg='black') 
user_entry = Entry(root) 
pass_label = Label(root, text = 'Enter Password:',fg='black') 
pass_entry = Entry(root,show='*')
id_label=Label(root,text="Enter ID:",fg='black')
id_entry=Entry(root,show="*")
id_label.grid(row=2, column=0)  
id_entry.grid(row=2, column=1)
user_label.grid(row=0, column=0)  
user_entry.grid(row=0, column=1)  
pass_label.grid(row=1, column=0)  
pass_entry.grid(row=1, column=1)  
#____create buttons__________    
Button ( root , text="Signup" , fg='black' ,activebackground='green',command = lambda : check_signup()).place(x=70, y=70)#>>signup button
Button ( root , text="Login" , fg='black' ,activebackground='blue',command = lambda : login()).place(x=130, y=70)#>>>login button
Button(root, text="Quit",bg='red', fg='black' ,command=quit,activebackground='red',width=6).place(x=190, y=70)#>>>quit button
#////////////////////////////////////////////////
def check_signup():#>>> function to search about your id in database???
  #____check if your id found in database or not_____ 
 if user_entry.get()!="" and pass_entry.get()!="" and id_entry.get()!="":
        data=cr.execute(f'''select ID,user_name from accounts where ID="{id_entry.get()}" ''').fetchone()#>> to check about your id in database...
        if data==None:#>>if not found the program can create a new account for you...
         data=cr.execute(f'''insert into accounts (ID,user_name,password) values("{id_entry.get()}","{user_entry.get()}","{pass_entry.get()}")''')
         sg.popup(f"{user_entry.get().upper()} Your Account Created Successfully Enjoy..")
         db.commit()
        elif data!=None:#>>> if id founded
          sg.popup("This Account Already Founded in Database") 
 elif user_entry.get()=="" and pass_entry.get()=="" and id_entry.get()=="":#>>some conditions to check if you fill the empty places or not//
     sg.popup("Please Man Fill The Following Fields!!")
 elif user_entry.get()=="":
     sg.popup("Enter user_Name Please!!")
 elif pass_entry.get()=="":
     sg.popup("Enter Password Please!!")
 elif id_entry.get()=="":
     sg.popup("Enter ID Please!!")      
          
root.mainloop()
#________Ending Of The Program____________ 