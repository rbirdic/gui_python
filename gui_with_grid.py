# -*- coding: utf-8 -*-
import Tkinter as tk
import tkFont
# using grid
# +------+-------------+
# | btn1 |    btn2     |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+
def callback1():
    print "Izabrali ste Espresso!"
def callback2():
    print "Izabrali ste Espresso sa mlekom!"
def callback3():
    print "Izabrali ste Nes sa šlagom!"
def callback4():
    print "Izabrali ste Čaj od nane!"        
root = tk.Tk()
# tkFont.BOLD == 'bold'
helv36 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
photo1 = tk.PhotoImage(file="rsz_download.gif")
photo2 = tk.PhotoImage(file="rsz_latteart.gif")
photo3 = tk.PhotoImage(file="rsz_exps.gif")
photo4 = tk.PhotoImage(file="rsz_tea-png-file.gif")

btn1 = tk.Button(text='Espresso', compound=tk.LEFT, image=photo1, font=helv36, command=callback1)
btn2 = tk.Button(text='Espresso sa mlekom', compound=tk.LEFT, image=photo2, font=helv36, command=callback2)
btn3 = tk.Button(text='Nes sa šlagom', compound=tk.LEFT, image=photo3, font=helv36, command=callback3)
btn4 = tk.Button(text='Čaj od nane', compound=tk.LEFT, image=photo4, font=helv36, command=callback4, background='white')
btn5 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36)
btn6 = tk.Button(text='Espresso', compound=tk.LEFT, image=photo1, font=helv36)
btn7 = tk.Button(text='Espresso sa mlekom', compound=tk.LEFT, image=photo2, font=helv36)
btn8 = tk.Button(text='Nes sa šlagom', compound=tk.LEFT, image=photo3, font=helv36)
btn9 = tk.Button(text='btn4', compound=tk.LEFT, image=photo1, font=helv36)
btn10 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36)
btn11 = tk.Button(text='btn4', compound=tk.LEFT, image=photo1, font=helv36)
btn12 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36)
root.rowconfigure((0,1), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized
btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn2.grid(row=1, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn3.grid(row=2, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn4.grid(row=3, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn5.grid(row=4, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn6.grid(row=5, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn7.grid(row=0, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn8.grid(row=1, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn9.grid(row=2, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn10.grid(row=3, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn11.grid(row=4, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn12.grid(row=5, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
root.mainloop() 