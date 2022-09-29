import psycopg2
conn = psycopg2.connect(
    'dbname=testdb user=flouda host=192.168.122.130')
cur = conn.cursor()
cur.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cur.execute("SELECT * FROM test;")
cur.fetchall()
conn.commit()
cur.close()
conn.close()
