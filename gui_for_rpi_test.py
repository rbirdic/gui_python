# -*- coding: utf-8 -*-
try:
  import Tkinter  as tk            # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
import tkFont
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.IN)
#GPIO.setup(11, GPIO.OUT)
#GPIO.input(11, FALSE)



def callback00():
    print "Izabrali ste kratki espresso!"
def callback01():
    print "Izabrali ste produženi espresso!"
def callback02():
    print "Izabrali ste macchiato!"
def callback03():
    print "Izabrali ste cappucchino!"
def callback04():
    print "Izabrali ste cappucchino sa čokoladom!"
def callback05():
    print "Izabrali ste Nes espresso!"
def callback06():
    print "Izabrali ste Nes macchiato!"
def callback07():
    print "Izabrali ste Nes cappucchino!"
def callback10():
    print "Izabrali ste toplu čokoladu!"
def callback11():
    print "Izabrali ste jaču čokoladu!"
def callback12():
    print "Izabrali ste čokolada sa mlekom!"
def callback13():
    print "Izabrali ste čaj!"
def callback14():
    print "Izabrali ste mleko!"
def callback15():
    print "Izabrali ste belu kafu!"
def callback16():
    print "Izabrali ste praznu čašu!"
def callback17():
    print "Izabrali ste kratki espresso sa čokoladom!"
def callbackSugarUp():
    if (sugarCounter.get() < 5) and (sugarCounter.get() >= 0):
        sugarCounter.set(sugarCounter.get() + 1)
        # labelSugarLevel(textvariable=sugarCounter).pack()
def callbackSugarDown():
    if (sugarCounter.get() <= 5) and (sugarCounter.get() > 0):
        sugarCounter.set(sugarCounter.get() - 1)
        # labelSugarLevel(textvariable=sugarCounter).pack()            
root = tk.Tk()
sugarCounter = tk.IntVar()
root.resizable(width=False, height=False)
root.configure(background="grey")

drinkTextFont = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)
sugarTextFont = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
photo00 = tk.PhotoImage(file="espresso38.gif")
bckgrndBtn = '#CA9B00'

labelInfoSugar = tk.Label(text="Pre nego što izaberete napitak regulišite količinu šećera sa - / +", font=sugarTextFont, wraplength=400, background="grey" )
labelSugarLevel = tk.Label(textvariable=sugarCounter, font=sugarTextFont)
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
sugarBtnDown.grid(row=1, column=0, columnspan=1)
sugarBtnUp.grid(row=1, column=4, columnspan=1)
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
