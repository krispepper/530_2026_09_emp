# Author: Branson Jamanram
# Description: Creates the python flask code for employee login
# Displays the employee login first and last name in a drop down menu
# Along side their role which will direct them into their dashboard
# Associated with their role

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

    if employee and employee["role"] == role:
            return render_template("dashboard.html", employees = employees)
    else:
        return render_template("login.html", employees = employees)
        

if __name__ == '__main__':
    login.run(debug=True, port=5002)


