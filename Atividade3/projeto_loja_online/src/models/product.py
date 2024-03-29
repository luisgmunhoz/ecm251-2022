# Luis Guilherme de Souza Munhoz RA: 20.01937-8

class Product():
    def __init__(self, name, price, url):
        self._name = name
        self._price = price
        self._url = url

    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price

    def get_url(self):
        return self._url

    def __str__(self):
        return f'Product(_name:{self.get_name()}, _price:{self.get_price()}, _url:{self.get_url()})'