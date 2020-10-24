from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import tkinter
from utils import utils

class graph():
    def __init__(self,window,widgets):
        self.widgets=widgets
        self.panel_frame=self.createPanel(window)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_frame)  # A tk.DrawingArea.
        self.figure()
        self.draw()
        self.toolbar()
        self.logger = utils.get_logger()
       

    def createPanel(self,window):
        graph_frame=self.widgets.createFrame(window,x=50,y=50,width=500,height=400)
        graph_frame.config(bg="gray42")
        return graph_frame

    def figure(self):
        f = np.arange(150000, 1000000, 1000)
        self.graph=self.fig.add_subplot(111)
        

    def draw(self):
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    def toolbar(self):
        toolbar = NavigationToolbar2Tk(self.canvas, self.panel_frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def draw_fig(self,data):
        data=data[0,:,0]
        print(data)
        f = np.arange(150000, 1000000, 100)
        self.line=self.graph.plot(f, data)
        print(self.line)
        
