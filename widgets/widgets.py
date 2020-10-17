import tkinter
from utils import utils
from tkinter.constants import *

class widgets():
    def __init__(self,tk):
        self.tk=tk
        self.tk.title("EMC Sonucu Tahmin Sistemi")
        self.tk.geometry("1080x600")
        self.tk.resizable(False,False)
        self.tk.config(bg="light slate gray")
        self.logger = utils.get_logger()

    def createButton(self,tk,text,x,y,command=None,width=None,height=None,anchor=None):
        button = tkinter.Button(tk,text=text,command=command,width=width,height=height)
        button.place(x=x,y=y)
        return button

    def createLabel(self,tk,text,x,y,font=None,anchor=None):
        label = tkinter.Label(tk, text=text,font=font)
        label.place(x=x,y=y,anchor=anchor)
        return label

    def createFrame(self,tk,x,y,width,height,anchor=None):
        frame=tkinter.Frame(tk,width=width,height=height,borderwidth = 5)
        frame.place(x=x,y=y,anchor=anchor)
        return frame

    def createDropdown(self,tk,variable,OptionList,x,y,width=None,height=None,anchor=None):
        dropdown=tkinter.OptionMenu(tk,variable,*OptionList)
        dropdown.config(width=width,height=height)
        dropdown["highlightthickness"]=0
        dropdown.place(x=x,y=y,anchor=anchor)
        return dropdown

     
