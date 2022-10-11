# Luis Guilherme de Souza Munhoz RA: 20.01937-8

import streamlit as st
from src.models.user import User
from src.controllers.cart_controller import CartController
class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="robin", password = "batman", email = "damian@wayneenterprises.com"),
            User(name="ednaldo", password = "pereira", email = "ednaldo.chance@gmail.com"),
            User(name ="tais", password="petacular", email = "tais@perando.com")
        ]

    def check_login(self, name, password):
        user_test = User(name = name, password = password, email=None)
        user_dict = {}
        for user in self.users:
            un = user.get_name()
            pw = user.get_password()
            user_dict[un] = (pw, user.get_email())

        try:

            if user_dict[name][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = name              # Nome
                st.session_state['Email'] = user_dict[name][1]  # Email
            else:
                st.session_state["Login"] = "negado"
                st.markdown("# Usuário/Senha Incorreta 💩")
        
        except KeyError:

            st.session_state["Login"] = "negado"
            st.markdown("# Usuário/Senha Incorreta 💩")
            
    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CartController()