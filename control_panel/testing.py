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

        parameter_button=self.widgets.createButton(test_frame,"Parametreleri Gir",100,100,width=20,height=1,command=self.parameters)
        parameter_button.config(bg="gray60")

        
        test_type=self.widgets.createDropdown(test_frame,variable,OptionList,100,50,width=18,height=1)
        test_type.config(bg="gray60") 

        limit_button=self.widgets.createButton(test_frame,"Model Seç",100,150,width=20,height=1,command=self.browseFiles)
        limit_button.config(bg="gray60")

        predict_button=self.widgets.createButton(test_frame,"Ölçüm Yap",100,200,width=20,height=1,command=self.predict)
        predict_button.config(bg="gray60")

    def predict(self):
        response=self.machine_learning.predict(self.path)
        self.logger.info(str(response))
        self.graph.draw_fig(response)
        self.graph.draw()

    def browseFiles(self): 
        self.path = tk.filedialog.askdirectory(initialdir = "/",title = "Model Seç")
        
    def limitControl(self):
        pass
    
    def parameters(self):
        popup = tk.Tk()
        popup.geometry("680x350")
        popup.wm_title("Parametreleri Gir")
        self.C_in_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Giriş Kapasitesi: ",40,80)
        C_in=self.widgets.createText(popup,self.C_in_variable,150,80,width=15,height=1)

        self.C_out_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Çıkış Kapasitesi: ",40,150)
        C_out=self.widgets.createText(popup,self.C_out_variable,150,150,width=15,height=1)

        self.switch_freq_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Tetikleme Frekansı: ",40,220)
        switch_freq=self.widgets.createText(popup,self.switch_freq_variable,150,220,width=15,height=1)

        self.input_voltage_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Giriş Gerilimi: ",400,80)
        input_voltage=self.widgets.createText(popup,self.input_voltage_variable,500,80,width=15,height=1)

        self.output_voltage_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Çıkış Gerilimi: ",400,150)
        output_voltage=self.widgets.createText(popup,self.output_voltage_variable,500,150,width=15,height=1)

        self.output_current_variable = tk.StringVar()
        self.widgets.createLabel(popup,"Çıkış Akımı: ",400,220)
        output_current=self.widgets.createText(popup,self.output_current_variable,500,220,width=15,height=1)


        B1 = self.widgets.createButton(popup, "Parametreleri Al",500,300,width=20,height=1, command = self.set_parameters)
        popup.mainloop()

    
    def set_parameters(self):
        pass

    def exit(self):
        pass
    
