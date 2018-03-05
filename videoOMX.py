import os,sys
from Tkinter  import *
from tkFileDialog import askopenfilename 
##filename=str(raw_input('@Enter a file name :'))
##os.system('omxplayer -o hdmi /home/pi/Desktop/1.mp4')
class MediaPlayer():
    def __init__(self,root):
        self.playbutton=Button(root,text='Play',command=self.play).pack()
        self.stopbutton=Button(root,text='stop',command=self.stop).pack()
    def play(self):
        filename=str(askopenfilename())
        try:
            os.system('omxplayer -o hdmi %s'%filename)
        except:
            print ("File OPening Problem")
    def stop (self):
        sys.exit()
root=Tk()
cd=MediaPlayer(root)
root.geometry('300x200')

root.mainloop()