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
        user_test = User(name = None, password = password, email=email, cpf = None)
        user_dict = {}
        for user in self.users:
            user_email = user.get_email()
            passw = user.get_password()
            user_dict[user_email] = (passw, [user.get_name(), user.get_cpf()])

        try:
            if user_dict[email][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = user_dict[email][1][0] # Nome
                st.session_state['Cpf'] = user_dict[email][1][1]     # CPF
                st.session_state['Email'] = email                    # Email
                
            else:
                st.session_state["Login"] = "negado"
                st.markdown("# Usuário/Senha Incorreta 💩")
        
        except KeyError:

            st.session_state["Login"] = "negado"
            st.markdown("# Usuário/Senha Incorreta")
            

    def sign_up(self, name, email, password, cpf):
        user = User(name, email, password, cpf)
       
        try:
            UserDAO.get_instance().inserir_user(user)
        except Exception as e:
            st.markdown(e)

    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CartController()