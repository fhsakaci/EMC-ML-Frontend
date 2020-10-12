import tkinter

from tkinter.constants import *

class widgets():
    def __init__(self,tk):
        self.tk=tk
        self.tk.title("EMC Sonucu Tahmin Sistemi")
        self.tk.geometry("1080x600")
        self.tk.resizable(False,False)
        self.tk.config(bg="gray62")

    def createButton(self,tk,text,x,y,command=None,width=None,height=None):
        button = tkinter.Button(tk,text=text,command=command,width=width,height=height)
        button.place(x=x,y=y)
        return button

    def createLabel(self,tk,text,x,y,font=None):
        label = tkinter.Label(tk, text=text,font=font)
        label.place(x=x,y=y)
        return label

    def createFrame(self,tk,x,y,width,height):
        frame=tkinter.Frame(tk,width=width,height=height)
        frame.place(x=x,y=y)
        return frame

    def createDropdown(self,tk,variable,OptionList,x,y,width=None,height=None):
        dropdown=tkinter.OptionMenu(tk,variable,*OptionList)
        dropdown.config(width=width,height=height)
        dropdown["highlightthickness"]=0
        dropdown.place(x=x,y=y)
        return dropdown

     
