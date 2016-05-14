IIT Bombay's Blog Aggregator
===

Rawdog's documentation: http://offog.org/code/rawdog/

### Installation

Follow these steps. Here, `<home>` refers to the `iitb-blog-aggregator` directory.

* Make a virtual environment with **Python2** (Learn how to do so [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).

* Install feedparser

		pip install feedparser

* Install psycopg2
		
		pip install psycopg2

* Go to `<home>/configurations/` and do

		cp config.example config

* In the `config` file, add path to your 

	* `iitb-blog-aggregator` directory at three places (replace `<path to github folder>` aptly by <kbd>Ctrl + F</kbd>-ing).


### Installation for Database

* Install PostgreSQL 9.5 if you haven't installed before. (Get it from [here](http://www.postgresql.org/download/))

* Go to `<home>/configurations/` and do

		cp config_db.py.example config_db.py

* Open `<home>/configurations/config_db.py` and set 

	* `DB_USER` and `DB_PASS` to the username and password of the role respectively. (Make sure that the role has CREATEDB permission)

	* `DB_NAME` to the name of the database for connecting the first time.

* Go to `<home>/configurations/` and execute

		python setup_db.py

### Running


* Go to `<home>/rawdog` and run

		./rawdog

* If the above works, run the following

	./rawdog -u
	./rawdog -w

Your feed would be added/updated in the database. If it doesn't work, post on the gitter chat.

