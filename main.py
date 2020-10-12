import tkinter
from tkinter.constants import *
from widgets import widgets
import numpy as np
from graph import graph
from control_panel import control_panel
from machine_learning import machine_learning

window = tkinter.Tk()
Widgets=widgets(window)
Control=control_panel(window,Widgets,machine_learning)
Graph=graph(window,Widgets)


FHS_label=Widgets.createLabel(window,"Furkan Hasan Sakacı",960,580)
FHS_label.config(bg="gray62")

window.mainloop()
 