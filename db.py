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

    def get_disc(self, id:int):
        self.db.execute(f"SELECT disc FROM men_program WHERE num = {id}")
        result = self.db.fetchone()
        return result[0].strip()

    def add_exercise(self, name, group, muscles, image_href, href, advice):
        self.db.execute("INSERT INTO all_exercises (name, group_name, muscles, image_href, href, advice) VALUES (%s, %s, %s, %s, %s, %s)", (name, group, muscles, image_href, href, advice))
        self.db.connection.commit()