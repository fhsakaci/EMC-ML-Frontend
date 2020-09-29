import tkinter
from tkinter.constants import *
from widgets import widgets
import numpy as np
from graph import graph


tk = tkinter.Tk()

tk.title("EMC Sonucu Tahmin Sistemi")
tk.geometry("1080x600")
tk.resizable(False,False)
tk.config(bg="gray62")
Widgets=widgets()

graph_frame=Widgets.createFrame(tk,x=50,y=50,width=600,height=500)
graph_frame.config(bg="gray42")

panel_frame=Widgets.createFrame(tk,x=580,y=50,width=470,height=500)
panel_frame.config(bg="gray42")


Graph=graph()
Graph.figure()
Graph.draw(graph_frame)
Graph.toolbar(graph_frame)

draw_button=Widgets.createButton(panel_frame,"Tahmin Et",300,150,width=20,height=1,command=tk.destroy)
draw_button.config(bg="gray62")


exit_button=Widgets.createButton(panel_frame,"Çıkış",300,450,width=20,height=1,command=tk.destroy)
exit_button.config(bg="gray62")

FHS_label=Widgets.createLabel(tk,"Furkan Hasan Sakacı",960,580)
FHS_label.config(bg="gray62")

tk.mainloop()
 