from django.shortcuts import render
from django.http import HttpResponse
import sys
import os

sys.path.append(os.getcwd() + "/../configurations")

from db_config import *
import psycopg2

def index(request):
	con = psycopg2.connect(
							database=DB_ARTICLE,
							user=DB_USER,
							password=DB_PASS,
							host=DB_HOST,
							port=DB_PORT)
	cur = con.cursor()
	cur.execute("SELECT * FROM " + DB_TABLE + ";")
	articles = cur.fetchall()
	ans = ""
	for article in articles:
		ans = ans + "<div>" + article[4] + "</div>"
	return HttpResponse(ans)
