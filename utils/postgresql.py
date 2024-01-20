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

    def get_parda(self, id):
        try:
            self.cursor.execute(
                "SELECT parda from mijoz WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_yostiq(self, id):
        try:
            self.cursor.execute(
                "SELECT yostiq from mijoz WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_korpa(self, id):
        try:
            self.cursor.execute(
                "SELECT korpa from mijoz WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_mijoz_id(self, phone_number):
        try:
            self.cursor.execute(
                "SELECT id FROM mijoz WHERE phone_number = %s", (phone_number,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def add_zakaz(self, name, mijoz_id, boyi=None, eni=None, kvadrat=None, tayyor=False, hammasi_tayyor=False):
        try:
            self.cursor.execute(
                "INSERT INTO zakaz (name, boyi, eni, kvadrat, mijoz_id, tayyor, hammasi_tayyor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, boyi, eni, kvadrat, mijoz_id, tayyor, hammasi_tayyor),
            )
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def update_zakaz(self, boyi, eni, kvadrat, tayyor, gilam, mijoz_id):
        try:
            self.cursor.execute(
                "UPDATE zakaz SET boyi = %s, eni = %s, kvadrat = %s, tayyor = %s where name = %s AND mijoz_id = %s", (str(boyi), str(eni), str(kvadrat), tayyor, str(gilam), int(mijoz_id))
            )
            self.connection.commit()
        except Exception as e:
            print("Error: ", e)

    def update_mijoz_nomi(self, mijoz_id, yangi_nomi):
        try:
            self.cursor.execute(
                "UPDATE zakaz SET tayyor = %s WHERE mijoz_id = %s",
                (yangi_nomi, mijoz_id)
            )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Xatolik: {e}")
            self.connection.rollback()
            return False

    def update_hammasi_tayyor(self, mijoz_id, yangi_nomi):
        try:
            self.cursor.execute(
                "UPDATE zakaz SET hammasi_tayyor = %s WHERE mijoz_id = %s",
                (yangi_nomi, mijoz_id)
            )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Xatolik: {e}")
            self.connection.rollback()
            return False

    def update_pardozlash(self, mijoz_id, yangi_nomi):
        try:
            self.cursor.execute(
                "UPDATE zakaz SET pardozlash = %s WHERE mijoz_id = %s",
                (yangi_nomi, mijoz_id)
            )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Xatolik: {e}")
            self.connection.rollback()
            return False

    def get_check(self, id):
        try:
            self.cursor.execute(
                "SELECT * FROM mijoz WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()
            return result if result else None
        except Exception as e:
            print(f"Error: {e}")


    def get_check_zakaz(self, mijoz_id):
        try:
            self.cursor.execute(
                "SELECT * FROM zakaz WHERE mijoz_id = %s", (mijoz_id,)
            )
            result = self.cursor.fetchall()
            return result if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None


