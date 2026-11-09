import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    
    cursor.execute('DROP TABLE IF EXISTS products')
    
    conn.commit()
    conn.close()
    print("Baza danych została wyczyszczona z lokalnych produktów.")

if __name__ == '__main__':
    init_db()
