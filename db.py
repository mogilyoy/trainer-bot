import psycopg2
from config import db_uri

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

    def get_group_exercises_name(self, table_name):
        self.db.execute(f'SELECT name FROM {table_name} ORDER BY num ASC')
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


    def get_column_names(self, table_name):
        self.db.execute(f"Select * FROM {table_name} LIMIT 0")
        colnames = [desc[0] for desc in self.db.description]
        return colnames

    def __add_table(self):
        self.db.execute('CREATE TABLE user_score (user_id integer, "ходьба" varchar, "отжимания на брусьях" varchar, "скакалка" varchar, "подтягивания" varchar, "приседания" varchar, "отжимания" varchar, "бег" varchar, "приседания со штангой" varchar, "приседания в тренажере смита" varchar, "приседания со штангой на груди в тренажере смита" varchar, "гак-приседания" varchar, "жим ногами" varchar, "выпады со штангой" varchar, "выпады назад" varchar, "вышагивания на платформу" varchar, "разгибания ног" varchar, "рывок штанги на грудь" varchar, "становая тяга на прямых ногах" varchar, "румынский подъем" varchar, "гиперэкстензия для мышц бедра" varchar, "сгибание ног лежа" varchar, "сгибания ног стоя" varchar, "сгибания ног сидя" varchar, "подъемы на носки стоя" varchar, "подъемы на носки в тренажере для жимов ногами" varchar, "подъемы на носки сидя" varchar, "подтягивания на перекладине" varchar, "тяга штанги в наклоне" varchar, "тяга штанги в наклоне обратным хватом" varchar, "тяга т-штанги" varchar, "тяга гантели одной рукой в наклоне" varchar, "вертикальная тяга широким хватом" varchar, "вертикальная тяга обратным хватом" varchar, "горизонтальная тяга в блочном тренажере" varchar, "пуловер в блочном тренажере стоя" varchar, "становая тяга" varchar, "наклоны со штангой на плечах" varchar, "обратные разведения в тренажере peck-deck" varchar, "разведение гантелей в наклоне" varchar, "подъем гантелей перед собой" varchar, "разведение гантелей стоя" varchar, "подъем гантелей над головой через стороны" varchar, "жим арнольда" varchar, "жим гантелей сидя" varchar, "жим штанги сидя" varchar, "жим штанги стоя (армейский жим)" varchar, "жим штанги лежа" varchar, "жим штанги на скамье с наклоном" varchar, "жим штанги на скамье с наклоном вниз" varchar, "жим гантелей лежа" varchar, "жим гантелей на скамье с наклоном вверх" varchar, "жимгантелей на скамье с наклоном вниз" varchar, "жим от груди в тренажере сидя" varchar, "разведение гантелей лежа" varchar, "разведение гантелей на скамье с наклоном вверх" varchar, "сведения в тренажере peck-deck" varchar, "сведение в кроссовере через верхние блоки" varchar, "сведение в кроссовере через нижние блоки" varchar, "шраги со штангой" varchar, "шраги со штангой за спиной" varchar, "шраги с гантелями" varchar, "тяга штанги к подбородку" varchar, "скручивание на римском стуле" varchar, "скручивания на скамье с наклоном вниз" varchar, "скручивание на коленях в болочном тренажере" varchar, "обратные скручивания" varchar, "подъемы коленей в висе" varchar, "подъемы ног в висе" varchar, "косые скручивания" varchar, "жим штанги узким хватом лежа" varchar, "отжимания от скамьи" varchar, "французский жим лежа" varchar, "французский жим ez-штанги сидя" varchar, "французский жим в тренажере сидя" varchar, "жим к низу в блочном тренажере" varchar, "жим книзу одной рукой обратным хватом" varchar, "разгибание руки с гантелью из-за головы" varchar, "разгибания руки с гантелью в наклоне" varchar, "подъем штанги на бицепс стоя" varchar, "подъемы гантелей на бицепс стоя" varchar, "подъем гантелей на бицепс сидя" varchar, "молоток" varchar, "подъем ez-штанги на бицепс в скамье скотта" varchar, "подъем гантелей на бицепс в скамье скотта" varchar, "подъем на бицепс в блочном тренажере стоя" varchar, "сгибание рук на бицепс в кроссовере" varchar, "концентрированный подъем на бицепс" varchar, "подъем штанги на бицепс обратным хватом" varchar, "сгибания рук в запястьях" varchar);')
        self.db.connection.commit()


    def add_user_to_user_score(self, user_id):
        self.db.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        self.db.connection.commit()


    def user_exist(self, user_id):
        self.db.execute(f"SELECT user_id FROM user_score WHERE user_id = '{user_id}'")
        result = self.db.fetchone()
        if result:
            return True
        return False

    def get_user_score(self, user_id, column):
        self.db.execute(f"SELECT {column} FROM user_score WHERE user_id = '{user_id}'")
        result = self.db.fetchone()
        return result

    def add_to_user_score(self, user_id, column_name, score):
        res = list(self.get_user_score(user_id, column_name))
        if res[0]:
            res[0] += f'-{score}'
            self.db.execute(f"UPDATE user_score SET {column_name} = '{res[0]}' WHERE user_id = '{user_id}'")
            self.db.connection.commit()

        else: 
            self.db.execute(f"UPDATE user_score SET {column_name} = '{score}' WHERE user_id = '{user_id}'")
            self.db.connection.commit()

    def get_user_score_list(self, user_id, column):
        self.db.execute(f"SELECT {column} FROM user_score WHERE user_id = '{user_id}'")
        result = self.db.fetchone()
        result = result[0].split('-')
        return result


    def delete_user_result(self, user_id, column_name):
        self.db.execute(f"UPDATE user_score SET {column_name} = '0' WHERE user_id = '{user_id}'")
        self.db.connection.commit()




if __name__ == '__main__':
    db = Database(db_uri)
    db.add_to_user_score(356366758, 'отжимания', 50)
    print(db.get_user_score_list(356366758, 'отжимания'))

    