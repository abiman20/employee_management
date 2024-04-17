from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/')
def root():
    return "Welcome to my API!"

# Sample Employee data
sample_employee = {
  "id": 1,
  "name": "John Doe",
  "department": "Engineering",
  "email": "john.doe@company.com"
}

# GET API to retrieve sample Employee JSON
@app.route('/employee', methods=['GET'])
def get_employee():
  return jsonify(sample_employee)


# POST API to echo back received Employee JSON
@app.route('/employee', methods=['POST'])
def post_employee():
  # Get data from request body
  data = request.get_json()

  # Check if data is valid JSON
  if data is None:
    return jsonify({"error": "Invalid JSON data"}), 400

  # Echo back the received data
  return jsonify(data)

if __name__ == '__main__':
  # Run the application in debug mode
  app.run(debug=True)