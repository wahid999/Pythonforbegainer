import sqlite3
import os
import hey
os.system('clear')

#connect to db

conn = sqlite3.connect('connect.db')

# create curser

c = conn.cursor()

#create table

c.execute("""CREATE TABLE customer (
			f_name text,
			l_name text,
			email text

			)""")
# commit our changes

conn.commit()

conn.close()


