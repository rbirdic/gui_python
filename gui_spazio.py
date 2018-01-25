# -*- coding: utf-8 -*-
# create a Tkinter button with an image and optional text
# note that Tkinter reads only GIF and PGM/PPM images
# for other image file types use the Python Image Library (PIL)
# replace the line photo1 = tk.PhotoImage(file="Press1.gif")
# with these three lines ...
#
# from PIL import Image, ImageTk
# image1 = Image.open("Press1.jpg")
# photo1 = ImageTk.PhotoImage(image1)
#
# tested with Python24     vegaseat     23dec2006
# -*- coding: utf-8 -*- 
import Tkinter as tk
import tkFont
button_flag = True
def click():
    """
    respond to the button click
    """
    global button_flag
    # toggle button colors as a test
    if button_flag:
        button1.config(bg="white")
        button_flag = False
    else:
        button1.config(bg="green")
        button_flag = True
root = tk.Tk()
times = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD)
# create a frame and pack it
frame1 = tk.Frame(root, width=2000, height=2000)
frame1.pack(fill=None, expand=False)
# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="rsz_latteart.gif")
photo2 = tk.PhotoImage(file="rsz_exps.gif")
# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.LEFT, width=250, height=150, image=photo1,
    text="Produženi espresso", fg='black', font=times, bg="#C0C0C0", command=click)
button1.pack(side=tk.TOP, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1
button2 = tk.Button(frame1, compound=tk.LEFT, width=250, height=150, image=photo2,
    text="Produženi espresso sa mlekom", fg='black', wraplength=150, font=times, bg="#C0C0C0", command=click)
button2.pack(padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button2.image = photo2
# start the event loop
root.mainloop()