import psycopg2


connection = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    dbname = 'worldbank',
    password = '070487'
)