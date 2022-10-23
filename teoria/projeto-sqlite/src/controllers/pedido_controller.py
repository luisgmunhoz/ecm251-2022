from src.models.pedido import Pedido
from src.controllers.item_controller import ItemController
from src.dao.pedido_dao import PedidoDAO

class PedidoController:
    def __init__(self) -> None:
        pass
    
    def total_pedido(self, numero_pedido) -> float:
        items_pedido = PedidoDAO.get_instance().get_itens(numero_pedido)
        total = 0
        item_controller = ItemController()
        for (item_id, quantidade) in items_pedido:
            item = item_controller.pegar_item(item_id)
            total += item.preco * quantidade
            
    def pegar_pedido(self, id) -> Pedido:
        pedido = PedidoDAO.get_instance().pegar_pedido(id)
        return pedido

    def inserir_pedido(self, pedido) -> bool:
        try:
            PedidoDAO.get_instance().inserir_pedido(pedido)
        except:
            return False
        return True
    
    def pegar_todos_itens(self) -> list[Pedido]:
        itens = PedidoDAO.get_instance().get_all()
        return itens
    
    def get_pedido(self, numero_pedido) -> list[Pedido]:
        pedido = PedidoDAO.get_instance().get_itens(numero_pedido)
        return pedido