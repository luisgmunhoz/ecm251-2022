import streamlit as st
from controllers.user_controller import UserController

st.text("")
st.text("")

st.title("Login")

st.markdown("***")

user_name = st.text_input(
    label="Usuário",
    )

password = st.text_input(
    label="Senha",
    type = "password")

st.text("")
button1 = st.button(
    label= "Entrar",
    on_click = UserController.login,
    kwargs={"user":user_name, "password":password}
)
    
