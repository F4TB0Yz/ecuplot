import sqlite3

class ControllerDB:
    def __init__(self):
        self.connector = sqlite3.connect('database/ecuplot_db.db')
        self.cursor = self.connector.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = self.cursor.fetchall()
        print(tablas)

    def guardar_usuario(self, user_id):
        query = "INSERT INTO users VALUES (?, ?, ?)"

        self.cursor.execute(query, (None, user_id, None))
        self.connector.commit()

    def guardar_imagen(self, user_id, imagen):
        self.guardar_usuario(user_id)
        query = "UPDATE users SET imagen = ? WHERE user_id = ?"

        self.cursor.execute(query, (imagen, user_id))
        self.connector.commit()

ControllerDB()
