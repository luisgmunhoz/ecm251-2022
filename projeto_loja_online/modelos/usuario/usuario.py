class Usuario():
    #Método construtor
    def __init__(self, login, senha):
        self._login = login
        self._senha = senha
        file = open("userdb.txt","a");
        file.write(login + " "+ senha)
        file.close()