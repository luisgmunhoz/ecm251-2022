from models.user import User

class UserController():
    def __init__(self) -> None:
        # Carrega os dados dos usuarios
        self.users = [
            User(name="joao",password="arroz",email="joao@gmail.com"),
            User(name="joao2",password="arroz2",email="joao@amaarroz.com"),
            User(name="tais",password="petacular",email="tais_@condida.com"),
        ]
    def check_user(self, user):
        return user in self.users

    def check_login(self, name, password):
        user_teste = User(name=name,password=password,email=None)
        for user in self.users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False