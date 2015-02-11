__author__ = 'hc'

#This opens a file chooser

from Tkinter import Tk
from tkFileDialog import askopenfilename

def fileChooser(title):
    Tk().withdraw() #Prevent window from appearing
    filename = askopenfilename(title=title) # show an "Open" dialog box and return the path to the selected file
    Tk().quit()
    Tk().destroy()
    return filename