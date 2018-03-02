# -*- coding: utf-8 -*-
try:
  import Tkinter  as tk            # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
import tkFont
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pinsInit[11, 13, 15, 35, 37]

GPIO.setup(pinsInit, GPIO.OUT, initial = GPIO.Low)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(11, GPIO.OUT)   # pin 1
# GPIO.setup(13, GPIO.OUT)   # pin 2
# GPIO.setup(15, GPIO.OUT)   # pin 3
# GPIO.setup(, GPIO.OUT)   # pin 4
# GPIO.setup(10, GPIO.OUT)  # pin 5
# GPIO.setup(11, GPIO.OUT)  # pin 6
# GPIO.setup(12, GPIO.OUT)  # pin 7
# GPIO.setup(13, GPIO.OUT)  # pin 8
# GPIO.setup(15, GPIO.OUT)  # pin 9
# GPIO.setup(16, GPIO.OUT)  # pin 10


# GPIO.output(3, False)
# GPIO.output(5, False)
# GPIO.output(7, False)
# GPIO.output(8, False)
# GPIO.output(10, False)
# GPIO.output(11, False)
# GPIO.output(12, False)
# GPIO.output(13, False)
# GPIO.output(15, False)
# GPIO.output(16, False)

##while GPIO.input(3) == 1:
##    print "Izabrali ste kratki espresso11111!"
def callback00():  # 1 & 7 ---- 1 
    print "Izabrali ste kratki espresso!"
    pinsLow[11, 35, 37]
    pinsHigh[13, 15]
    sleep(20)

    # GPIO.output(3, True)
    # GPIO.output(12, True)
    # if GPIO.input(3)==1 :
    #     print "Izabrali ste kratki espresso11111!"

def callback01():   # 2 & 7 ---- 3
    print "Izabrali ste produženi espresso!"
    # GPIO.output(5, True)
    # GPIO.output(12, True)
    pinsLow[11, 13, 35, 37]
    pinsHigh[15]
    sleep(20)

def callback02():   # 3 & 7 ---- 5
    print "Izabrali ste macchiato!"
    # GPIO.output(7, True)
    # GPIO.output(12, True)
    pinsLow[13, 35, 37]
    pinsHigh[11, 15]
    sleep(20)

def callback03():   # 4 & 7 ---- 7
    print "Izabrali ste cappucchino!"
    # GPIO.output(8, True)
    # GPIO.output(12, True)
    pinsLow[15, 37]
    pinsHigh[11, 13, 35]
    sleep(20) 

def callback04():   # 1 & 9 ---- 9
    print "Izabrali ste cappucchino sa čokoladom!"
    # GPIO.output(3, True)
    # GPIO.output(15, True)
    pinsLow[35, 37]
    pinsHigh[11, 13, 15]
    sleep(20)   

def callback05():   # 2 & 9 ---- 11
    print "Izabrali ste Nes espresso!"
    # GPIO.output(5, True)
    # GPIO.output(15, True)
    pinsLow[13, 15, 37]
    pinsHigh[11, 35]
    sleep(20)

def callback06():   # 3 & 9 ---- 13
    print "Izabrali ste Nes macchiato!"
    # GPIO.output(7, True)
    # GPIO.output(15, True)
    pinsLow[11, 13, 15, 37]
    pinsHigh[35]
    sleep(20) 

def callback07():   # 4 & 9 ---- 15
    print "Izabrali ste Nes cappucchino!"
    # GPIO.output(8, True)
    # GPIO.output(15, True)
    pinsLow[11, 15, 37]
    pinsHigh[13, 35]
    sleep(20)

def callback10():   # 1 & 8 ---- 2
    print "Izabrali ste toplu čokoladu!"
    # GPIO.output(3, True)
    # GPIO.output(13, True)
    pinsLow[13, 15, 35, 37]
    pinsHigh[11]
    sleep(20)

