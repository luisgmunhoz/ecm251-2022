from item import Item
from carrinho import Carrinho

item1 = Item('Carregador', 'Carrega iPhone e Android', 200.0)

item2 = Item(
    valor = 350.00,
    nome = 'Stray',
    descricao = 'gato' 
)

item3 = Item(
    valor = 350.00,
    nome = 'Stray',
    descricao = 'gato' 
)

carrinho = Carrinho()

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.remover(item1)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')
