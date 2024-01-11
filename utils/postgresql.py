import psycopg2


class Database():
    def __init__(self, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME):
        self.connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            result = self.cursor.fetchall()
            return result


