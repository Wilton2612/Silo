import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
sys.path.insert(1, os.getcwd())
from back.data import generar_excel, listar_datos, leer_usuario, buscar_silo
import agregar
import editar

 



class Principal:


    def __init__(self):
        self.window = tk.Tk()
                
        self.window.title("Sistema de inventarios")
        self.center(1000, 700)
       # self.window.geometry('1000x700')
        self.window.config(bg='#69DADB')
        self.window.resizable(1,1)

        self.window.columnconfigure(0, weight=2)



        """ Panel que agrupa los titulos de las columnas el contenido de esta"""
        panel  = tk.Frame(self.window, borderwidth=2, height=400, width=900)
        panel.grid(row=0, column=0, pady=60)

        panel.columnconfigure(0, weight=2)


        #tabla

        self.tree = ttk.Treeview(panel, columns=("FECHA", "INVENTARIO", "OCUPACIÓN", "ESTADO"), height=15)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.column('#0', width=60)
        
        
        self.tree.heading('#0', text='ID SILO', anchor= tk.CENTER)
        self.tree.heading('FECHA', text='FECHA', anchor= tk.CENTER)
        self.tree.heading('INVENTARIO', text='INVENTARIO' , anchor= tk.CENTER )
        self.tree.heading('OCUPACIÓN', text='OCUPACIÓN', anchor= tk.CENTER)
        self.tree.heading('ESTADO', text='ESTADO' , anchor= tk.CENTER)
       
      
        """ Sección de los botones bg='#a6d3ff', """
        botones = tk.Frame(self.window, bg='#69DADB',height=300, width=500)
        botones.grid(row=1, column=0, pady=30)

        botones.columnconfigure(0, weight=2)
        botones.columnconfigure(1, weight=2)
        botones.columnconfigure(2, weight=2)

        btn_inventario = tk.Button(botones, text='Calcular inventario', font='arial 12', bg='#1597E5',borderwidth = 0,  height=2, width=20, command=self.calcular)
        btn_inventario.grid(row=0, column=0, padx=15, pady=5)

        btn_excel = tk.Button(botones, text='Exportar a Excel', font='arial 12', bg='#1597E5', borderwidth = 0,  height=2, width=20, command=self.exportar_excel)
        btn_excel.grid(row=0, column=1, padx=15, pady=5)

        btn_medida = tk.Button(botones, text='Agregar silo', font='arial 12', bg='#1597E5',borderwidth = 0,  height=2, width=20, command=self.cambiar_medida)
        btn_medida.grid(row=0, column=2,  padx=15, pady=5)
        
        btn_editar = tk.Button(botones, text='Cambiar medidas', font='arial 12', bg='#1597E5',borderwidth = 0,  height=2, width=20, command=self.editar_medida)
        btn_editar.grid(row=0, column=3,  padx=15, pady=5)
        


        

        self.window.mainloop()


    def editar_medida(self):
        sele = self.tree.focus()
        identificador = self.tree.item(sele, 'text' )
        nombre_usuario = leer_usuario()
        si = buscar_silo(identificador, nombre_usuario)
        if si == 0:
            self.window.destroy()
            editar.Editar()
        else:
            messagebox.showerror(message="Ocurrio un error, selecciona un silo",title="Mensaje")



    def exportar_excel(self):
        nombre_usuario = leer_usuario()
        answer = generar_excel(nombre_usuario)
        if answer == 0:
            messagebox.showinfo(message="Se genero el Excel",title="Mensaje")
        else:
            messagebox.showerror(message="Ocurrio un error, intentalo de nuevo",title="Mensaje")
            

    
    def cambiar_medida(self):
        self.window.destroy()
        agregar.Medida()
    

    def calcular(self):

        # limpio la tabla
        datos_en_tabla = self.tree.get_children()
        for fila in datos_en_tabla:
            self.tree.delete(fila)
        
        #obtengo los datos de firebase
        nombre_usuario = leer_usuario()
        datos = listar_datos(nombre_usuario)
        for element in datos:
            self.tree.insert('', 0, text=element[0], value=(element[1], element[2], element[3], element[4]))

    def center(self, ancho, alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_pantalla = self.window.winfo_screenwidth()
        alto_pantalla = self.window.winfo_screenheight()
        x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
        y_cor = int((alto_pantalla/2)-(alto_ven/2))
        self.window.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))

if __name__  == '__main__':
    Principal()

  
"""
        titles = tk.Frame(panel, borderwidth=2, height=60, width=900)
        titles.grid(rows=1, column=0, pady=10, padx=10)

        titles.columnconfigure(0, weight=2)
        titles.columnconfigure(1, weight=2)
        titles.columnconfigure(2, weight=2)
        titles.columnconfigure(3, weight=2)
        titles.columnconfigure(4, weight=2)


        title_id_silo = tk.Label(titles, text="Id silo", borderwidth=0, bg='#193498', fg='white',  font='arial 12', height=2, width=15)
        title_id_silo.grid(row=0, column=0, padx=5, pady=2) 
        title_fecha = tk.Label(titles, text="Fecha", borderwidth=0, bg='#193498', fg='white',  font='arial 12', height=2, width=15)
        title_fecha.grid(row=0, column=1, padx=5, pady=2)
        title_inventario = tk.Label(titles,text="Inventario",  borderwidth=0, bg='#193498', fg='white',  font='arial 12', height=2, width=15)
        title_inventario.grid(row=0, column=2, padx=5, pady=2)
        title_ocupacion = tk.Label(titles, text="Ocupación", borderwidth=0, bg='#193498', fg='white',  font='arial 12', height=2, width=15)
        title_ocupacion.grid(row=0, column=3, padx=5, pady=2)
        title_estado = tk.Label(titles, text="Estado", borderwidth=0, bg='#193498', fg='white',  font='arial 12', height=2, width=15)
        title_estado.grid(row=0, column=4, padx=5, pady=2)
        """



"""Contenido de cada columna"""

"""
        contenido = tk.Frame(panel, borderwidth=2, height=170, width=900)
        contenido.grid(rows=1, column=0, pady=10, padx=10)


        panel.columnconfigure(0, weight=2)
        panel.columnconfigure(1, weight=2)
        panel.columnconfigure(2, weight=2)
        panel.columnconfigure(3, weight=2)
        panel.columnconfigure(4, weight=2)


        id_silo = tk.LabelFrame(contenido, borderwidth=1, relief="solid", height=350, width=136)
        id_silo.grid(row=0, column=0, padx=5, pady=2)
        fecha = tk.LabelFrame(contenido, borderwidth=1, relief="solid", height=350, width=136)
        fecha.grid(row=0, column=1, padx=5, pady=2)
        inventario = tk.LabelFrame(contenido,  borderwidth=1, relief="solid", height=350, width=136)
        inventario.grid(row=0, column=2, padx=5, pady=2)
        ocupacion = tk.LabelFrame(contenido, borderwidth=1, relief="solid", height=350, width=136)
        ocupacion.grid(row=0, column=3, padx=5, pady=2)
        estado = tk.LabelFrame(contenido, borderwidth=1, relief="solid", height=350, width=136)
        estado.grid(row=0, column=4, padx=5, pady=2)
        """








      