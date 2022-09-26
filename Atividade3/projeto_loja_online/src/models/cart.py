import streamlit as st

class Cart():
    def __init__(self):
        self._products = [[]]

    def adicionar(self, item, amount):
        for i in range(len(self._products)):
            if item not in self._products[i][0]:
                self._products.append([item, amount])
                ii = i
            else:
                self._products[ii][1] += amount
            print(self._products)

    def get_valor_total(self):
        total = 0
        for lista in self._products:
            total += lista[0].get_price() * lista[1]
        return total
        
    def get_quantidade_itens(self):
        return len(self._products)