// Creates object with computed property name using ES6 syntax
export default function createEmployeesObject(departmentName, employees) {
  // [departmentName] creates dynamic property key
  return ({ [departmentName]: employees });
}