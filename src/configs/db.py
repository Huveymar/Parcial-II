import mariadb

config = {
    'host' : 'localhost',
    'port' : 3309,
    'user' : 'root',
    'password' : 'root',
    'database' : 'asistencia',
}

DB = mariadb.connect(**config)
DB.autocommit = True