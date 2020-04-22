import tkinter as tk
import os


def openfile1():
    try:
        os.startfile(
            '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\VALORANT.lnk"')
        os._exit(0)
    except Exception:
        print('of1')


def openfile2():
    try:
        os.startfile(
            'C:\\Program Files (x86)\\Borderless Gaming\\BorderlessGaming.exe')
        os._exit(0)
    except Exception:
        print('of2')


def openfile3():
    try:
        os.startfile(
            "C:\\Program Files (x86)\\Wizard of Legend Thundering Keep\\WizardOfLegend.exe")
        os._exit(0)
    except Exception:
        print('of3')


def openfile4():
    try:
        os.startfile(
            'C:\\Users\\silve\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\BakkesMod.exe')
        os._exit(0)
    except Exception:
        print('of4')


def openfile5():
    try:
        os.startfile("C:\\Users\\silve\\AppData\\Local\\Minion\\Minion.exe")
        os._exit(0)
    except Exception:
        print('of5')


def openfile6():
    try:
        os.startfile(
            "C:\\Users\\silve\\Downloads\\RimWorld.v1.0.2408\\RimWorldWin64.exe")
        os._exit(0)
    except Exception:
        print('of6')


def openfile7():
    try:
        os.startfile("C:\\Program Files\\TruckersMP Launcher\\Launcher.exe")
        os._exit(0)
    except Exception:
        print('of7')


def openfile8():
    try:
        os.startfile("C:\\Program Files\\poe-overlay\\poe-overlay.exe")
        os._exit(0)
    except Exception:
        print('of8')


def openfile9():
    try:
        os.startfile("C:\\Users\\silve\\Documents\\Batch\\silverbot.vbs")
        os._exit(0)
    except Exception:
        print('of9')


root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=300, bg='#1c8bbd')
canvas1.pack()

label1 = tk.Label(root, text='')
label1.config(font=('Arial', 20), bg='#1c8bbd')
canvas1.create_window(400, 25, window=label1)

button1 = tk.Button(root, width=15, height=1, text=' Valorant ',
                    command=openfile1, bg='#2b6eff', font=('Arial', 11, 'bold', ))
canvas1.create_window(225, 75, window=button1)

button2 = tk.Button(root, width=15, height=1, text=' Borderless gaming ',
                    command=openfile2, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(225, 125, window=button2)

button3 = tk.Button(root, width=15, height=1, text='Wizard of Legend',
                    command=openfile3, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(225, 175, window=button3)

button4 = tk.Button(root, width=15, height=1, text='BakkesMod',
                    command=openfile4, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(575, 75, window=button4)

button5 = tk.Button(root, width=15, height=1, text='MMO',
                    command=openfile5, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(575, 125, window=button5)

button6 = tk.Button(root, width=15, height=1, text='Rimworld',
                    command=openfile6, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(575, 175, window=button6)

button7 = tk.Button(root, width=15, height=1, text='TruckersMP',
                    command=openfile7, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 125, window=button7)

button8 = tk.Button(root, width=15, height=1, text='Poe Overlay',
                    command=openfile8, bg='#2b6eff', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 175, window=button8)

button9 = tk.Button(root, width=15, height=1, text='SilverBot',
                    command=openfile9, bg='#2b6eff', font=('Ariel', 11, 'bold'))
canvas1.create_window(400, 75, window=button9)
root.mainloop()
