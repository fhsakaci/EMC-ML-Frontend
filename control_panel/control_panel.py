import tkinter as tk
from utils import utils
from control_panel.training import training
from control_panel.testing import testing

class control_panel():
    def __init__(self,window,widgets,machine_learning,graph):
        self.widgets=widgets
        panel_frame=self.createPanel(window)
        Training=training(panel_frame,widgets,machine_learning)
        Testing=testing(panel_frame,widgets,machine_learning,graph)

    def createPanel(self,window):
        panel_frame=self.widgets.createFrame(window,x=580,y=50,width=470,height=500)
        panel_frame.config(bg="gray50")
        return panel_frame
    
    def exit(self):
        pass


