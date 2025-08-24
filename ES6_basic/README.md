# ES6 Basic Features

This project demonstrates the fundamental features of ECMAScript 6 (ES6) through practical examples.

## 📁 Files Overview

| File | Feature | Description |
|------|---------|-------------|
| `0-constants.js` | `const` & `let` | Block-scoped variable declarations |
| `1-block-scoped.js` | Block Scope | Understanding variable scope in blocks |
| `2-arrow.js` | Arrow Functions | Functions that preserve `this` context |
| `3-default-parameter.js` | Default Parameters | Function parameters with default values |
| `4-rest-parameter.js` | Rest Parameters | Collecting function arguments into an array |
| `5-spread-operator.js` | Spread Operator | Expanding arrays and strings |
| `6-string-interpolation.js` | Template Literals | String interpolation with `${}` |
| `7-getBudgetObject.js` | Property Shorthand | Object property shorthand syntax |
| `8-getBudgetCurrentYear.js` | Computed Properties | Dynamic object property names |
| `9-getFullBudget.js` | Method Shorthand | ES6 method definitions in objects |
| `10-loops.js` | `for...of` Loop | Iterating through array values |
| `11-createEmployeesObject.js` | Computed Properties | Dynamic property keys |
| `12-createReportObject.js` | Arrow Functions | Arrow functions in objects |

## 🚀 Key ES6 Features Covered

### 1. Variable Declarations
- `const` - for constants
- `let` - for block-scoped variables

### 2. Functions
- Arrow functions `() => {}`
- Default parameters
- Rest parameters `...args`

### 3. Objects
- Property shorthand `{name}` instead of `{name: name}`
- Method shorthand `method() {}` instead of `method: function() {}`
- Computed properties `{[key]: value}`

### 4. Arrays & Strings
- Spread operator `...array`
- `for...of` loops
- Template literals with `${}`

## 💡 Usage Examples

```javascript
// Arrow functions with default parameters
const greet = (name = 'World') => `Hello, ${name}!`;

// Spread operator
const combined = [...array1, ...array2];

// Object shorthand
const user = {name, age, email}; // instead of {name: name, age: age, email: email}

// Template literals
const message = `Welcome ${user.name}, you are ${user.age} years old`;
```

## 🔧 How to Run

```bash
# Navigate to the ES6_basic directory
cd ES6_basic

# Run any file with Node.js
node 0-constants.js
node 1-block-scoped.js
# ... etc
```

## 📚 Learning Objectives

After completing this project, you should understand:
- Modern JavaScript variable declarations
- ES6 function enhancements
- Object and array manipulation techniques
- Template literals for string formatting
- Modern loop constructs

## 🎯 Project Goals

This project helps you transition from ES5 to ES6 JavaScript by:
- Providing practical examples of each feature
- Demonstrating real-world use cases
- Building a foundation for modern JavaScript development

---

**Author:** Khaled  