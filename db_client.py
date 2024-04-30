import pyodbc
import json

class DB_Client:

    def __init__(self,server,database,username,password):
        self.__server = server
        self.__database = database
        self.__username = username
        self.__password = password
    
    def connect(self):
        conn_string = 'DRIVER={SQL Server};SERVER='+self.__server+';DATABASE='+self.__database+';Trusted_Connection=yes'
        self.__conn = pyodbc.connect(conn_string)
        self.__cursor = self.__conn.cursor()
        print("Connected to SQL Server database successfully!")

    def update(self,query):
        self.__cursor.execute(query)

    def read(self,query):
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
  
        data = []
        for row in rows:
            row_dict = {}
            for i, col in enumerate(self.__cursor.description):
                column_name = col[0]
                row_dict[column_name] = row[i]
            data.append(row_dict)

        json_data = json.dumps(data)
        return json_data

    def close(self):
        if self.__conn:
            self.__conn.close()
            print("Connection closed.")

