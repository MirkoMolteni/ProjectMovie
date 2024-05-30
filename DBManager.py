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
        
    def get_watchlist(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM watchlist WHERE IDUtente=%s", (user_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def add_to_watchlist(self, user_id, movie_id, movie_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM watchlist WHERE IDUtente=%s AND IDFilm=%s", (user_id, movie_id))
        result = cursor.fetchone()
        if result:
            return False
        cursor.execute("INSERT INTO watchlist (IDUtente, IDFilm, NomeFilm) VALUES (%s, %s, %s)", (user_id, movie_id, movie_name))
        self.conn.commit()
        cursor.close()
        
    def remove_from_watchlist(self, user_id, movie_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM watchlist WHERE IDUtente=%s AND IDFilm=%s", (user_id, movie_id))
        self.conn.commit()
        cursor.close()