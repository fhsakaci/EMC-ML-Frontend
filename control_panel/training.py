from utils import utils
import tkinter as tk
from control_panel import control_panel
from datetime import datetime

class training():
    def __init__(self,window,widgets,machine_learning):
        self.machine_learning=machine_learning
        self.widgets=widgets
        self.logger = utils.get_logger()

        training_frame=self.widgets.createFrame(window,x=230,y=120,width=400,height=200,anchor="center")
        training_frame.config(bg="gray70")

        title1_label=self.widgets.createLabel(training_frame,"Yeni Eğitim Modeli Üret",200,20,font=("Times New Roman", 16),anchor="center")
        title1_label.config(bg="gray70")
        OptionList = ["RE102","CE102"] 
        self.variable = tk.StringVar(training_frame)
        self.variable.set(OptionList[0])

        test_type=self.widgets.createDropdown(training_frame,self.variable,OptionList,100,50,width=18,height=1)
        test_type.config(bg="gray60") 

        file_button=self.widgets.createButton(training_frame,"Dosya Seç",100,100,width=20,height=1,command=self.browseFiles)
        file_button.config(bg="gray60")


        draw_button=self.widgets.createButton(training_frame,"Model Oluştur",100,150,width=20,height=1,command=self.train)
        draw_button.config(bg="gray60") 


    
    def train(self):
        savePath=self.saveFolderLocation()
        model=self.machine_learning.train(self.filename)
        model.save(savePath)
    
    def saveFolderLocation(self): 
        directory = tk.filedialog.askdirectory (initialdir = "/",title = "Dosya Seç")
        filename=str(int(datetime.now().timestamp()))
        testType=self.variable.get()
        savePath=directory+"/"+testType+"-"+filename
        return savePath


    def browseFiles(self): 
        self.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Dosya Seç", 
            filetypes = (("Excel files", "*.csv*"),("all files",     "*.*")))

    def exit(self):
        pass