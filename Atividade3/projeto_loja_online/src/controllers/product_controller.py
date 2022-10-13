# Luis Guilherme de Souza Munhoz RA: 20.01937-8

from models.product import Product

class ProductController:
    def __init__(self):

        self._products = [
            Product("Elden Ring", 199.99, "https://assets-prd.ignimgs.com/2021/06/12/elden-ring-button-03-1623460560664.jpg?width=300&crop=1%3A1%2Csmart"),
            Product("Cyberpunk 2077", 129.99, "https://sm.ign.com/t/ign_br/game/c/cyberpunk-/cyberpunk-2077_tdqt.300.jpg"),
            Product("Starfield", 399.99, "https://sm.ign.com/t/ign_br/game/s/starfield/starfield_23ps.300.jpg"),
            Product("Fallout 5", 399.99, "https://sm.ign.com/t/ign_br/cover/f/fallout-5/fallout-5_kfgs.300.jpg"),
            Product("Geladeira XSX", 9999.99, "https://sm.ign.com/t/ign_pt/cover/x/xbox-mini-/xbox-mini-fridge_h8at.300.jpg"),
            Product("Console KFC", 4999.99, "https://i0.wp.com/assets.mspimages.in/wp-content/uploads/2020/12/KFConsole-696x365.jpg?resize=300%2C300&ssl=1")
        ]

    def get_product(self,index):
        return self._products[index]