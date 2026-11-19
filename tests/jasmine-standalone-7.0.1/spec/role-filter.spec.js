
/*
 Author: Cynthia Luizia
 Unit Test: Employee Role Filtering
*/

describe("Employee Role Filtering", function() {
    it("should filter employees by selected role", function() {
        const dropdown = document.createElement("select");
        dropdown.innerHTML = `
            <option value="">Select Employee</option>
            <option value="1" data-role="Manager">John</option>
            <option value="2" data-role="Auditor">Mary</option>
            <option value="3" data-role="Employee">Jane</option>
        `;
        dropdown.value = "2";
        filterEmployeesByRole("Manager", dropdown);
        expect(dropdown.options[0].hidden).toBe(false);
        expect(dropdown.options[1].hidden).toBe(false);
        expect(dropdown.options[2].hidden).toBe(true);
        expect(dropdown.options[3].hidden).toBe(true);
        expect(dropdown.value).toBe("");
        expect(dropdown.disabled).toBe(false);
    });
});