def callback11():   # 2 & 8 ---- 4
    print "Izabrali ste jaču čokoladu!"
    # GPIO.output(5, True)
    # GPIO.output(13, True)
    pinsLow[11, 13, 15, 35, 37]
    sleep(20)

def callback12():   # 3 & 8 ---- 6
    print "Izabrali ste čokolada sa mlekom!"
    # GPIO.output(7, True)
    # GPIO.output(13, True)
    pinsLow[11, 15, 35, 37]
    pinsHigh[13]
    sleep(20)

def callback13():   # 4 & 8 ---- 8
    print "Izabrali ste čaj!"
    # GPIO.output(8, True)
    # GPIO.output(13, True)
    pinsLow[15, 35, 37]
    pinsHigh[11, 13]
    sleep(20)

def callback14():   # 1 & 10 ---- 10
    print "Izabrali ste mleko!"
    # GPIO.output(3, True)
    # GPIO.output(16, True)
    pinsLow[37]
    pinsHigh[11, 13, 15, 35]
    sleep(20)

def callback15():   # 2 & 10 ---- 12
    print "Izabrali ste belu kafu!"
    # PIO.output(5, True)
    # GPIO.output(16, True)
    pinsLow[13, 37]
    pinsHigh[11, 15, 35]
    sleep(20)

def callback16():   # 3 & 10 ---- 14
    print "Izabrali ste praznu čašu!"
    # PIO.output(7, True)
    # GPIO.output(16, True)
    pinsLow[11, 13, 37]
    pinsHigh[15, 35]
    sleep(20)

def callback17():   # 4 & 10 ---- 16
    print "Izabrali ste kratki espresso sa čokoladom!"
    # PIO.output(8, True)
    # GPIO.output(16, True)
    pinsLow[11, 37]
    pinsHigh[13, 15, 35]
    sleep(20)

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
root.configure(background="grey")
# root.geometry("400x400") 

drinkTextFont = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)
sugarTextFont = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
photo00 = tk.PhotoImage(file="espresso38.gif")
bckgrndBtn = '#CA9B00'

labelInfoSugar = tk.Label(text="Pre nego što izaberete napitak regulišite količinu šećera sa - / +", font=sugarTextFont, wraplength=400, background="grey" )
labelSugarLevel = tk.Label(textvariable=sugarCounter, font=sugarTextFont, background="grey")
sugarBtnDown = tk.Button(height=1, width=3, text='-', borderwidth=5, font=drinkTextFont, command=callbackSugarDown)
sugarBtnUp = tk.Button(height=1, width=3, text='+', borderwidth=5, font=drinkTextFont, command=callbackSugarUp)
photoLabel = tk.Label(image = photo00)
btn00 = tk.Button(text='Kratki espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback00)
btn01 = tk.Button(text='Produženi espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback01)
btn02 = tk.Button(text='Macchiato', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback02)
btn03 = tk.Button(text='Cappucchino', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback03)
btn04 = tk.Button(text='Cappucchino sa čokoladom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback04)
btn05 = tk.Button(text='Nes espresso', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback05)
btn06 = tk.Button(text='Nes macchiato', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback06)
btn07 = tk.Button(text='Nes cappucchino', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback07)
btn10 = tk.Button(text='Topla čokolada', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback10)
btn11 = tk.Button(text='Jača čokolada', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback11)
btn12 = tk.Button(text='Čokolada sa mlekom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback12)
btn13 = tk.Button(text='Čaj', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback13)
btn14 = tk.Button(text='Mleko', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback14)
btn15 = tk.Button(text='Bela kafa', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback15)
btn16 = tk.Button(text='Prazna čaša', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback16)
btn17 = tk.Button(text='Kratki espresso sa čokoladom', compound=tk.LEFT, background=bckgrndBtn, font=drinkTextFont, borderwidth=7, command=callback17)

root.rowconfigure((0,9), weight=1)  # make buttons stretch when
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

GPIO.cleanup()
root.mainloop()
