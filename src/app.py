from fastapi import FastAPI, HTTPException
from models import Location, Department, Manager, Employee

# Initialize the app (as shown in your professor's PDF)
app = FastAPI(title="HR Org Chart System")

# --- IN-MEMORY DATABASE ---
locations = []
departments = []
managers = []
employees = []

# --- PRE-LOAD SAMPLE DATA ---
# (Same logic as before, just re-running it here)
loc1 = Location(1, "Switzerland", "Basel", "Main St 1")
locations.append(loc1)

mgr1 = Manager(1, "Alice", "Boss", 101)
managers.append(mgr1)

dept1 = Department(101, "Human Resources", 1, 1)
departments.append(dept1)

emp1 = Employee(201, "Bob", "Worker", "bob@company.com", "123-456", 101, 1)
employees.append(emp1)

# --- API ENDPOINTS (The Use Cases) ---

@app.get("/")
def home():
    return {"message": "HR Org Chart System API is Running"}

# 1. USE CASE: MANAGE EMPLOYEES
@app.get("/employees")
def list_employees():
    # FastAPI automatically converts dictionaries to JSON
    return [e.to_json() for e in employees]

@app.post("/employees")
def add_employee(data: dict):
    # In a full FastAPI app we would use Pydantic models here, 
    # but using a dict is fine for this prototype.
    new_emp = Employee(
        data['EmployeeID'],
        data['FirstName'],
        data['LastName'],
        data['Email'],
        data['PhoneNumber'],
        data['DepartmentID'],
        data['ManagerID']
    )
    employees.append(new_emp)
    return {"message": "Employee added successfully", "employee": new_emp.to_json()}

# 2. USE CASE: MANAGE DEPARTMENTS
@app.get("/departments")
def list_departments():
    return [d.to_json() for d in departments]

@app.post("/departments")
def add_department(data: dict):
    new_dept = Department(
        data['DepartmentID'],
        data['DepartmentName'],
        data['LocationID'],
        data['ManagerID']
    )
    departments.append(new_dept)
    return {"message": "Department added successfully"}

# 3. USE CASE: VIEW ORG CHART
@app.get("/orgchart")
def view_org_chart():
    hierarchy = []
    
    for mgr in managers:
        mgr_data = mgr.to_json()
        # Find all employees who report to this manager
        subordinates = [e.to_json() for e in employees if e.manager_id == mgr.manager_id]
        mgr_data['Reports'] = subordinates
        hierarchy.append(mgr_data)
        
    return hierarchy

# Note: We do NOT put app.run() at the bottom for FastAPI.
# We run it from the terminal using 'uvicorn'.