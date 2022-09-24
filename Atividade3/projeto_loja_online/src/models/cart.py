class Cart():
    def __init__(self):
        self._products = []

    def adicionar(self, item):
        self._products.append(item)

    def remover(self, item):
        self._products.remove(item)

    def get_valor_total(self):
        total = 0
        for item in self._products:
            total += item.get_price()
        return total
        
    def get_quantidade_itens(self):
        return len(self._products)