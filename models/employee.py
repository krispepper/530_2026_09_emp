# Author: Branson Jamanram
# Description: Creates the python code for retrieving employee information
# This consists of employeeID, first name, last name, and role
# Thus allowing each employee to select their information and return it 

from models.db import get_connection

def get_employees():
    """Get every employee, ordered by employeeID.

    Returns: list of dicts (employeeID, firstName, lastName, role).
    """
    sql = '''
    SELECT * FROM Employees
    ORDER BY employeeID;
    '''
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

def get_employeesID(employeeID):
    """Get one employee by ID.

    employeeID: int or str, the employee's ID.
    Returns: dict for that employee, or None if not found.
    """
    sql = '''
    SELECT * FROM Employees
    WHERE EmployeeID = %s
    '''
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (employeeID,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee