from src.controllers.item_controller import ItemController
from src.controllers.pedido_controller import PedidoController
from src.models.item import Item
from src.models.pedido import Pedido
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

"""
print(80 * "-")
print("*" * 80)
print(80 * "-")

item_controller = ItemController()
items = item_controller.pegar_todos_itens()

for item in items:
    print(item)

#print(80 * "-")
#print("*" * 80)
#print(80 * "-")

#items = item_controller.buscar_todos_itens_nome("c")

#print(items)

pedido1 = Pedido("ABC", "CAF", 2, "846", "233", "23/10/2022-10:222")
pedido2 = Pedido("ABCD", "BDE", 2, "997", "3456", "23/10/2022-10:222")

controller =  PedidoController()
# controller.inserir_pedido(pedido1)
# controller.inserir_pedido(pedido2)
pedidos = controller.pegar_todos_itens()

print(80 * "-")
print("*" * 80)
print(80 * "-")

for pedido in pedidos:
    print(pedido)

print(80 * "-")
print("*" * 80)
print(80 * "-")
print()

print(controller.get_pedido("997"))

"""
items = controller.pegar_todos_itens()

for item in items:
    print(items)


"""
