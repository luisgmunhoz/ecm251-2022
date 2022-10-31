# Luis Guilherme de Souza Munhoz RA: 20.01937-8

class Product():
    def __init__(self, name, price, url, amount):
        self._name = name
        self._price = price
        self._url = url
        self._amount = amount

    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price

    def get_url(self):
        return self._url
    
    def get_amount(self):
        return self._amount
    
    def set_amount(self, amount):
        self._amount = amount

    def __str__(self):
        return f'Product(name:{self.get_name()}, price:{self.get_price()}, url:{self.get_url()}, amount:{self.get_amount()})'