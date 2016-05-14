# sets up the database for use
# to change configuration, go to config_db.py in <home>/rawdog/config_db.py
from config_db import *
import psycopg2

con = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
cur = con.cursor()

con.set_isolation_level(0)
forward = True
try :
	cur.execute("CREATE DATABASE " + DB_ARTICLE)
	con.commit()
	print "Database successfully created"
except psycopg2.ProgrammingError :
	con.rollback()
	print "Database already exists"
	forward = False

if forward :
	try :
		cur.execute("GRANT ALL PRIVILEGES ON DATABASE " + DB_ARTICLE + " TO " + DB_USER)
		con.commit()
		print "Granted permissions on database to the user"
	except psycopg2.ProgrammingError:
		con.rollback()
		print "Failed to grant permission"
	con.close()

	con = psycopg2.connect(database=DB_ARTICLE, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
	cur = con.cursor()

	try :
		cur.execute("CREATE TABLE " + DB_TABLE + "(ID serial PRIMARY KEY, " + ', '.join([DB_COLUMNS[i] + ' ' + DB_COLUMNS_MODIFIERS[i] for i in range(len(DB_COLUMNS))]) + ")")
		con.commit()
		print "Table successfully created"
	except psycopg2.ProgrammingError:
		con.rollback()
		print "Failed to create table"

	try :
		cur.execute("GRANT ALL PRIVILEGES ON TABLE " + DB_TABLE + " to " + DB_USER)
		con.commit()
		print "Granted permissions on tables to user"
	except psycopg2.ProgrammingError:
		con.rollback()
		print "Failed to grant privileges on table"


con.close()