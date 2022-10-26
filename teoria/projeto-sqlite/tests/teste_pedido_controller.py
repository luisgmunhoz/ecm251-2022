from src.controllers.pedido_controller import PedidoController

controller = PedidoController()
# Exibe os itens de um pedido_controller
resultado = controller.pegar_pedido("00")
print(resultado)


for elemento in resultado:
    print(elemento)