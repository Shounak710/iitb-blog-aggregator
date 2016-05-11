DB_USER = 'admin'
DB_PASS = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'
DB_ARTICLE = 'gur'
#DB_NAME is only for setup
DB_NAME = 'postgres'

DB_TABLE  = 'items'
DB_COLUMNS = ['LINK', 'FEED', 'TITLE', 'SUMMARY', 'AUTHOR_EMAIL', 'AUTHOR_NAME', 'HASH']
DB_COLUMNS_MODIFIERS = ['text NOT NULL UNIQUE', 'text NOT NULL', 'text NOT NULL', 'text', 'text', 'text', 'text']