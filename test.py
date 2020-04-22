import tkinter as tk
import os

def openfile1() :
    os.startfile('C:\\Users\\silve\\Documents\\Dungreed.v31.01.2019\\Dungreed.exe')
def openfile2() :
    try:
        os.startfile('C:\\Program Files (x86)\\Borderless Gaming\\BorderlessGaming.exe')
    except Exception:
        print('broke')
def openfile3() :
    os.startfile('C:\\Users\\silve\\Documents\\Dungreed.v31.01.2019\\Dungreed.exe')
def openfile4() :
    try:
        os.startfile('C:\\Program Files (x86)\\Borderless Gaming\\BorderlessGaming.exe')
    except Exception:
        print('broke')

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=300)
canvas1.pack()

label1 = tk.Label(root, text='Silver Launcher')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)

button1 = tk.Button(root, text=' Print hello ', command=openfile1, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 100, window=button1)

button2 = tk.Button(root, text=' Button Duex ', command=openfile2, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 150, window=button2)

button3 = tk.Button(root, text='Exit Application', command=openfile3, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 200, window=button3)

button4 = tk.Button(root, text='Button 4', command=openfile4, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 250, window=button4)

root.mainloop()
