import pyodbc
import json

class DB_Client:

    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
    
    def connect(self):
        conn_string = 'DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes'
        self.conn = pyodbc.connect(conn_string)
        self.cursor = self.conn.cursor()
        print("Connected to SQL Server database successfully!")

    def update(self,query):
        self.cursor.execute(query)

    def read(self,query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
  
        data = []
        for row in rows:
            row_dict = {}
            for i, col in enumerate(self.cursor.description):
                column_name = col[0]
                row_dict[column_name] = row[i]
            data.append(row_dict)

        json_data = json.dumps(data)
        return json_data

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")

