import pyodbc
import json

server = 'LAPTOP-4A5K00VD'
database = 'company'
username = 'automation'
password = '123456789'

# Connect to the database
conn = None
try:

  #---------------Connection string using SQL Server authentication-----------------
  conn_string = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
   #---------------Connection string using trusted connection-----------------
  conn_string = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes'

  conn = pyodbc.connect(conn_string)
  print("Connected to SQL Server database successfully!")

  #----------------Create a cursor object and execute a query------------------
  cursor = conn.cursor()

  
  update_query = "UPDATE EMPLOYEE SET salary = 2000 WHERE EmpId=14 "
  cursor.execute(update_query)

  cursor.execute("SELECT * FROM EMPLOYEE")
  rows = cursor.fetchall()
  
  data = []
  for row in rows:
      row_dict = {}
      for i, col in enumerate(cursor.description):
          column_name = col[0]
          row_dict[column_name] = row[i]
      data.append(row_dict)

  json_data = json.dumps(data)
  print(json_data)


except pyodbc.Error as ex:
  print("Error connecting to database:", ex)

finally:
  # Always close the connection
  if conn:
      conn.close()

print("Connection closed.")



