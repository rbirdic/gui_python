# -*- coding: utf-8 -*-
try:
  import Tkinter  as tk            # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
import tkFont
# using grid
# +------+-------------+
# | btn1 |    btn2     |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+
def rounded_rect(canvas, x, y, w, h, c):
    canvas.create_arc(x,   y,   x+2*c,   y+2*c,   start= 90, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y+h-2*c, x+w, y+h, start=270, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y,   x+w, y+2*c,   start=  0, extent=90, style="arc")
    canvas.create_arc(x,   y+h-2*c, x+2*c,   y+h, start=180, extent=90, style="arc")
    canvas.create_line(x+c, y,   x+w-c, y    )
    canvas.create_line(x+c, y+h, x+w-c, y+h  )
    canvas.create_line(x,   y+c, x,     y+h-c)
    canvas.create_line(x+w, y+c, x+w,   y+h-c)

def callback1():
    print "Izabrali ste Espresso!"
def callback2():
    print "Izabrali ste Espresso sa mlekom!"
def callback3():
    print "Izabrali ste Nes sa šlagom!"
def callback4():
    print "Izabrali ste Čaj od nane!"
def callback5():
    progress.step(20)
def callback6():
    print "Izabrali ste Čaj od nane!"      
root = tk.Tk()


# tkFont.BOLD == 'bold'
helv36 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
photo1 = tk.PhotoImage(file="rsz_download.gif")
photo2 = tk.PhotoImage(file="rsz_latteart.gif")
photo3 = tk.PhotoImage(file="rsz_exps.gif")
photo4 = tk.PhotoImage(file="rsz_tea-png-file.gif")


btn1 = tk.Button(text='Espresso', compound=tk.LEFT, image=photo1, font=helv36, borderwidth=7, command=callback1)
progress = ttk.Progressbar(orient=tk.HORIZONTAL,length=100,  mode='determinate')
btn3 = tk.Button(text='Nes sa šlagom', compound=tk.LEFT, image=photo3, font=helv36, borderwidth=7, command=callback3)
btn4 = tk.Button(text='Čaj od nane', compound=tk.LEFT, image=photo4, font=helv36, borderwidth=7, command=callback4, background='white')
btn5 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
btn6 = tk.Button(text='Espresso', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
btn7 = tk.Button(text='Espresso sa mlekom', compound=tk.LEFT, image=photo2, font=helv36, command=callback4, borderwidth=7)
btn8 = tk.Button(text='Nes sa šlagom', compound=tk.LEFT, image=photo3, font=helv36, command=callback4, borderwidth=7)
btn9 = tk.Button(text='btn4', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
btn10 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
btn11 = tk.Button(text='btn4', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
btn12 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36, command=callback4, borderwidth=7)
root.rowconfigure((0,6), weight=1)  # make buttons stretch when
root.columnconfigure((0,1), weight=1)  # when window is resized
volumeUp = tk.Button(height=1, width=5, text='◄◄', borderwidth=10, fg = 'black', bg='light blue', command=callback5).grid(row=0,column=0)
volumeDown =tk.Button(height=1, width=5, text='►', borderwidth=10, fg = 'black', bg='light blue', command=callback5).grid(row=0,column=1)
# tk.Label(root, text="First", font=helv36).grid(row=0, columnspan=2)


progress.grid(row=1, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn3.grid(row=2, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn4.grid(row=3, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn5.grid(row=4, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn6.grid(row=5, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn1.grid(row=6, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn8.grid(row=1, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn9.grid(row=2, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn10.grid(row=3, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn11.grid(row=4, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn12.grid(row=5, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn7.grid(row=6, column=1, columnspan=1, sticky='EWNS', padx=10, pady=10)

root.mainloop() 