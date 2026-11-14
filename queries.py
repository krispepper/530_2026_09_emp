from db import get_connection

def get_employees():
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
    sql = '''
    SELECT * FROM Employees
    '''
    sql = sql + ' WHERE EmployeeID =' + str(employeeID)
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee