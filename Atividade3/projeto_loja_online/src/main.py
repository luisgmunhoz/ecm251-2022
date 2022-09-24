import streamlit as st

from src.models import product
from src.controllers.user_controller import UserController

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)
    
st.text("")
st.text("")

st.title("Login")

st.markdown("***")

user = st.text_input(
    label="Usuário",
)

password = st.text_input(
    label="Senha",
        type = "password"
)

st.text("")
st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),user,password))
if "Login" in st.session_state:
    st.markdown("#### Login " + st.session_state["Login"])
    if st.session_state["Login"] == "aprovado":
        tab1, tab2, tab3, tab4= st.tabs(["Profile", "Home", "Produto", "Carrinho"])
        with tab1: 
            st.title("Profile")

            st.markdown("***")
            st.text("")
            col1,col2, col3= st.columns(3)

            with col1:
                st.markdown("#")
                st.image("https://i.scdn.co/image/ab6761610000e5eb9319d939accc1f1e22155955")
                
            with col2:
                nome ="Ednaldo P."
                st.markdown("***")
                st.markdown("### Nome:")
                st.markdown("#### %s" % nome)
                st.markdown("***")
                st.markdown("### Email:")
                st.markdown("#### Godnaldopereira@gmail.com ")
                st.markdown("***")
            with col3:
                st.markdown("***")
                st.button(label= "Sair", on_click= UserController.logout)
        with tab2:

            st.title("Home")

            st.markdown("***")

            col1,col2 = st.columns(2,gap="large")
                
            with col1:
                c = st.container()
                c.markdown("## Cadeira")
                c.image("https://lojamor.vteximg.com.br/arquivos/ids/168129-400-400/009401-Cadeira-Eiffel-Mor-Branca.jpg?v=636832571625900000")
                c.markdown("#### R$ 99,00")
                c.markdown("#### 25 Unidades em estoque")
                c.number_input(label = "", format = "%i", step = 1,min_value = 0)
                c.button(label = "Adicionar")
            with col2:
                c = st.container()
                c.markdown("## Bola")
                
            with col1:
                c = st.container()
                c.markdown("## Clipes")

        with tab3:
            col1,col2 = st.columns([2,1])
            with col1:
                st.markdown("#")
                st.image("https://lojamor.vteximg.com.br/arquivos/ids/168129-400-400/009401-Cadeira-Eiffel-Mor-Branca.jpg?v=636832571625900000")
                
            with col2:
                teste = 0
                st.markdown("# Cadeira")
                st.markdown("### R$ 99,00")
                st.markdown("### 25 Unidades em estoque")
                st.number_input(label = " ", format = "%i", step = 1, min_value = 0)
                st.button(label = "Adicionar", help = "Adiciona a quantidade selecionada ao carrinho")
                
                st.markdown("***")
                st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt sem et felis molestie, at pulvinar massa sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque in vehicula leo. Vivamus a eleifend dolor, ut porttitor eros. Morbi pharetra scelerisque lorem, sed suscipit eros ultricies vel. In volutpat nibh in erat finibus posuere. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam sit amet rhoncus nisi. Nulla sed pulvinar metus. Aenean ligula ante, gravida ut lectus quis, tempor lobortis est. Nulla ac eros pulvinar, hendrerit purus eget, sollicitudin magna. Mauris sit amet massa non tortor tincidunt varius. Suspendisse non ex mauris. Praesent in tellus dictum, egestas lacus nec, aliquam risus.")
                    
