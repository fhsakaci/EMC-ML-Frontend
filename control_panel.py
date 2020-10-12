import tkinter as tk

class control_panel():
    def __init__(self,window,widgets,machine_learning):
        self.window=window
        self.widgets=widgets
        self.panel_frame=self.createPanel(window)
        self.createPanelContents()
        self.machine_learning=machine_learning

    def createPanel(self,window):
        panel_frame=self.widgets.createFrame(window,x=580,y=50,width=470,height=500)
        panel_frame.config(bg="gray42")
        return panel_frame
    
    def createPanelContents(self):
        
        
        title1_label=self.widgets.createLabel(self.panel_frame,"Yeni Eğitim Modeli Üret",125,20,font=("Helvetica", 16))
        title1_label.config(bg="gray42")
        OptionList = ["RE102","CE102"] 
        variable = tk.StringVar(self.panel_frame)
        variable.set(OptionList[0])

        file_button=self.widgets.createButton(self.panel_frame,"Dosya Seç",300,100,width=20,height=1,command=self.browseFiles)
        file_button.config(bg="gray62")

        test_type=self.widgets.createDropdown(self.panel_frame,variable,OptionList,300,150,width=18,height=1)
        test_type.config(bg="gray62") 


        draw_button=self.widgets.createButton(self.panel_frame,"Model Oluştur",300,200,width=20,height=1,command=self.train)
        draw_button.config(bg="gray62") 

        title2_label=self.widgets.createLabel(self.panel_frame,"Emisyon Ölçümü Yap",100,300,font=("Helvetica", 16))
        title2_label.config(bg="gray42")

        
        exit_button=self.widgets.createButton(self.panel_frame,"Çıkış",300,450,width=20,height=1,command=self.exit)
        exit_button.config(bg="gray62")

    def train(self,filename):
        self.machine_learning.train(self.filename)

    def browseFiles(self): 
        self.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Dosya Seç", 
            filetypes = (("Excel files", "*.csv*"),("all files",     "*.*")))
    
    def limitControl(self):
        pass


    def exit(self):
        pass


