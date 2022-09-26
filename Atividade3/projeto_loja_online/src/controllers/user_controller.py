import streamlit as st
from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="robin", password = "batman", email = "damian@wayneenterprises.com"),
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
            d[key] = (val, user.get_email())

        try:
            if d[name][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = name
                st.session_state['Email'] = d[name][1]
            else:
                st.session_state["Login"] = "negado"
                st.markdown("# Senha Incorreta")
        except KeyError:
            st.session_state["Login"] = "negado"
            st.markdown("# Usuário Incorreto")
    def logout():
        st.session_state["Login"] = "negado"