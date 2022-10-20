from src.controllers.item_controller import ItemController
from src.models.item import Item

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
item.nome = "RTX 4090"
item.preco = 13500

print(controller.atualizar_item(item))


print(controller.deletar_item(item.id))

items = controller.pegar_todos_itens()

for item in items:
    print(item)