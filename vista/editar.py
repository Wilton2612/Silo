
import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
sys.path.insert(1, os.getcwd())
from back.data import leer_usuario, nuevas_medidas
import interfaz


class Editar:
    
    def __init__(self):
        self.window = tk.Tk()
                
        self.window.title("Sistema de inventarios")
        self.center(800, 700)
        #self.window.geometry('800x700')
        self.window.config(bg='#69DADB')
        self.window.resizable(1,1)
        
        self.window.columnconfigure(0, weight=3)

        saludo = tk.Label(self.window, text="Aquí puedes editar las medidas de un nuevo silo!!", borderwidth=2,bg='#69DADB', fg='white',  font='arial 25', height=2, width=100)
        saludo.grid(row=0, column=0, padx=5, pady=30) 



        """PANEL PARA INGRESAR DATOS"""
        panel_principal = tk.Frame(self.window, borderwidth=2,height=380, width=900, bg='#1597E5')
        panel_principal.grid(row=1, column=0, pady=30)
        
        tk.Label(panel_principal, text="Nueva Capacidad:", font='arial 14', bg='#1597E5').grid(pady=10, row=0, column=0)
        tk.Label(panel_principal, text="Nueva Altura:", font='arial 14', bg='#1597E5').grid(pady=10, row=1, column=0)
        tk.Label(panel_principal, text="Nueva Diámetro:", font='arial 14', bg='#1597E5').grid( pady=10, row=2, column=0)
        tk.Label(panel_principal, text="Nueva Altura del cono:", font='arial 14', bg='#1597E5').grid( pady=10, row=3, column=0)



        self.capacidad = tk.Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 14')
        self.capacidad.grid(padx=15,pady=10, ipadx=10, ipady=5, row=0, column=1)
        
        self.altura = tk.Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 14')
        self.altura.grid(padx=15,pady=10, ipadx=10, ipady=5, row=1, column=1)
       
        self.diametro = tk.Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 14')
        self.diametro.grid(padx=15,pady=10, ipadx=10,  ipady=5,row=2, column=1)
        
        self.altura2 = tk.Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 14')
        self.altura2.grid(padx=15,pady=10, ipadx=10,  ipady=5,row=3, column=1)



        """BOTONES"""
        botones = tk.Frame(self.window, bg='#69DADB',height=300, width=500)
        botones.grid(row=2, column=0, pady=30)

        botones.columnconfigure(0, weight=2)
        botones.columnconfigure(1, weight=2)

        
        btn_volver = tk.Button(botones, text='Volver', font='arial 14', bg='#1597E5',borderwidth = 0,  height=2, width=25, command=self.volver)
        btn_volver.grid(row=0, column=0,  padx=15, pady=5)

        btn_aceptar = tk.Button(botones, text='Aceptar', font='arial 14', bg='#1597E5',borderwidth = 0,  height=2, width=25, command=self.aceptar)
        btn_aceptar.grid(row=0, column=1,  padx=15, pady=5)
        self.window.mainloop()


    
    def validar_capacidad(self):
        capacidad =  self.capacidad.get()

        try:
            int(capacidad)
            return True
        except:
            return False
            


    def validar_alturaCilindro(self):
        alturaCilindro = self.altura.get()

        try:
            int(alturaCilindro)
            return True
        except:
            return False

    def validar_diametro(self):
        diametro = self.diametro.get()

        try:
            int(diametro)
            return True
        except:
            return False
    
    def validar_alturaCono(self):
        alturaCono = self.altura2.get()

        try:
            int(alturaCono)
            return True
        except:
            return False


    def validar(self):
     
        if self.validar_capacidad() and self.validar_alturaCilindro() and self.validar_alturaCono() and self.validar_diametro():
            return True
        else:
            return False
            messagebox.showerror(message="Solo se aceptan números",title="Mensaje")
            


    def verificacion(self):
        return len(self.altura.get()) != 0 and len(self.diametro.get()) != 0 and len(self.altura2.get())!= 0

   
    def volver(self):
        self.window.destroy()
        interfaz.Principal()
    
    def aceptar(self):
        capacidad =  self.capacidad.get()
        alturaCilindro = self.altura.get()
        diametro = self.diametro.get()
        alturaCono = self.altura2.get()
        
        if self.verificacion() and self.validar():
            usuario = leer_usuario()
            respuesta = nuevas_medidas(alturaCilindro, diametro, alturaCono,capacidad, usuario )
            if (respuesta ==0):
                messagebox.showinfo(message="Medidas actualizadas",title="Mensaje")
                self.window.destroy()
                interfaz.Principal()
            else:
                messagebox.showerror(message="No se pudo actualizar la medida",title="Mensaje") 
        else:
            messagebox.showerror(message="Escriba en todos los campos",title="Mensaje")
        
    def center(self, ancho, alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_pantalla = self.window.winfo_screenwidth()
        alto_pantalla = self.window.winfo_screenheight()
        x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
        y_cor = int((alto_pantalla/2)-(alto_ven/2))
        self.window.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))

if __name__  == '__main__':
    Editar()
