# -*- coding: utf-8 -*-
try:
  import Tkinter  as tk            # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
import tkFont
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pinsInit = [11, 13, 15, 35]

GPIO.setup(pinsInit, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(37, True)

def callback00():  # 1 & 7 ---- 1 
    print "Izabrali ste kratki espresso!"
    pinsLow = [11, 35, 37]
    pinsHigh = [13, 15]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback01():   # 2 & 7 ---- 3
    print "Izabrali ste produženi espresso!"

    pinsLow = [11, 13, 35, 37]
    pinsHigh = [15]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback02():   # 3 & 7 ---- 5
    print "Izabrali ste macchiato!"

    pinsLow = [13, 35, 37]
    pinsHigh = [11, 15]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback03():   # 4 & 7 ---- 7
    print "Izabrali ste cappucchino!"

    pinsLow = [35, 37]
    pinsHigh = [11, 13, 15]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True) 

def callback04():   # 1 & 9 ---- 9
    print "Izabrali ste cappucchino sa čokoladom!"

    pinsLow = [15, 37]
    pinsHigh = [11, 13, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)  

def callback05():   # 2 & 9 ---- 11
    print "Izabrali ste Nes espresso!"

    pinsLow = [13, 15, 37]
    pinsHigh = [11, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback06():   # 3 & 9 ---- 13
    print "Izabrali ste Nes macchiato!"

    pinsLow = [11, 13, 15, 37]
    pinsHigh = [35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback07():   # 4 & 9 ---- 15
    print "Izabrali ste Nes cappucchino!"

    pinsLow = [11, 15, 37]
    pinsHigh = [13, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback10():   # 1 & 8 ---- 2
    print "Izabrali ste toplu čokoladu!"

    pinsLow = [13, 15, 35, 37]
    pinsHigh = [11]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback11():   # 2 & 8 ---- 4
    print "Izabrali ste jaču čokoladu!"

    pinsLow = [11, 13, 15, 35, 37]
    GPIO.output(pinsLow, False)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback12():   # 3 & 8 ---- 6
    print "Izabrali ste čokolada sa mlekom!"

    pinsLow = [11, 15, 35, 37]
    pinsHigh = [13]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback13():   # 4 & 8 ---- 8
    print "Izabrali ste čaj!"

    pinsLow = [15, 35, 37]
    pinsHigh = [11, 13]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback14():   # 1 & 10 ---- 10
    print "Izabrali ste mleko!"

    pinsLow = [37]
    pinsHigh = [11, 13, 15, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback15():   # 2 & 10 ---- 12
    print "Izabrali ste belu kafu!"

    pinsLow = [13, 37]
    pinsHigh = [11, 15, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback16():   # 3 & 10 ---- 14
    print "Izabrali ste praznu čašu!"

    pinsLow = [11, 13, 37]
    pinsHigh = [15, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callback17():   # 4 & 10 ---- 16
    print "Izabrali ste kratki espresso sa čokoladom!"

    pinsLow = [11, 37]
    pinsHigh = [13, 15, 35]
    GPIO.output(pinsLow, False)
    GPIO.output(pinsHigh, True)
    time.sleep(0.5)
    GPIO.output(37, True)

def callbackSugarUp():  # 1 & 5
    if (sugarCounter.get() < 5) and (sugarCounter.get() >= 0):
        sugarCounter.set(sugarCounter.get() + 1)
        # labelSugarLevel(textvariable=sugarCounter).pack()
def callbackSugarDown(): # 1 & 6
    if (sugarCounter.get() <= 5) and (sugarCounter.get() > 0):
        sugarCounter.set(sugarCounter.get() - 1)
        # labelSugarLevel(textvariable=sugarCounter).pack()            
root = tk.Tk()
sugarCounter = tk.IntVar()
sugarCounter.set(2)
root.resizable(width=False, height=False)
root.geometry("960x1080")
root.configure(background="grey")

drinkTextFont = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
sugarTextFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
photo00 = tk.PhotoImage(file="espresso38.gif")
bckgrndBtn = '#CA9B00'

labelInfoSugar = tk.Label(text="Pre nego što izaberete napitak regulišite količinu šećera sa - / +", font=sugarTextFont, wraplength=400, background="grey" )
labelSugarLevel = tk.Label(textvariable=sugarCounter, font=sugarTextFont, background="grey")
sugarBtnDown = tk.Button(height=1, width=4, text='-', borderwidth=5, font=drinkTextFont, command=callbackSugarDown)
sugarBtnUp = tk.Button(height=1, width=4, text='+', borderwidth=5, font=drinkTextFont, command=callbackSugarUp)
photoLabel = tk.Label(image = photo00)
btn00 = tk.Button(text='Kratki espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback00,  width = 1, height = 3)
btn01 = tk.Button(text='Produženi espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback01,  width = 1, height = 3)
btn02 = tk.Button(text='Macchiato', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback02,  width = 1, height = 3)
btn03 = tk.Button(text='Cappucchino', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback03,  width = 1, height = 3)
btn04 = tk.Button(text='Cappucchino sa čokoladom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback04,  width = 1, height = 3)
btn05 = tk.Button(text='Nes espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback05,  width = 1, height = 3)
btn06 = tk.Button(text='Nes macchiato', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback06,  width = 1, height = 3)
btn07 = tk.Button(text='Nes cappucchino', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback07,  width = 1, height = 3)
btn10 = tk.Button(text='Topla čokolada', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback10,  width = 1, height = 3)
btn11 = tk.Button(text='Jača čokolada', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback11,  width = 1, height = 3)
btn12 = tk.Button(text='Čokolada sa mlekom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback12,  width = 1, height = 3)
btn13 = tk.Button(text='Čaj', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback13,  width = 1, height = 3)
btn14 = tk.Button(text='Mleko', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback14,  width = 1, height = 3)
btn15 = tk.Button(text='Bela kafa', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback15,  width = 1, height = 3)
btn16 = tk.Button(text='Prazna čaša', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback16,  width = 1, height = 3)
btn17 = tk.Button(text='Kratki espresso sa čokoladom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback17, width = 1, height = 3)

root.rowconfigure((0,15), weight=1)  # make buttons stretch when
root.columnconfigure((0,4), weight=1)  # when window is resized

labelInfoSugar.grid(row=0, column=0, columnspan=5)
labelSugarLevel.grid(row=1, column=2, columnspan=1)
sugarBtnDown.grid(row=1, column=0, columnspan=2)
sugarBtnUp.grid(row=1, column=4, columnspan=2)
# photoLabel.grid(row=2, column=0, columnspan=1)
btn00.grid(row=2, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn01.grid(row=3, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn02.grid(row=4, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn03.grid(row=5, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn04.grid(row=6, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn05.grid(row=7, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn06.grid(row=8, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn07.grid(row=9, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn10.grid(row=2, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn11.grid(row=3, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn12.grid(row=4, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn13.grid(row=5, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn14.grid(row=6, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn15.grid(row=7, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn16.grid(row=8, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn17.grid(row=9, column=4, columnspan=1, sticky='EWNS', padx=10, pady=10)

#GPIO.cleanup()
root.mainloop()
