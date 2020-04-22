import os

def openfile1() :
    try:
        os.startfile('C:\\Users\\silve\\Documents\\Dungreed.v31.01.2019\\Dungreed.exe')
    except Exception:
        print('broken')

def openfile2() :
    try:
        os.startfile('C:\\Program Files (x86)\\Borderless Gaming\\BorderlessGaming.exe')
    except Exception:
        print('broken')

def openfile3() :
    try:
        os.startfile("C:\\Program Files (x86)\\Wizard of Legend Thundering Keep\\WizardOfLegend.exe")
    except Exception:
        print('broken')


answer = input('What Game? ')
if "dungreed" == answer.casefold():
    print('Opening...')
    openfile1()

if "bg" == answer.casefold():
    print('Opening...')
    openfile2()

if "wol" == answer.casefold():
    print('Opening...')
    openfile3()

