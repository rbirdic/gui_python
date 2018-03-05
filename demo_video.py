import sys
import os

if sys.version_info[0] < 3:
    import Tkinter as tkinter
else:
    import tkinter

from tkFileDialog import askopenfilename 
##filename=str(raw_input('@Enter a file name :'))
##os.system('omxplayer -o hdmi /home/pi/Desktop/1.mp4')
class MediaPlayer():
    def __init__(self,root):
        filename='/home/pi/Desktop/demo_final/gui_python/nescafe1.mp4'
        while 1:
            os.system('omxplayer -o hdmi --win "45 45 960 1035" %s'%filename)
root=tkinter.Tk()
cd=MediaPlayer(root)
root.geometry('300x200')

root.mainloop()