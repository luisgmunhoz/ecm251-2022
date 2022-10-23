from src.controllers.item_controller import ItemController
from src.controllers.pedido_controller import PedidoController
from src.models.item import Item

"""
controller =  ItemController()

items = controller.pegar_todos_itens()

for item in items:
    print(item)

print("*" * 80)
print()
novo_item = Item("OLA", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

items = controller.pegar_todos_itens()

for item in items:
    print(item)

print(80 * "-")
print("*" * 80)
print(80 * "-")
print()

item = controller.pegar_item("CAF")
print(item)

print()

item = controller.pegar_item("CAF6")
print(item)



item = controller.pegar_item("SQL")


print(controller.atualizar_item(item))


print(80 * "-")
print("*" * 80)
print(80 * "-")


items = controller.pegar_todos_itens()

for item in items:
    print(item)

print(80 * "-")
print("*" * 80)
print(80 * "-")

items = controller.buscar_todos_itens_nome("c")

print(items)
"""

controller =  PedidoController()
pedidos = controller.pegar_todos_itens()

for pedido in pedidos:
    print(pedido)

print("*" * 80)
print()


items = controller.pegar_todos_itens()

for item in items:
    print(item)

print(80 * "-")
print("*" * 80)
print(80 * "-")
print()
