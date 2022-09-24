import streamlit as st
from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="batman", password = "robin", email = "joao@gmail.com"),
            User(name="João2", password = "arroz2", email = "joao2@gmail.com"),
            User(name ="tais", password="petacular", email = "tais@perando.com")
        ]
    
    def check_user(self,user):
        return user in self.users

    def check_login(self, name, password):
        user_test = User(name = name, password = password, email=None)
        d = {}
        for user in self.users:
            key = user.get_name()
            val = user.get_password()
            d[key] = val
        try:
            if d[name] == password:
                st.session_state["Login"] = "aprovado"
            else:
                st.session_state["Login"] = "negado"
                st.write("Senha Incorreta")
        except KeyError:
            st.session_state["Login"] = "negado"
            st.write("Usuário Incorreto")
    def logout():
        st.session_state["Login"] = "negado"