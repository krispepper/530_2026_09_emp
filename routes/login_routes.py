# Author: Branson Jamanram
# Description: Creates the python flask code for employee login
# Displays the employee login first and last name in a drop down menu
# Along side their role which will direct them into their dashboard
# Associated with their role
# Moved into a Blueprint (routes/login_routes.py) so the whole app runs from app.py.

from flask import Blueprint, render_template, request
from models.employee import (get_employees, get_employeesID)

login_bp = Blueprint('login', __name__)

# Login page: drop-downs to pick your role and name
@login_bp.route("/")
def login_page():
    employees = get_employees()
    return render_template('login.html', employees = employees)

# Login submit: if the role matches the employee, open their dashboard
@login_bp.route("/login", methods = ['POST'])
def login_successful():
    employees = get_employees()

    employeeID = request.form['employeeID']
    role = request.form['role']
    employee = get_employeesID(employeeID)

    if employee and employee["role"] == role:
            return render_template("dashboard.html", employees = employees)
    else:
        return render_template("login.html", employees = employees)
