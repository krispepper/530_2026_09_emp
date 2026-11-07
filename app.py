from flask import Flask, render_template
from queries import(get_employees)


app = Flask(__name__)

@app.route('/Employees')
def employees_page():
    employees = get_employees()
    print(employees)
    return render_template('employees.html', employee_list=employees)


if __name__ == '__main__':
    app.run(debug=True, port=5001)