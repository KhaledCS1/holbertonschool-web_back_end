# ES6 Data Manipulation

This project focuses on modern JavaScript (ES6+) data manipulation techniques using array methods, Set, Map, and typed arrays.

## 📁 Files Overview

| File | Description |
|------|-------------|
| `0-get_list_students.js` | Returns an array of student objects |
| `1-get_list_student_ids.js` | Extracts student IDs using map() |
| `2-get_students_by_loc.js` | Filters students by location using filter() |
| `3-get_ids_sum.js` | Calculates sum of student IDs using reduce() |
| `4-update_grade_by_city.js` | Updates student grades by city using map() |
| `5-typed_arrays.js` | Creates and manipulates typed arrays |
| `6-set.js` | Creates a Set from an array |
| `7-has_array_values.js` | Checks if Set contains all array values |
| `8-clean_set.js` | Filters and joins Set values with specific criteria |
| `9-groceries_list.js` | Creates a Map with groceries and quantities |
| `10-update_uniq_items.js` | Updates Map values based on conditions |

## 🚀 ES6 Features Covered

### 1. Array Methods
- **`map()`**: Transforms each element in an array
- **`filter()`**: Creates new array with elements that pass a test
- **`reduce()`**: Reduces array to a single value
- **`find()`**: Returns first element that matches criteria
- **`some()`**: Tests if at least one element passes test
- **`every()`**: Tests if all elements pass test

### 2. Set Data Structure
- **Creation**: `new Set()`
- **Add elements**: `set.add(value)`
- **Check existence**: `set.has(value)`
- **Size**: `set.size`
- **Iteration**: `for...of`, `forEach()`

### 3. Map Data Structure
- **Creation**: `new Map()`
- **Set key-value**: `map.set(key, value)`
- **Get value**: `map.get(key)`
- **Check key**: `map.has(key)`
- **Iteration**: `for...of`, `forEach()`

### 4. Typed Arrays
- **Int8Array**: 8-bit signed integers
- **Uint8Array**: 8-bit unsigned integers
- **ArrayBuffer**: Fixed-length binary data buffer

## 💡 Usage Examples

### Array Methods
```javascript
// map() - Transform data
const ids = students.map(student => student.id);

// filter() - Filter data
const localStudents = students.filter(student => student.location === 'San Francisco');

// reduce() - Aggregate data
const totalGrades = grades.reduce((sum, grade) => sum + grade, 0);
```

### Set Operations
```javascript
// Create Set
const uniqueValues = new Set([1, 2, 2, 3, 3, 4]);

// Check values
if (uniqueValues.has(2)) {
    console.log('Set contains 2');
}

// Convert to array
const arrayFromSet = [...uniqueValues];
```

### Map Operations
```javascript
// Create Map
const groceries = new Map();
groceries.set('Apples', 10);
groceries.set('Tomatoes', 10);

// Get values
const appleCount = groceries.get('Apples');

// Iterate
for (const [item, quantity] of groceries) {
    console.log(`${item}: ${quantity}`);
}
```

### Typed Arrays
```javascript
// Create ArrayBuffer
const buffer = new ArrayBuffer(10);

// Create Int8Array view
const int8View = new Int8Array(buffer);

// Set values
int8View[0] = 42;
```

## 🎯 How to Run

### Individual Files
```bash
# Run specific file
node 0-get_list_students.js
node 1-get_list_student_ids.js
# ... etc
```

### With Test Files
```bash
# If test files exist
node 0-main.js
node 1-main.js
# ... etc
```

## 📚 Learning Objectives

After completing this project, you should understand:
- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays and their use cases
- Set data structure and its methods
- Map data structure and its methods
- WeakMap and WeakSet concepts

## 🔧 Key Concepts Explained

### Array Methods vs Loops
- **Functional approach**: More readable and declarative
- **Immutability**: Methods like `map()` don't modify original array
- **Chaining**: Methods can be chained together

### Set vs Array
- **Uniqueness**: Set automatically handles duplicates
- **Performance**: Faster lookups for existence checks
- **No indexing**: Cannot access by index

### Map vs Object
- **Any key type**: Maps can use any type as key
- **Size**: Map has `.size` property
- **Iteration**: Maps are iterable by default

### Typed Arrays Benefits
- **Memory efficiency**: Fixed-size, specific data types
- **Performance**: Faster operations on numeric data
- **Interoperability**: Works with binary data formats

## 🎯 Project Goals

This project helps you learn:
- **Modern JavaScript**: ES6+ features and best practices
- **Functional programming**: Using array methods effectively
- **Data structures**: Understanding Set and Map
- **Performance**: When to use different data structures
- **Memory management**: Working with typed arrays

## 📖 Common Patterns

### Data Transformation Pipeline
```javascript
const result = data
    .filter(item => item.active)
    .map(item => ({ ...item, processed: true }))
    .reduce((acc, item) => acc + item.value, 0);
```

### Set for Deduplication
```javascript
const uniqueItems = [...new Set(arrayWithDuplicates)];
```

### Map for Caching
```javascript
const cache = new Map();
function expensiveOperation(key) {
    if (cache.has(key)) {
        return cache.get(key);
    }
    const result = doExpensiveCalculation(key);
    cache.set(key, result);
    return result;
}
```

## 🔄 Method Chaining Examples

### Student Data Processing
```javascript
// Get student IDs from San Francisco
const sfStudentIds = students
    .filter(student => student.location === 'San Francisco')
    .map(student => student.id);

// Calculate average grade
const averageGrade = students
    .map(student => student.grade)
    .filter(grade => grade !== null)
    .reduce((sum, grade, _, arr) => sum + grade / arr.length, 0);
```

### Set Operations
```javascript
// Check if all values exist in set
function hasAllValues(set, values) {
    return values.every(value => set.has(value));
}

// Clean and process set data
function cleanSet(set, startString) {
    return [...set]
        .filter(value => value.startsWith(startString))
        .map(value => value.replace(startString, ''))
        .join('-');
}
```

## 🛠️ Best Practices

1. **Use appropriate method**: Choose the right array method for the task
2. **Avoid mutations**: Prefer immutable operations
3. **Chain operations**: Combine multiple operations efficiently
4. **Handle edge cases**: Check for null/undefined values
5. **Use Set for uniqueness**: When dealing with unique values
6. **Use Map for key-value**: When you need flexible keys

## 🎯 Performance Tips

- **Set lookups**: O(1) vs Array.includes() O(n)
- **Map access**: O(1) vs Object property access
- **Typed arrays**: Better performance for numeric operations
- **Method chaining**: Readable but creates intermediate arrays

---

**Author:** Khaled  
**Language:** JavaScript (ES6+)  
**Environment:** Node.js  
**Focus:** Data Manipulation & Modern JavaScript