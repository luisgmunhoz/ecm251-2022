import streamlit as st

from src.models.product import Product
from src.controllers.user_controller import UserController
from src.models.cart import Cart

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)
if "Login" not in st.session_state:
    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
with st.sidebar:

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
    col1, col2 = st.columns(2)
    with col1:
        st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),user,password))
    with col2:
        st.button(label= "Sair", on_click= UserController.logout)
                    
if "Login" in st.session_state:
    # st.markdown("#### Login " + st.session_state["Login"])
    if st.session_state["Login"] == "aprovado":
        tab1, tab2, tab3= st.tabs(["Profile", "Home", "Carrinho"])
        with tab1: 
            st.title("Profile")

            st.markdown("***")
            st.text("")
            col1,col2, col3= st.columns(3)

            with col1:
                st.markdown("#")
                st.image("https://i.scdn.co/image/ab6761610000e5eb9319d939accc1f1e22155955")
                
            with col2:
                st.markdown("***")
                st.markdown(f"### Nome: {st.session_state['Usuario']}")
                st.markdown("***")
                st.markdown(f"### Email: {st.session_state['Email']}")
                st.markdown("***")
           
        with tab2:

            st.title("Home")
            cart = Cart()
            st.markdown("***")

            col1,col2 = st.columns(2,gap="large")
                
            with col1:
                product1 = Product("Elden Ring", 199.00, "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png")
                c = st.container()
                c.markdown(f"## {product1.get_name()}")
                c.image(f"{product1.get_url()}", width = 256)
                
                c.markdown(f"## R${product1.get_price()}")
                c.markdown("#### Unidades em estoque")
                quantity1 = c.number_input(label = "", format = "%i", step = 1,min_value = 0)
                c.button(label = f"Adicionar {product1.get_name()}", on_click= cart.adicionar(product1))
            with col2:
                product2 = Product("Cyberpunk 2077", 199.00, "https://gizmodo.uol.com.br/wp-content/blogs.dir/8/files/2022/09/capsule_616x353.jpg")
                c = st.container()
                c.markdown(f"## {product2.get_name()}")
                c.image(f"{product2.get_url()}",width = 330)
                c.markdown(f"## R${product2.get_price()}")
                c.markdown("#### Unidades em estoque")
                quantity2 = c.number_input(label = "quantity", format = "%i", step = 1,min_value = 0)
                c.button(label = f"Adicionar {product2.get_name()}", on_click= cart.adicionar(product2))

        with tab3:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3, col4 = st.columns(4,gap="small")
            
            valor_total = cart.get_valor_total()
            st.markdown(f"## Valor total: {valor_total} ")
            
            
            with col1:
                c = st.container()
                product_names = []
                for i in range(cart.get_quantidade_itens()):
                    product_names.append(cart._products[i].get_name())
                    c.markdown(f"#### {product_names[i]}")
            with col2:
                c = st.container()
                product_prices = []
                for i in range(cart.get_quantidade_itens()):
                    product_prices.append(cart._products[i].get_price())
                    c.markdown(f"#### {product_prices[i]}")
            with col3:
                c = st.container()
                product_qtt = []
                for i in range(cart.get_quantidade_itens()):
                    product_qtt.append(cart.get_quantidade_itens())
                    c.markdown(f"#### {product_qtt[i]}")
            with col4:
                c = st.container()
                c.button(label = f"Remover {product_names[0]}", on_click= cart.remover(cart._products[0]))
                c.button(label = f"Remover {product_names[1]}", on_click= cart.remover(cart._products[0]))