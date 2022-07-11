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

    def add_exercise(self, num, name, group, muscles, image_href, href, advice):
        self.db.execute("INSERT INTO all_exercises (num, name, group_name, muscles, image_href, href, advice) VALUES (%s, %s, %s, %s, %s, %s, %s)", (str(num), name, group, muscles, image_href, href, advice))
        self.db.connection.commit()

    
    def get_musc_groups(self):
        self.db.execute('SELECT group_name FROM all_exercises')
        result = self.db.fetchall()
        musc = set()
        for el in result:
            musc.add(el[0].strip())

        return list(musc)

    def get_mus_table_name(self, num):
        gr_dict = {'Спина':1, 'Грудь':2, 'Пресс':4, 'Руки':3, 'Трапеция':7, 'Дельтовидные мышцы':6, 'Ноги':5}
        self.db.execute(f"SELECT group_name FROM musc_group WHERE id = {gr_dict[num]}")
        result = self.db.fetchone()
        return result[0].strip()

    def get_group_exercises_name(self, name):
        self.db.execute(f'SELECT name FROM {name} ORDER BY num ASC')
        result = self.db.fetchall()
        a = []
        for i in result:
            a.append(i[0].strip())
        return a

    def get_exercise_info(self, group, num):
        self.db.execute(f"SELECT name, group_name, muscles, image_href, href, advice FROM {group}_ex WHERE num = {num} ORDER BY num ASC")
        result = self.db.fetchone()
        inf = []
        for i in result:
            inf.append(i.strip())

        return inf