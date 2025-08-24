// Creates report object with employees list and method to count departments
export default function createReportObject(employeesList) {
  return ({
    allEmployees: employeesList,
    // Arrow function to count number of departments
    getNumberOfDepartments: (all) => Object.keys(all).length,
  });
}