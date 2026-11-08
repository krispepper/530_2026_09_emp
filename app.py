from flask import Flask, render_template
from queries import(get_employees)


app = Flask(__name__)

@app.route('/')
def employees_page():
    employees = get_employees()
    employee_html = ""
    for employee in employees:
        employee_html += f"""<p>
        Employee ID: {employee['employeeID']} <tr>
        First Name: {employee['firstName']} <tr>
        Last Name: {employee['lastName']} <tr>
        </p>
        """
    print(employees)
    
    return f"""<html>
    <head>
    <title>Employee List</title>
    </head>
    <body>
    <h1>Employee List</h1>
    {employee_html}
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5001)