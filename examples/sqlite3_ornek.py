import sqlite3
conn = sqlite3.connect('testdb.db')
cur = conn.cursor()
cur.execute('create table test(column1, column2, column3)')
print(cur.execute('select name from sqlite_master').fetchone())
cur.execute('''
    insert into test values
        ('ilk kolon', 123, 16.7),
        ('ikinci kolon', 122, 15.3)
''')
conn.commit()
print(cur.execute('select * from test').fetchall())
