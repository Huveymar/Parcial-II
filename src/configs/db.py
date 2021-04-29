import mariadb

config = {
    'host' : 'localhost',
    'port' : 3308,
    'user' : 'root',
    'password' : '',
    'database' : 'asistencia',
}

DB = mariadb.connect(**config)
DB.autocommit = True