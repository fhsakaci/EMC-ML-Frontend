from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import tkinter

class graph():
    def __init__(self):
        pass

    def figure(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    
    def draw(self,window):
        self.canvas = FigureCanvasTkAgg(self.fig, master=window)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    def toolbar(self,window):
        toolbar = NavigationToolbar2Tk(self.canvas, window)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)