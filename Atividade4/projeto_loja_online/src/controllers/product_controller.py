# Luis Guilherme de Souza Munhoz RA: 20.01937-8

from models.product import Product
from dao.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self._products = ProductDAO.get_instance().get_all()

    def get_product(self,index):
        return self._products[index]