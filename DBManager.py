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
        
    def get_watchlist(self, user_id, watchlist_filter):
        cursor = self.conn.cursor()
        if watchlist_filter == 0:
            cursor.execute("SELECT * FROM watchlist WHERE IDUtente=%s", (user_id,))
        else:
            cursor.execute("SELECT * FROM watchlist WHERE IDUtente=%s AND IDTipo=%s", (user_id, watchlist_filter))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def add_to_watchlist(self, user_id, movie_id, movie_name, watchlist_type):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM watchlist WHERE IDUtente=%s AND IDFilm=%s", (user_id, movie_id))
        result = cursor.fetchall()
        if len(result) == 0:
            #INSERT INTO `watchlist` (`ID`, `IDUtente`, `IDFilm`, `IDTipo`, `NomeFilm`) VALUES (NULL, '', '', '3', '')
            cursor.execute("INSERT INTO watchlist (IDUtente, IDFilm, IDTipo, NomeFilm) VALUES (%s, %s, %s, %s)", (user_id, movie_id, watchlist_type, movie_name))
            self.conn.commit()
            cursor.close()
            return True
        else:
            if result[3] == watchlist_type:
                return False
            else:
                cursor.execute("UPDATE watchlist SET IDTipo=%s WHERE ID=%s", (watchlist_type, result[0]))
                self.conn.commit()
                cursor.close()
                return True

        
    def remove_from_watchlist(self, user_id, movie_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM watchlist WHERE IDUtente=%s AND IDFilm=%s", (user_id, movie_id))
        self.conn.commit()
        cursor.close()
        
    def get_tipi(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tipi")
        result = cursor.fetchall()
        cursor.close()
        return result