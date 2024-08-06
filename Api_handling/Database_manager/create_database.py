import sqlite3
DB_FILE = 'memory_data.db'
def create_table():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp INTEGER,
                total INTEGER,
                free INTEGER,
                used INTEGER
            )
        ''')
    conn.commit()
    print("Database and table created successfully.")
    conn.close()
# class MemoryDatabase:
#     DB_FILE = 'memory_data.db'
#     def __init__(self):
#         self.connect = sqlite3.connect(MemoryDatabase.DB_FILE)
#         self.c = self.connect.cursor()
#         self.create_table()

#     def create_table(self):
#         try:
#             self.c.execute('''
#                 CREATE TABLE IF NOT EXISTS memory (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     timestamp INTEGER,
#                     total INTEGER,
#                     free INTEGER,
#                     used INTEGER
#                 )
#             ''')
#             self.connect.commit()
#             print("Database and table created successfully.")
#         except Exception as e:
#             print(f"Error creating database or table: {e}")

#     def __del__(self):
#         self.connect.close()
