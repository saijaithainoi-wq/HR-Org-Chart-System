from flask import Flask, jsonify, request
# This imports the classes you just pasted into the other file
from models import Location, Department, Manager, Employee

app = Flask(__name__)

# --- IN-MEMORY DATABASE (Temporary Storage) ---
locations = []
departments = []
managers = []
employees = []

# --- PRE-LOAD SAMPLE DATA ---
# Creating 1 Location
loc1 = Location(1, "Switzerland", "Basel", "Main St 1")
locations.append(loc1)

# Creating 1 Manager
mgr1 = Manager(1, "Alice", "Boss", 101)
managers.append(mgr1)

# Creating 1 Department (HR)
dept1 = Department(101, "Human Resources", 1, 1)
departments.append(dept1)

# Creating 1 Employee (Bob) who reports to Alice (ManagerID 1)
emp1 = Employee(201, "Bob", "Worker", "bob@company.com", "123-456", 101, 1)
employees.append(emp1)

@app.route('/')
def home():
    return "<h1>HR Org Chart System API is Running</h1>"

# 1. USE CASE: MANAGE EMPLOYEES
@app.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        return jsonify([e.to_json() for e in employees])
    
    if request.method == 'POST':
        data = request.json
        new_emp = Employee(
            data.get('EmployeeID'),
            data.get('FirstName'),
            data.get('LastName'),
            data.get('Email'),
            data.get('PhoneNumber'),
            data.get('DepartmentID'),
            data.get('ManagerID')
        )
        employees.append(new_emp)
        return jsonify({"message": "Employee added successfully"}), 201

# 2. USE CASE: VIEW ORG CHART
@app.route('/orgchart', methods=['GET'])
def view_org_chart():
    hierarchy = []
    # Loop through managers to find their subordinates
    for mgr in managers:
        mgr_data = mgr.to_json()
        subordinates = [e.to_json() for e in employees if e.manager_id == mgr.manager_id]
        mgr_data['Reports'] = subordinates
        hierarchy.append(mgr_data)
        
    return jsonify(hierarchy)

if __name__ == '__main__':
    app.run(debug=True)