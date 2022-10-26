from src.controllers.item_controller import ItemController
from src.controllers.pedido_controller import PedidoController
from src.models.item import Item
from src.models.pedido import Pedido

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

