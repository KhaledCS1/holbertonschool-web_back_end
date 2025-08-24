# ES6 Classes

This project demonstrates ES6 class syntax and object-oriented programming concepts in JavaScript.

## 📁 Files Overview

| File | Class/Feature | Description |
|------|---------------|-------------|
| `0-classroom.js` | ClassRoom | Simple class with constructor |
| `1-make_classrooms.js` | Array Creation | Function returning array of ClassRoom objects |
| `2-hbtn_course.js` | HolbertonCourse | Class with getters/setters and validation |
| `3-currency.js` | Currency | Currency class with display method |
| `4-pricing.js` | Pricing | Extended pricing functionality |
| `5-building.js` | Building | Abstract class with required method override |
| `6-sky_high.js` | SkyHighBuilding | Class inheritance extending Building |
| `7-airport.js` | Airport | Custom string representation with Symbol |
| `8-hbtn_class.js` | HolbertonClass | Custom primitive conversion |
| `9-hoisting.js` | Class Hoisting | Multiple classes and instances |
| `10-car.js` | Car | Cloning with Symbol.species |

## 🚀 Key ES6 Class Features

### 1. Basic Class Syntax
- Constructor methods
- Class properties
- Method definitions

### 2. Getters and Setters
- Property validation
- Controlled access to private properties
- Type checking

### 3. Inheritance
- `extends` keyword
- `super()` calls
- Method overriding

### 4. Symbols
- `Symbol.toStringTag`
- `Symbol.toPrimitive`
- `Symbol.species`

### 5. Static Methods
- Class-level methods
- Factory patterns

## 💡 Usage Examples

```javascript
// Basic class
const classroom = new ClassRoom(30);

// Inheritance
class Building extends AbstractBuilding {
  evacuationWarningMessage() {
    return "Please evacuate";
  }
}

// Getters/Setters
class Course {
  set name(value) {
    if (typeof value !== 'string') throw new TypeError();
    this._name = value;
  }
}
```

## 🔧 How to Run

```bash
# Navigate to ES6_classes directory
cd ES6_classes

# Run any file with Node.js
node 0-classroom.js
node 1-make_classrooms.js
# ... etc
```

## 📚 Learning Objectives

- Understand ES6 class syntax
- Implement getters and setters
- Use class inheritance with extends
- Work with static methods
- Understand Symbol usage in classes

---

**Author:** Khaled  