class Usuario():
    #Método construtor
    def __init__(self, login, senha):
        self._login = login
        self._senha = senha
        self.registrar()

    def registrar(self):
        file = open("userdb.txt","a")
        file.write("\n" + self._login + " "+ self._senha)
        file.close()