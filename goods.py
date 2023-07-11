from connection import *


class Goods:
    def __init__(self):
        self.connection = SQLiteConnection("goods.db")
        self.connection.connect()

    def goods_insert(self, goods_name, goods_no):
        query = "INSERT INTO goods (goods_name, goods_no) VALUES (?, ?)"
        self.connection.execute_query(query, goods_name, goods_no)
        self.connection.close()

    def goods_fetch_id(self, goods_id):
        query = "SELECT * FROM goods WHERE goods_id = ?"
        self.connection.execute_query(query, goods_id)
        row = self.connection.fetch_one()
        self.connection.close()
        return row

    def goods_fetch_all(self):
        query = "SELECT * FROM goods"
        self.connection.execute_query(query)
        rows = self.connection.fetch_all()
        self.connection.close()
        return rows
