import mysql.connector

class DBManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_projectmovie"
        )
    
    def check_login(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM utenti WHERE Username=%s AND Password=MD5(%s)", (username, password))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def check_register(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM utenti WHERE Username=%s", (username,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def register_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO utenti (Username, Password) VALUES (%s, MD5(%s))", (username, password))
        self.conn.commit()
        cursor.close()