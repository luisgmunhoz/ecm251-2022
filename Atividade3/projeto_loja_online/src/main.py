import streamlit as st

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
from src.controllers.cart_controller import CartController

p_controller = ProductController()

st.set_page_config(page_title="Projeto Loja Online T3 Luis Guilherme", page_icon="assets/batman.png")

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

if "Login" not in st.session_state:

    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
    st.session_state["Cart"] = CartController()

with st.sidebar:

    if st.session_state["Login"] == "negado":
        
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

    if st.session_state["Login"] == "aprovado":

        st.text("")

        st.title(f"Bem vindo, {st.session_state['Usuario']}")
        st.markdown("***")
        st.button(label= "Sair", on_click= UserController.logout)
        st.markdown("***")

if "Login" in st.session_state:

    # st.markdown("#### Login " + st.session_state["Login"])
    if st.session_state["Login"] == "aprovado":
        tab1, tab2, tab3= st.tabs(["Perfil", "Home", "Carrinho"])

        with tab1: 

            st.title("Perfil")

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
            
            st.markdown("***")

            col1,col2 = st.columns(2,gap="large")

            with col1:

                product = p_controller.get_product(index = 0)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "", key = 1, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 2, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
            
            with col2:

                product = p_controller.get_product(index = 1)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity2 = c.number_input(label = "", key = 3, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 4, on_click= st.session_state["Cart"].add_product, args = (product, quantity2))
            
            with col1:

                product = p_controller.get_product(index = 2)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "",key = 5, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 6, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
            
            with col2:

                product = p_controller.get_product(index = 3)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "",key = 7, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 8, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
            
            with col1:

                product = p_controller.get_product(index = 4)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "",key = 9, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 10, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
            
            with col2:

                product = p_controller.get_product(index = 5)
                c = st.container()
                c.markdown(f"## {product.get_name()}")
                c.image(f"{product.get_url()}")
                c.markdown(f"## R${product.get_price()}")
                quantity1 = c.number_input(label = "",key = 11, format = "%i", step = 1,min_value = 1, max_value = 10)
                c.button(label = f"Adicionar {product.get_name()}", key = 12, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
        
        with tab3:

            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3 = st.columns(3,gap="large")
            col1.markdown("### Produto")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
            
            
            
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")

            with col2:

                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### R${product_prices[i]}")

            with col3:
                
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")

            st.markdown("***")
            valor_total = st.session_state["Cart"].get_total_price()
            
            st.markdown(f"## Valor total: R${valor_total:.3f} ")
        