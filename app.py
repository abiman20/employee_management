from flask import Flask, jsonify, request
from db_client import DB_Client

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Load configuration


# Connect directly to MSSQL using pyodbc (alternative to Flask-SQLAlchemy)
import pyodbc

db_client = DB_Client('LAPTOP-4A5K00VD','company','automation','12345678')
db_client.connect()


# Define an Employee class (can replace with SQLAlchemy model if preferred)
class Employee:
    def __init__(self, id, name, department, email):
        self.id = id
        self.name = name
        self.department = department
        self.email = email

# Get all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = db_client.read("SELECT * FROM Employee") 
    return employees

# Get specific employee by ID
@app.route('/employees/<int:empid>', methods=['GET'])
def get_employees_by_id(empid):
    employees = db_client.read(f"SELECT * FROM Employee WHERE empid = {empid}")
    return employees
   


# # Create a new employee (POST request)
# @app.route('/employees', methods=['POST'])
# def create_employee():
#     data = request.get_json()
#     if not data or not data.get('name') or not data.get('department') or not data.get('email'):
#         return jsonify({'error': 'Missing required fields'}), 400

#     connection = connect_to_db()
#     if not connection:
#         return jsonify({'error': 'Failed to connect to database'}), 500

#     cursor = connection.cursor()
#     try:
#         cursor.execute("INSERT INTO Employees (name, department, email) VALUES (?, ?, ?)", (data['name'], data['department'], data['email']))
#         connection.commit()
#     except pyodbc.Error as ex:
#         connection.rollback()  # Rollback on error
#         print(ex)
#         return jsonify({'error': 'Failed to create employee'}), 500

#     close_connection(connection)
#     return jsonify({'message': 'Employee created successfully'}), 201  # Created

if __name__ == '__main__':
  # Run the application in debug mode
  app.run(debug=True)