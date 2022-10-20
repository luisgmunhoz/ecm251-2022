import sqlite3
from src.models.pedido import Pedido

class PedidoDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PedidoDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Pedidos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Pedido(id = resultado[0], id_item = resultado[1], id_cliente = resultado[2], quantidade = resultado[3], numero_pedido = resultado[4], data_hora = resultado[5]))
        self.cursor.close()
        return resultados

    def inserir_pedido(self, pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO Pedidos(id_item, 
                                id_cliente, 
                                quantidade, 
                                numero_pedido, 
                                data_hora
                            )
            Values(
                '{pedido.id_item}',
                '{pedido.id_cliente}',
                {pedido.quantidade},
                '{pedido.numero_pedido}',
                '{pedido.data_hora}'
            );
        """)
        self.conn.commit()
        self.cursor.close()

    def get_itens(self, numero_pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Pedidos
            WHERE numero_pedido = '{numero_pedido}';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Pedido(id = resultado[0], id_item = resultado[1], id_cliente = resultado[2], quantidade = resultado[3], numero_pedido = resultado[4], data_hora = resultado[5]))
        self.cursor.close()
        return resultados