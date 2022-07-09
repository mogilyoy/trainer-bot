import psycopg2

class Database():
    def __init__(self, db_uri):
        self.db_connection = psycopg2.connect(db_uri, sslmode = 'require')
        self.db = self.db_connection.cursor()

    def add_program(self, title, disc):
        self.db.execute("INSERT INTO men_program (title, disc) VALUES (%s, %s)", (title, disc))
        self.db.connection.commit()


    def get_all_programs(self):
        self.db.execute(f'SELECT * FROM men_program')
        result = self.db.fetchall()
        return result

    def get_all_programs_title(self):
        self.db.execute(f'SELECT title FROM men_program')
        result = self.db.fetchall()
        return result

