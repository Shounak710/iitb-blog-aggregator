# Configuration file for database
# Make sure user has CREATEDB priviledge.
DB_USER = 'admin'
DB_PASS = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'
DB_ARTICLE = 'articles'

# DB_NAME is only for setup
# Change this variable to connect to a database for initial setup only
DB_NAME = 'postgres'

# Can add or remove columns
# You might want to have a look at the variable "values" in the dnHandler file if you change columns
# "LINK" Column must remain at 0 index.
DB_TABLE  = 'items'
DB_COLUMNS = [
				'LINK',
				'FEED',
				'TITLE',
				'SUMMARY',
				'AUTHOR_EMAIL',
				'AUTHOR_NAME',
				'HASH'
			]

DB_COLUMNS_MODIFIERS = [
						'text NOT NULL UNIQUE',
						'text NOT NULL',
						'text NOT NULL',
						'text',
						'text',
						'text',
						'text'
					]