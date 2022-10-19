import sqlite3
from src.models.item import Item

class ItemDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ItemDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id = resultado[0], nome = resultado[1], preco = resultado[2]))
        self.cursor.close()
        return resultados

    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens(id, nome, preco)
            Values(?,?,?);
        """, (item.id, item.nome, item.preco))
        self.conn.commit()
        self.cursor.close()