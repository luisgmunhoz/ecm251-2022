import streamlit as st

class ListaTarefasView:
    def __init__(self, controller) -> None:
        self.controller = controller
        self.descricao_tarefa = st.text_input(label = "Insira sua tarefa aqui...")
        self.bot_adicionar = st.button(label = "adicionar", on_click = self.adicionar_tarefa)

    def adicionar_tarefa(self):
        self.controller.criar_nova_tarefa(self.descricao_tarefa)