from utils import utils
import tkinter as tk

class testing():
    def __init__(self,window,widgets,machine_learning,graph):
        self.machine_learning=machine_learning
        self.graph=graph
        self.widgets=widgets
        self.logger = utils.get_logger()

        test_frame=self.widgets.createFrame(window,x=230,y=350,width=400,height=250,anchor="center")
        test_frame.config(bg="gray70")

        title2_label=self.widgets.createLabel(test_frame,"Emisyon Tahmini Yap",190,20,font=("Times New Roman", 16),anchor="center")
        title2_label.config(bg="gray70")

        OptionList = ["RE102","CE102"] 
        variable = tk.StringVar(test_frame)
        variable.set(OptionList[0])

        parameter_button=self.widgets.createButton(test_frame,"Parametreleri Gir",100,100,width=20,height=1,command=self.exit)
        parameter_button.config(bg="gray60")

        
        test_type=self.widgets.createDropdown(test_frame,variable,OptionList,100,50,width=18,height=1)
        test_type.config(bg="gray60") 

        limit_button=self.widgets.createButton(test_frame,"Model Seç",100,150,width=20,height=1,command=self.loadBrowseFiles)
        limit_button.config(bg="gray60")

        predict_button=self.widgets.createButton(test_frame,"Ölçüm Yap",100,200,width=20,height=1,command=self.loadBrowseFiles)
        predict_button.config(bg="gray60")

    def predict(self,filename):
        response=self.machine_learning.predict(filename)
        self.graph.draw(response)

    def BrowseFiles(self): 
        self.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Model Seç", 
            filetypes = (("Excel files", "*.csv*"),("all files",     "*.*")))
        
    def limitControl(self):
        pass

    
    def exit(self):
        pass
    
