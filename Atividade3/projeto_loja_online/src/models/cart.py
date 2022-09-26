import streamlit as st

class Cart():
    def __init__(self):
        self._products = []

    def adicionar(self, item, amount):
        for i in range(amount):
            if item not in self._products:
                self._products.append([item, amount])
            else:
                self._products[item] += amount
                
    def get_valor_total(self):
        total = 0
        for [item, amount] in self._products:
            total += item.get_price() * amount
        return total
        
    def get_quantidade_itens(self):
        return len(self._products)