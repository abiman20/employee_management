from db_client import DB_Client

server = 'LAPTOP-4A5K00VD'
database = 'company'
username = 'automation'
password = '123456789'

db_connection = DB_Client(server,database,username,password)
db_connection.connect()

update_query =db_connection.update("UPDATE EMPLOYEE SET salary = 10 WHERE EmpId=14 ")
print(update_query)

data = db_connection.read("SELECT * FROM EMPLOYEE")
print(data)

