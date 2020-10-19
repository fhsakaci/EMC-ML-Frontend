import tkinter
from tkinter.constants import *
import numpy as np
from widgets.widgets import widgets
from graph.graph import graph
from control_panel.control_panel import control_panel
from machine_learning.machine_learning import machine_learning
from utils import utils
import signal
import os


def sigint_handler(signum, frame):
    if signum == signal.SIGINT:
        logger.error( 'Interrupt signal caught, process exiting...' )
    if signum == signal.SIGUSR1:
        logger.error( 'Gasmon server is exited, process exiting...' )
    os.kill( os.getpid(), signal.SIGKILL )


# configure logging
logger = utils.set_logger( __name__, __file__ )

# bind signal handler to handle keyboard interrupts etc.
logger.info( 'Setting a signal for EMC Learning System' )
signal.signal( signal.SIGINT, sigint_handler )

window = tkinter.Tk()
Widgets=widgets(window)
Machine_Learning=machine_learning()
Graph=graph(window,Widgets)
Control=control_panel(window,Widgets,Machine_Learning,Graph)



FHS_label=Widgets.createLabel(window,"Furkan Hasan Sakacı",900,580)
FHS_label.config(bg="light slate gray")

window.mainloop()
 