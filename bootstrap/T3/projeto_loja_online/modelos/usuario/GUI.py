from cgitb import text
from login import logar

import tkinter as tk
from usuario import Usuario
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from tkinter.ttk import Label
from ttkbootstrap import Colors
from ttkbootstrap import Style

class MinhaUI():
    def tela_home(self):
        nav_bar = ttk.Frame(style='primary', master = self.janela,height=70)
        nav_bar.pack(fill=X, pady=1, side=TOP)
        icon1 = PhotoImage(file='back-arrow-icon.png')
        cart_button = ttk.Button(style = 'danger', master = nav_bar, image = icon1)
        cart_button.image = icon1
        cart_button.pack(side = RIGHT)

    def tela_login(self, login, senha):
        texto = ttk.Label(text="Projeto Loja Online - Login", background = "#373E40", foreground = "#488286", font = ("Ubuntu Mono", 24))
        texto.pack()
        style_login = ttk.Style()
        # Create style used by default for all Frames
        style_login.configure('TFrame', background='green')
        
        # Create style for the first frame
        style_login.configure('Frame1.TFrame', background='#77878B')
        # Use created style in this frame
        frame1 = ttk.Frame(self.janela, style='Frame1.TFrame')
        frame1['padding'] = (100,200,100,200)
        frame1.place(rely=0.5,relx=0.5,anchor="c")
        
        
        estyle = ttk.Style()
        estyle.element_create("plain.field", "from", "clam")
        estyle.layout("EntryStyle.TEntry",
                        [('Entry.plain.field', {'children': [(
                            'Entry.background', {'children': [(
                                'Entry.padding', {'children': [(
                                    'Entry.textarea', {'sticky': 'nswe'})],
                            'sticky': 'nswe'})], 'sticky': 'nswe'})],
                            'border':'2', 'sticky': 'nswe'})])
        estyle.configure("EntryStyle.TEntry",
                        background="#B7D5D4", 
                        foreground="#488286",
                        fieldbackground="#B7D5D4")
                        


       
        texto1 = ttk.Label(text="Usuário",master = frame1, background = "#77878B", foreground = "#373E40", font = ("Ubuntu Mono", 24), anchor = W)
        texto1.grid(row=1,pady=[15,0])

        self._login = ttk.Entry(style="EntryStyle.TEntry",master = frame1,width=60, textvariable=login,  background = "#B7D5D4", font = ("Ubuntu Mono",24))
        self._login.grid(row=2)

        texto2 = ttk.Label(text="Senha",master = frame1, background = "#77878B", foreground = "#373E40", font = ("Ubuntu Mono", 24), anchor = W)
        texto2.grid(row=3,pady=[15,0])

        self._senha = ttk.Entry(style="EntryStyle.TEntry", master = frame1, width=60, textvariable = senha, show = "*", background = "#B7D5D4", font = ("Ubuntu Mono",24))
        self._senha.grid(row=4)

        ttk.Style().configure("TButton", padding=16, relief="flat",
        background="#B7D5D4",foreground = '#488286', width = 20, font = ("Ubuntu Mono", 20))
        
        botao1 = ttk.Button(text="Entrar", master = frame1, width=16, command=self.guardar_logar)
        botao1.grid(row=5,pady=[20,0])
        botao2 = ttk.Button(text="Registrar", master = frame1, width=16, command=self.guardar_registrar)
        botao2.grid(row=6,pady=[20,0])

    def tela_produto(self):
        nav_bar = ttk.Frame(style='primary', master = self.janela)
        nav_bar.pack(fill=X, pady=1,ipady=10, side=TOP)
        # Creating a photoimage object to use image
        photo = PhotoImage(file = "back-arrow-icon.png")
        
        # Resizing image to fit on button
        photoimage = photo.subsample(3, 3)
        
        # here, image option is used to
        # set image on button
        # compound option is used to align
        # image on LEFT side of button
        cart_button = ttk.Button(master =nav_bar,text = "back", style = "danger",image = photoimage, compound = LEFT)
        cart_button.pack(side = RIGHT)

    def __init__(self):
        self.janela = ttk.Window(
            size = [1920,1080]
            )
        self.janela.iconphoto(False, PhotoImage(file='calculator.png'))
        self.janela.configure(background = "#373E40")
        self._login = ttk.StringVar(value="")
        self._senha = ttk.StringVar(value="")
        ##self.tela_login(self.usuario,self.senha)
        self.tela_login(self._login,self._senha)
        self.janela.place_window_center()


    def run(self):
        self.janela.mainloop()

    def guardar_logar(self):
        logar(self._login.get(), self._senha.get())

    def guardar_registrar(self):
        Usuario(self._login.get(), self._senha.get())


if __name__ == "__main__":
    app = MinhaUI()
    app.run()