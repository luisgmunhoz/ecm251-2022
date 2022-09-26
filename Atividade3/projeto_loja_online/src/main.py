import streamlit as st

from src.models.product import Product
from src.controllers.user_controller import UserController
from src.models.cart import Cart
from src.controllers.product_controller import ProductController

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)
if "Login" not in st.session_state:
    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
if "cart" not in st.session_state:
    st.session_state["cart"] = "removido"
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
    p_controller = ProductController()

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
                st.image("https://i.pinimg.com/736x/ea/8b/c0/ea8bc0fd9e2bf37e9ad09f056ff6ebc6.jpg")
                
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
                product = p_controller.get_product(index = 0)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}", width = 280)
                
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "", format = "%i", step = 1,min_value = 0)
                c.button(label = f"Adicionar {product.get_name()}", key = 1, on_click= cart.adicionar(item = product, amount = quantity1))
            with col2:
                product = p_controller.get_product(index = 1)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}",width = 300)
                c.markdown(f"## R${product.get_price()}")
                quantity2 = c.number_input(label = "quantity", format = "%i", step = 1,min_value = 0)
                c.button(label = f"Adicionar {product.get_name()}", key = 2, on_click= cart.adicionar(item = product, amount = quantity2))

        with tab3:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3, col4 = st.columns(4,gap="small")
            
            valor_total = cart.get_valor_total()
            if st.session_state["cart"] != "removido": 
                st.markdown(f"## Valor total: {valor_total} ")
            
            product_qtt = []
            product_names = []
            product_prices = []
            for i in range(0, cart.get_quantidade_itens()):
                if cart._products[i][0].get_name() not in product_names:
                    product_names.append(cart._products[i][0].get_name())
                    product_prices.append(cart._products[i][0].get_price())
                    product_qtt.append(cart._products[i][1])
                    amount1 = product_qtt[i]
                    ii = i
                else:
                    amount1 += cart._products[i][1]
                    product_qtt.insert(ii, amount1)
            with col1:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")
            with col2:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_prices[i]}")
            with col3:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")