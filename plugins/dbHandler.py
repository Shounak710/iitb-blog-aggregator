# Uses psycopg2 library to add and update new blog entries
# To change configuration, go to config_db.py in <home>/rawdog/config_db.py
import sys
import os
from pprint import pprint
sys.path.append(os.getcwd() + "/../configurations")

from rawdoglib.plugins import attach_hook
from db_config import *
import psycopg2


def dbHandler(rawdog, config, articles, article_dates):
	con = psycopg2.connect(
							database=DB_ARTICLE,
							user=DB_USER,
							password=DB_PASS,
							host=DB_HOST,
							port=DB_PORT)
	cur = con.cursor()
	values = []
	sqlQuery = "INSERT INTO " + DB_TABLE + "(" + ', '.join(DB_COLUMNS) + ") VALUES "
	for article in articles:
		link = article.entry_info['link']
		title = ""
		summary = ""
		authorEmail = ""
		authorName = ""
		if 'author_detail' in article.entry_info:
			if 'name' in article.entry_info['author_detail']:
				authorName = article.entry_info['author_detail']['name']

		if 'author_detail' in article.entry_info:
			if 'email' in article.entry_info['author_detail']:
				authorEmail = article.entry_info['author_detail']['email']

		if 'summary' in article.entry_info:
			summary = article.entry_info['summary']

		if 'title' in article.entry_info:
			title = article.entry_info['title']

		# The values to be added in the database.
		values.extend([
						link,
						article.feed,
						title,
						summary,
						authorEmail,
						authorName,
						article.hash
					])
		sqlQuery += "(" + ', '.join(['%s' for i in range(len(DB_COLUMNS))]) + "),"

	sqlQuery = sqlQuery[:-1] + " ON CONFLICT (LINK) DO UPDATE SET " + ', '.join([column + " = EXCLUDED." + column for column in DB_COLUMNS[1:]]) + ";"
	#print sqlQuery
	try:
		cur.execute(sqlQuery, values)
		con.commit()
	except psycopg2, error:
		con.rollback()
		print error

	con.close()
	return False

#attaches the function to handle the articles parsed by rawdog
attach_hook("output_write_files", dbHandler)
