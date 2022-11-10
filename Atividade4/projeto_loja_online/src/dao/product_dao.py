import sqlite3
from src.models.product import Product

class ProductDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(name = resultado[0], price = resultado[1], url = resultado[2], amount = resultado[3]))
        self.cursor.close()
        return resultados

    def insert_product(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                INSERT INTO Products Values(
                    '{product.get_name()}',
                    {product.get_price()},
                    '{product.get_url()}',
                    {product.get_amount()}
                );
                
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def update_product(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Products SET
                amount = {product.get_amount()}
                WHERE name = '{product.get_name()}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
