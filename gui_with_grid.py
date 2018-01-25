import Tkinter as tk
import tkFont
# using grid
# +------+-------------+
# | btn1 |    btn2     |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+
def callback():
    print "clicked!"
root = tk.Tk()
# tkFont.BOLD == 'bold'
helv36 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
photo1 = tk.PhotoImage(file="rsz_download.gif")
photo2 = tk.PhotoImage(file="rsz_latteart.gif")
photo3 = tk.PhotoImage(file="rsz_exps.gif")


btn1 = tk.Button(text='btn1', compound=tk.LEFT, image=photo1, font=helv36, command=callback)
btn2 = tk.Button(text='btn2', compound=tk.LEFT, image=photo2, font=helv36)
btn3 = tk.Button(text='btn3', compound=tk.LEFT, image=photo3, font=helv36)
btn4 = tk.Button(text='btn4', compound=tk.LEFT, image=photo1, font=helv36)
btn5 = tk.Button(text='btn5', compound=tk.LEFT, image=photo1, font=helv36)
root.rowconfigure((0,6), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized
btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn2.grid(row=1, column=0, columnspan=2, sticky='EWNS', padx=10, pady=10)
btn3.grid(row=2, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn4.grid(row=3, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
btn5.grid(row=4, column=0, columnspan=1, sticky='EWNS', padx=10, pady=10)
root.mainloop() 