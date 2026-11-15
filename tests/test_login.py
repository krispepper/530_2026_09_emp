# Author: Branson Jamanram
# Purpose: Unit test for the login page


import login

employees = [{"employeeID": 10001, "firstName": "Cynthia", "lastName": "Luizia", "role": "Auditor"}]


def test_login_successful(monkeypatch):
    monkeypatch.setattr('login.get_employees', lambda: employees)
    monkeypatch.setattr('login.get_employeesID', lambda employeeID: employees[0])
    with login.login.test_request_context("/login", method = "POST", data = {"employeeID": 10001, "role": "Auditor"}):
        success = login.login_successful()
    # Since dashboard wasnt created and was called in login, I created a temporary dashboard to test the case
    assert "Dashboard" in success


def test_wrong_role_login(monkeypatch):
    monkeypatch.setattr('login.get_employees', lambda: employees)
    monkeypatch.setattr('login.get_employeesID', lambda employeeID: employees[0])
    with login.login.test_request_context("/login", method = "POST", data = {"employeeID": 10001, "role": "Employee"}):
        success = login.login_successful()
    assert "login" in success


    

