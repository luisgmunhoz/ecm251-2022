# Luis Guilherme de Souza Munhoz RA: 20.01937-8

import streamlit as st
import time
from models.product import Product
from dao.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self._products = ProductDAO.get_instance().get_all()

    def get_product(self,index):
        return self._products[index]
    
    def get_products(self):
        return self._products

    def sign_product(self, name, price, url, amount):
        product = Product(name, price, url, amount)
        
        ProductDAO.get_instance().inserir_product(product)
        st.session_state["Login"] = "negado"
        time.sleep(0.2)
        st.session_state["Login"] = "aprovado"