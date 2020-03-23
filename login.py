import tkinter as tk
from tkinter import ttk

class Axeso:
    """etiqueta y entry primera linea horizontal(row 0)"""
    def __init__(self):
        
        
        self.vent1=tk.Tk()
        self.vent1.title("axeso")
        self.e1=ttk.Label(text=" NOMBRE:")
        self.e1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.vent1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        """segunda linea etiqueta y entry  (row,1)  """   
        
        self.e2=ttk.Label(text=" CLAVE:")
        self.e2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.vent1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
 ##botones#######$$$$$$$$     
        self.boton1=ttk.Button(self.vent1, text="Ingresar", command=self.verificar)
        self.boton1.grid(column=1, row=2)
 ###$$$$$$$$$$$$###$$$$$$       
        self.boton2=tk.Button(self.vent1,text="salir",command=self.vent1.destroy)
        self.boton2.grid(column=0,row=2)
 #loop #####$$$$$$$$$$$$       
        self.vent1.mainloop()
        
        #user and pass###
########$#$$$$#######
    def verificar(self):
        if self.dato1.get()=="asd" and self.dato2.get()=="123":
###$$$$$$$$$$$$$$$$$$$$$$
        
            self.vent1.withdraw()
            import  index
            
            
            
        else:
            self.vent1.title("incorrecto")
            
