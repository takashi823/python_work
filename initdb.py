import sqlite3

conn = sqlite3.connect("goods.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS goods (
        goods_id INTEGER PRIMARY KEY AUTOINCREMENT,
        goods_name TEXT NOT NULL,
        goods_no TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
)
query = "INSERT INTO goods (goods_name, goods_no) VALUES (?, ?)"
cursor.execute(query, ("ぬいぐるみ", "001"))
cursor.execute(query, ("プラモデル", "002"))
cursor.execute(query, ("ラジコン", "003"))
cursor.execute(query, ("Switch", "005"))
cursor.execute(query, ("プレステ5", "006"))
cursor.execute(query, ("サッカーボール", "007"))
conn.commit()
conn.close()
