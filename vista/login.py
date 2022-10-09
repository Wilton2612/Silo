from tkinter import *
from tkinter import messagebox, ttk
import interfaz
from back.autenticacion import login
from back.data import usuario_logueado_excel



class Login:

    def __init__(self, window):
        self.root = window
        self.root.title("Sistema de inventarios")
        self.center(1000, 500)
       # self.root.geometry('1000x500')
        self.root.config(bg='#69DADB')
        self.root.resizable(1,1)

        self.root.columnconfigure(0, weight=3)
                
        saludo = Label(self.root, text="Bienvenido a SensorInv!!", borderwidth=2,bg='#69DADB', fg='white',  font='arial 25', height=2, width=100)
        saludo.grid(row=0, column=0, padx=5, pady=30) 


        panel_principal = Frame(self.root, borderwidth=2,height=400, width=900, bg='#1597E5')
        panel_principal.grid(row=1, column=0, pady=30)

        Label(panel_principal, text="Usuario:", font='arial 12', bg='#1597E5').grid(pady=5, row=0, column=0)
        
        Label(panel_principal, text="Password:", font='arial 12', bg='#1597E5').grid( pady=5, row=1, column=0)

        self.email = Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 12')
        self.email.focus()
        self.email.grid(padx=1,pady=5, ipadx=10, ipady=5, row=0, column=1)
        self.password = Entry(panel_principal, width=40, border=0, borderwidth=1, relief='solid', font='arial 12')
        self.password.grid(padx=1,pady=5, ipadx=10,  ipady=5,row=1, column=1)
        self.password.config(show="*")

        self.loguear = Button(panel_principal, text="Aceptar", font='arial 12',width=50, bg='#69DADB', border=0, command=self.ingresar)
        self.loguear.grid(padx=10, pady=10, row=2, column=0, columnspan=2)
    




    def validar(self):
        return len(self.email.get()) != 0 and len(self.password.get()) != 0


    def ingresar(self):
        usuario = self.email.get()
        contrasena = self.password.get()
        if self.validar():
            respuesta = login(usuario, contrasena)
            if (respuesta ==0):
                usuario_logueado_excel(usuario, contrasena)
                self.root.destroy()
                interfaz.Principal()
            else:
                messagebox.showerror(message="El correo o la contraseña no es correcta",title="Mensaje") 
        else:
            messagebox.showerror(message="Escriba en todos los campos",title="Mensaje")


    def center(self, ancho, alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
        y_cor = int((alto_pantalla/2)-(alto_ven/2))
        self.root.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))

if __name__ == '__main__':
    window = Tk()
    app = Login(window)
    window.mainloop()











