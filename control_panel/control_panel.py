import tkinter as tk
from utils import utils

class control_panel():
    def __init__(self,window,widgets,machine_learning):
        self.window=window
        self.widgets=widgets
        self.panel_frame=self.createPanel(window)
        self.createPanelContents()
        self.machine_learning=machine_learning
        self.logger = utils.get_logger()

    def createPanel(self,window):
        panel_frame=self.widgets.createFrame(window,x=580,y=50,width=470,height=500)
        panel_frame.config(bg="gray50")
        return panel_frame
    
    def createPanelContents(self):
        self.trainingPanel()
        self.testPanel()
        

    def trainingPanel(self):
        training_frame=self.widgets.createFrame(self.panel_frame,x=230,y=120,width=400,height=200,anchor="center")
        training_frame.config(bg="gray70")

        title1_label=self.widgets.createLabel(training_frame,"Yeni Eğitim Modeli Üret",200,20,font=("Times New Roman", 16),anchor="center")
        title1_label.config(bg="gray70")
        OptionList = ["RE102","CE102"] 
        variable = tk.StringVar(training_frame)
        variable.set(OptionList[0])

        test_type=self.widgets.createDropdown(training_frame,variable,OptionList,100,50,width=18,height=1)
        test_type.config(bg="gray60") 

        file_button=self.widgets.createButton(training_frame,"Dosya Seç",100,100,width=20,height=1,command=self.browseFiles)
        file_button.config(bg="gray60")


        draw_button=self.widgets.createButton(training_frame,"Model Oluştur",100,150,width=20,height=1,command=self.train)
        draw_button.config(bg="gray60") 

    def testPanel(self):
        test_frame=self.widgets.createFrame(self.panel_frame,x=230,y=350,width=400,height=250,anchor="center")
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

        

        limit_button=self.widgets.createButton(test_frame,"Limit Seç",100,150,width=20,height=1,command=self.exit)
        limit_button.config(bg="gray60")

        predict_button=self.widgets.createButton(test_frame,"Ölçüm Yap",100,200,width=20,height=1,command=self.exit)
        predict_button.config(bg="gray60")


    def train(self):
        self.machine_learning.train(self.filename)

    def browseFiles(self): 
        self.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Dosya Seç", 
            filetypes = (("Excel files", "*.csv*"),("all files",     "*.*")))
        (self.filename)
        
    def limitControl(self):
        pass


    def exit(self):
        pass


