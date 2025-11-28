# src/models.py

class Location:
    def __init__(self, location_id, country, city, address):
        self.location_id = location_id
        self.country = country
        self.city = city
        self.address = address

    def to_json(self):
        return {
            "LocationID": self.location_id,
            "Country": self.country,
            "City": self.city,
            "Address": self.address
        }

class Manager:
    def __init__(self, manager_id, first_name, last_name, department_id):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def to_json(self):
        return {
            "ManagerID": self.manager_id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "DepartmentID": self.department_id
        }

class Department:
    def __init__(self, department_id, department_name, location_id, manager_id):
        self.department_id = department_id
        self.department_name = department_name
        self.location_id = location_id
        self.manager_id = manager_id

    def to_json(self):
        return {
            "DepartmentID": self.department_id,
            "DepartmentName": self.department_name,
            "LocationID": self.location_id,
            "ManagerID": self.manager_id
        }

class Employee:
    def __init__(self, employee_id, first_name, last_name, email, phone_number, department_id, manager_id):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.department_id = department_id
        self.manager_id = manager_id

    def to_json(self):
        return {
            "EmployeeID": self.employee_id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Email": self.email,
            "PhoneNumber": self.phone_number,
            "DepartmentID": self.department_id,
            "ManagerID": self.manager_id
        }