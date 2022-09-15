from cgitb import text
from login import logar
from usuario import Usuario
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class MinhaUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Login Mauá Loja Online",
            size= (1024,400),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0
        )
        janela.iconphoto(False, PhotoImage(file='calculator.png'))
        return janela

    def _criar_botao(self, texto, acao):
        return ttk.Button(
            self.base,
            text=texto,
            bootstyle=(DEFAULT),
            command=acao
        )

    def _criar_texto(self, guardar,senha):
        if(senha == True):
            return ttk.Entry(
                self.base,
                textvariable=guardar,
                show = "*"
            )
        else:
            return ttk.Entry(
                self.base,
                textvariable=guardar,
            )

    def __init__(self) -> None:
        self.base = self._construir_base()
        self.valor_digitado = ""
        self.login = self._criar_texto(guardar=self.valor_digitado, senha = False)
        self.login.grid(row=2, column=1, padx=5, pady=5)
        self.senha = self._criar_texto(guardar=self.valor_digitado, senha = True)
        self.senha.grid(row=3, column=1, padx=5, pady=5)
        self.bot = self._criar_botao(texto="Logar", acao=self.guardar_logar)
        self.bot.grid(row=4, column=1, padx=5, pady=5)
        self.bot = self._criar_botao(texto="Registrar", acao=self.guardar_registrar)
        self.bot.grid(row=5, column=1, padx=5, pady=5)
    def run(self):
        self.base.mainloop()

    def guardar_logar(self):
        log = [self.login.get(), self.senha.get()]
        logar(log[0],log[1])

    def guardar_registrar(self):
        log = [self.login.get(), self.senha.get()]
        user = Usuario(log[0], log[1])


if __name__ == "__main__":
    app = MinhaUI()
    app.run()