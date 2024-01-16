import psycopg2


class Database():
    def __init__(self, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT):
        self.connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        self.cursor = self.connection.cursor()

    def mijoz_exists(self, phone_number):
        with self.connection:
            self.cursor.execute("SELECT * FROM mijoz WHERE phone_number = %s", (phone_number,))
            result = self.cursor.fetchall()
            return result

    def add_mijoz(self, first_name, phone_number, gilam=None, parda=None, yostiq=None, korpa=None, adress=None):
        try:
            self.cursor.execute(
                "INSERT INTO mijoz (first_name, phone_number, gilam, parda, yostiq, korpa, adress) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (first_name, phone_number, gilam, parda, yostiq, korpa, adress),
            )
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def get_mijoz(self, id):
        try:
            self.cursor.execute(
                "SELECT gilam FROM mijoz WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
