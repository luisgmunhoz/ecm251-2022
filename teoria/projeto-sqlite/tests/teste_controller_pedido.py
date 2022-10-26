from src.controllers.pedido_controller import PedidoController

controller = PedidoController()
# Exibe os itens de um pedido_controller
resultado = controller.pegar_pedido("001")
print(resultado)


for elemento in resultado:
    print(elemento)

item_pedido = resultado[0]
item_pedido.quantidade = 10
controller.atualizar_pedido(item_pedido)
print("#" * 80)
resultado = controller.pegar_pedido("001")
for elemento in resultado:
    print(elemento)