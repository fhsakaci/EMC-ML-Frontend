import tkinter

from tkinter.constants import *

class widgets():
    def __init__(self):
        pass

    def createButton(self,tk,text,x,y,command=None,width=None,height=None):
        button = tkinter.Button(tk,text=text,command=command,width=width,height=height)
        button.place(x=x,y=y)
        return button

    def createLabel(self,tk,text,x,y):
        label = tkinter.Label(tk, text=text)
        label.place(x=x,y=y)
        return label

    def createFrame(self,tk,x,y,width,height):
        frame=tkinter.Frame(tk,width=width,height=height)
        frame.place(x=x,y=y)
        return frame
