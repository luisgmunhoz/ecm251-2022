
import streamlit as st

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)


tab1, tab2, tab3 = st.tabs(["Login", "Profile", "Home"])

with tab1:
    st.text("")
    st.text("")

    st.title("Login")

    st.markdown("***")

    st.text_input(
        label="Usuário",
        )

    st.text_input(
        label="Senha",
        type = "password")

    st.text("")
    st.button(label= "Entrar")

with tab2:
    st.title("Profile")

    st.markdown("***")

    col1,col2 = st.columns(2)

    with col1:
        st.markdown("#")
        st.image("https://i.scdn.co/image/ab6761610000e5eb9319d939accc1f1e22155955")
    
    with col2:
        st.markdown("***")
        st.markdown("### Nome:")
        st.markdown("#### Ednaldo P.")
        st.markdown("***")
        st.markdown("### Email:")
        st.markdown("#### Godnaldopereira@gmail.com ")
        st.markdown("***")

with tab3:

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