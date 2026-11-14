from flask import Flask, render_template, request
from queries import (get_employees, get_employeesID)

login = Flask(__name__)

@login.route("/")
def login_page():
    employees = get_employees()
    print(employees)
    return render_template('login.html', employees = employees)

@login.route("/login", methods = ['POST'])
def login_successful():
    employees = get_employees()

    employeeID = request.form['employeeID']
    role = request.form['role']
    employee = get_employeesID(employeeID)

    if employee["role"] == role:
        # Employee ID needs to be converted to a string otherwise the statement will be false 
        # 1001 ≠ "1001"
        if str(employee["employeeID"]) == employeeID:
            return render_template("dashboard.html", employees = employees)
        
    return render_template("login.html", employees = employees)
        

if __name__ == '__main__':
    login.run(debug=True, port=5002)


