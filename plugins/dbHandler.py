from rawdoglib.plugins import attach_hook
from config_db import *
import psycopg2
from pprintpp import pprint

def dbHandler(rawdog, config, articles, article_dates):
	con = psycopg2.connect(database=DB_ARTICLE, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
	cur = con.cursor()
	con.commit()
	con.close()
	for article in articles :
		pprint (article.entry_info, width=1)
	return False

attach_hook("output_write_files", dbHandler)