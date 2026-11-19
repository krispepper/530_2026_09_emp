
/*
 Author: Cynthia Luizia
 Purpose: Filter employee dropdown options by role.

 AI Assistance Disclosure:
 Used ChatGPT to assist with developing the JavaScript functionality for filtering 
 employee names based on theselected employee role.

 Prompt used:
 "How can I use JavaScript to filter an employee name dropdown based on the 
 employee role selected in another dropdown?"

 I reviewed, tested, and adapted the generated guidance to work with my login page.
*/

function filterEmployeesByRole(selectedRole, employeeDropdown) {
    employeeDropdown.value = "";
    const employees = employeeDropdown.querySelectorAll("option");
    employees.forEach(function(employee) {
        if (employee.value === "") {
            employee.hidden = false;
            return;
        }
        employee.hidden = employee.dataset.role !== selectedRole;
    });
    employeeDropdown.disabled = !selectedRole;
}
