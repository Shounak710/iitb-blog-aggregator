from rawdoglib.plugins import attach_hook
from config_db import *
import psycopg2
from pprintpp import pprint

def dbHandler(rawdog, config, articles, article_dates):
	con = psycopg2.connect(database=DB_ARTICLE, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
	cur = con.cursor()
	for article in articles :
		try :
			values = [article.entry_info['link'] if 'link' in article.entry_info else "", article.feed , article.entry_info['title'] if 'title' in article.entry_info else "", article.entry_info['summary'] if 'summary' in article.entry_info else "", article.entry_info['author_detail']['email'] if 'author_detail' in article.entry_info else "", article.entry_info['author_detail']['name'] if 'author_detail' in article.entry_info else "", article.hash]
			cur.execute("INSERT INTO "+DB_TABLE+"("+', '.join(DB_COLUMNS)+") VALUES ("+ ', '.join(['%s' for i in range(len(DB_COLUMNS))]) +");", values)
			con.commit()
		except psycopg2.IntegrityError:
			con.rollback()
			cur.execute("UPDATE " + DB_TABLE + " SET "+ '=%s, '.join(DB_COLUMNS[1:]) +"=%s WHERE LINK= %s", tuple(values[1:]) + (values[0],))
	con.commit()
	con.close()
	
	return False

attach_hook("output_write_files", dbHandler)