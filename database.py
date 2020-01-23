import psycopg2
from psycopg2.extensions import STATUS_BEGIN, STATUS_READY
from credentials import (
    db_name, db_password, db_user
)

class DB:
    def __init__(self, database=db_name, user=db_user, password=db_password):
        self.conn = psycopg2.connect(database=database, user=user, password=password,)
        self.curr = self.conn.cursor()
    
    def execute(self, query):
        self.curr.execute(query)
        self.conn.commit()

    def update(self, subject, value, table='bot_users', **kwargs):
        where = ''
        if type(value) == str:
            value = f"'{value}'"
        
        for key, val in kwargs.items():
            if type(val) == type(1):
                where += f"{key}={val}"
            if type(val) == type(''):
                where += f"{key}='{val}'"

        if len(kwargs.keys()):
            where = f"WHERE {where}"

        query = f"UPDATE {table} SET {subject}={value} {where};"
        self.execute(query)


    def check_conn(self):
        print("[!] Connection succeded" if (psycopg2.extensions.STATUS_READY == self.conn.status) or (psycopg2.extensions.STATUS_BEGIN == self.conn.status) else "[!] Connecton was not established")


    # Select data you need with
    def select(self, subject='*', table='bot_users', **kwargs):
        where = ''

        for key, value in kwargs.items():
            if type(value) == type(1):
                where += f"{key}={value}"
            if type(value) == type(''):
                where += f"{key}='{value}'"

        if len(kwargs.keys()):
            where = f"WHERE {where}"


        query = f"SELECT {subject} FROM {table} {where};"
        self.curr.execute(query)
        return self.curr.fetchall()


    def add_user_bot(self, message):
        if len(self.select(user_id=message.chat.id)):
            return

        self.curr.execute("""
            INSERT INTO bot_users(user_id,username,first_name,last_name,is_bot,registered_on_site,in_game,lang,status) VALUES({},'{}','{}','{}','{}',{},{},{},{});"""
            .format(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, False, 'NULL', False, "'EN'", "'LANG_CHOOSE'")) # HERE YOU NEED TO WRITE A CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        self.conn.commit()

    
    def get_user_status(self, user_id):
        return self.select(subject='status', user_id=user_id)[0][0]

    def get_user_language(self, user_id):
        return self.select(subject='lang', user_id=user_id)[0][0]
    
    def update_status(self, user_id, status):
        self.update(subject='status', value=status, user_id=user_id)

    def update_language(self, user_id, language):
        self.update(subject='lang', value=language, user_id=user_id)


if __name__ == "__main__":
    db = DB()
    db.update_language(language='RU', user_id=11111111)
    print(db.select())
