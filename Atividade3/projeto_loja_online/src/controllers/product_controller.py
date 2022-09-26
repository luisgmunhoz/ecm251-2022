from models.product import Product

class ProductController:
    def __init__(self):
        self._products = [
            Product("Elden Ring", 199.00, "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png"),
            Product("Cyberpunk 2077", 199.00, "https://gizmodo.uol.com.br/wp-content/blogs.dir/8/files/2022/09/capsule_616x353.jpg")
        ]

    def get_product(self,index):
        return self._products[index]