# Luis Guilherme de Souza Munhoz RA: 20.01937-8

class User():
    def __init__(self, name, email, password, cpf):
        self._email = email
        self._name = name
        self._password = password
        self._cpf = cpf

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf

    def __str__(self)->str:
        return f'User(name:{self.get_name()}, email:{self.get_email()}, password:{self.get_password()} cpf:{self.get_cpf()}'