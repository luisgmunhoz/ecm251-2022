class Product():
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url
    def __str__(self):
        return f'Product(name:{self.name}, price:{self.price}, url:{self.url})'