from database import myDB

# CONEXAO COM O BANCO
host = 'localhost'
username = 'root'
password = 'root'
database = 'database'
charset = 'utf8mb4'

my_db = myDB(host, username, password, database, charset)
my_db.cleanDatabase()