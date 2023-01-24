import customtkinter as ctk
from time import sleep
from win32api import *
from win32con import *
import pyautogui as pg
from random import randint, random, choice
from tkinter import messagebox
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('rate', 160)

engine.say('привет, спасибо что ты используешь наше программное обеспечение')
engine.runAndWait()

def cmd():
    Beep(350, 430)
    os.system('start cmd')

def off_pc():
    Beep(350, 430)
    Beep(350, 430)
    os.system('shutdown /p')

def yt():
    Beep(350, 430)
    webbrowser.open('https://www.youtube.com/')

def vk():
    Beep(350, 450)
    webbrowser.open('https://www.vk.com/feed')

def paint():
    Beep(350, 450)
    os.system('start mspaint')

def make_password():
    all = 'QWERTYUIOPASDFGHJKLZXCVBNM$'
    all.lower()
    password = choice(all) + choice(all) + choice(all) * 4 + str(randint(1,1000))
    messagebox.showinfo('your pass: ', password)
    
app = ctk.CTk()
app.geometry('840x450')
app.title('Programm Helper')
app.resizable(None, None)
ctk.set_appearance_mode('dark')

cmd_btn = ctk.CTkButton(master=app, text='Открыть cmd', command=cmd, fg_color='#620062', border_color='#490049', border_width=2.5, hover_color='#830083')
shutdown_btn = ctk.CTkButton(master=app, text='Выключить Пк', command=off_pc, fg_color='#620062', border_color='#490049', border_width=2.5, hover_color='#830083')
youtube_btn = ctk.CTkButton(master=app, text='октыть youtube', command=yt, fg_color='#620062', border_color='#490049', border_width=2.5, hover_color='#830083')
password_btn = ctk.CTkButton(master=app, text='Сгенерировать Пароль', command=make_password, fg_color='#620062', border_color='#490049', border_width=2.5, hover_color='#830083')
main_label = ctk.CTkLabel(master=app, text='Windows Helper', text_color='#620069', font=('Arial', 32))
vk_btn = ctk.CTkButton(master=app, text='открыть vk', fg_color='#620069', command=vk, border_color='#490049', border_width=2.5, hover_color='#830083')
text_frame = ctk.CTkTextbox(master=app,fg_color='#3e3e3e', text_color='white', border_width=2.8)
text_frame.insert(0.0, 'Привет, это моя первая gui программа на яп python\n и я очень рад что ты сказал её\n удачи и приятного пользования это мой первый проект\n думаю тебе понравиться)\n Спасибо за внимание!')
paint_btn = ctk.CTkButton(master=app, text='порисовать', fg_color='#620069', command=paint, border_color='#490049', border_width=2.5, hover_color='#830083')

cmd_btn.place(x=100, y=350)
shutdown_btn.place(x=250, y=350)
youtube_btn.place(x=600, y=350)
vk_btn.place(x=400, y=400)
paint_btn.place(x=250, y=400)
password_btn.place(x=420, y=350)
text_frame.place(x=320, y=120)
main_label.place(x=300, y=25)

app.mainloop()