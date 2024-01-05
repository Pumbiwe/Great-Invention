import sqlite3


class Database:
    def __init__(self, name='database.db'):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS levels (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            summand_1 INTEGER, 
                            summand_2 INTEGER,
                            result_id INTEGER,
                            passed    INTEGER
                            );''')
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS elements (
                            id            INTEGER,
                            name          TEXT    NOT NULL,
                            color         TEXT    NOT NULL,
                            russian_title TEXT    NOT NULL
                        );""")
        
    def query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.text_factory = str
        return self.cursor.fetchall()

    def insert(self, id, name, color=None, russian_title=None):
        return self.query('INSERT INTO elements (id, name, color, russian_title) VALUES ({}, {}, {}, {})'.format(
            id, name, color, russian_title
        ))
        
    def get_levels(self):
        levels = list()
        for level in self.query('SELECT id FROM levels'):
            levels.append(level[0])
        return levels
    
    def get_elements(self):
        elements = list()
        for element in self.query('SELECT name FROM elements'):
            elements.append(element[0])
        return elements
    
    def get_color(self, name):
        return self.query('SELECT color FROM elements WHERE name = "{}"'.format(name))[0][0]
    
    def get_element(self, id):
        return self.query('SELECT * FROM elements WHERE id = {}'.format(id))[0]
    
    def get_passed_count(self):
        return self.query('SELECT SUM(passed) FROM levels')[0][0]
    
    def __del__(self):
        self.connection.close()

if __name__ == '__main__':
    
    db = Database()
    output = db.get_passed_count()
    print(output)