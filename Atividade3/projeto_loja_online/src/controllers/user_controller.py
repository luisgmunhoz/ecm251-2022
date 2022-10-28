# Luis Guilherme de Souza Munhoz RA: 20.01937-8

import streamlit as st
from src.models.user import User
from src.controllers.cart_controller import CartController
from src.dao.user_dao import UserDAO

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = UserDAO.get_instance().get_all()

    def check_login(self, email, password):
        user_test = User(name = None, password = password, email=email)
        user_dict = {}
        for user in self.users:
            un = user.get_email()
            pw = user.get_password()
            user_dict[un] = (pw, user.get_name())

        try:

            if user_dict[email][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = user_dict[email][1] # Nome
                st.session_state['Email'] = email                 # Email
            else:
                st.session_state["Login"] = "negado"
                st.markdown("# Usuário/Senha Incorreta 💩")
        
        except KeyError:

            st.session_state["Login"] = "negado"
            st.markdown("# Usuário/Senha Incorreta 💩")
            
    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CartController()