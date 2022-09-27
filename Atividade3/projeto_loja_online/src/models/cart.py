class Cart():
    def __init__(self):
        self._products=[]
    def get_product(self,name):
        for i in self._products:
            if i.get_name() == name:
                return i
    def __str__(self):
        return self._products