# ES6 Promises

This project demonstrates ES6 Promise functionality and asynchronous JavaScript programming concepts.

## 📁 Files Overview

| File | Description |
|------|-------------|
| `0-promise.js` | Basic Promise creation and resolution |
| `1-promise.js` | Promise with conditional resolve/reject logic |
| `2-then.js` | Promise chaining with .then() and .catch() |
| `3-all.js` | Using Promise.all() for concurrent operations |
| `4-user-promise.js` | Simple resolved Promise with user data |
| `5-photo-reject.js` | Promise rejection handling |
| `6-final-user.js` | Complex Promise handling with multiple operations |
| `7-load_balancer.js` | Promise.race() for load balancing scenarios |
| `8-try.js` | Error handling with try/catch in async functions |
| `9-try.js` | Advanced async/await error handling patterns |

## 🚀 ES6 Promise Features Covered

### 1. Promise Fundamentals
- **Promise Constructor**: `new Promise((resolve, reject) => {})`
- **Promise States**: Pending, Fulfilled, Rejected
- **Promise Resolution**: `resolve()` and `reject()`

### 2. Promise Methods
- **`.then()`**: Handle successful resolution
- **`.catch()`**: Handle errors and rejections
- **`.finally()`**: Execute code regardless of outcome

### 3. Promise Utilities
- **`Promise.all()`**: Wait for all promises to complete
- **`Promise.race()`**: Return first completed promise
- **`Promise.resolve()`**: Create resolved promise
- **`Promise.reject()`**: Create rejected promise

### 4. Async/Await
- **`async` functions**: Return promises automatically
- **`await` keyword**: Wait for promise resolution
- **Error handling**: try/catch with async/await

## 💡 Usage Examples

### Basic Promise Creation
```javascript
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Asynchronous operation
    if (success) {
      resolve(data);
    } else {
      reject(new Error('Operation failed'));
    }
  });
}
```

### Promise Chaining
```javascript
getResponseFromAPI()
  .then(response => {
    console.log('Success:', response);
    return processResponse(response);
  })
  .then(processed => {
    console.log('Processed:', processed);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

### Promise.all() for Concurrent Operations
```javascript
Promise.all([uploadPhoto(), createUser()])
  .then(results => {
    const [photo, user] = results;
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  })
  .catch(() => {
    console.log('System offline');
  });
```

### Promise.race() for Load Balancing
```javascript
function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
```

### Async/Await Pattern
```javascript
async function handleUserData() {
  try {
    const user = await createUser();
    const photo = await uploadPhoto();
    return { user, photo };
  } catch (error) {
    throw new Error('User creation failed');
  }
}
```

## 🔧 How to Run

### Individual Files
```bash
# Run specific file
node 0-promise.js
node 1-promise.js
# ... etc
```

### With Test Files
```bash
# If test files exist
node 0-main.js
node 1-main.js
# ... etc
```

### Using ES6 Modules
```bash
# Run with ES6 module support
node --experimental-modules file.js
```

## 📚 Learning Objectives

After completing this project, you should understand:
- How to create and use Promises
- Promise chaining with .then() and .catch()
- Handling multiple promises with Promise.all() and Promise.race()
- Error handling in asynchronous code
- Converting callback-based code to Promises
- Using async/await for cleaner asynchronous code

## 🎯 Key Concepts Explained

### Promise States
1. **Pending**: Initial state, neither fulfilled nor rejected
2. **Fulfilled**: Operation completed successfully
3. **Rejected**: Operation failed

### Promise vs Callback
```javascript
// Callback pattern (old way)
getData(function(error, data) {
  if (error) {
    handleError(error);
  } else {
    processData(data);
  }
});

// Promise pattern (ES6 way)
getData()
  .then(data => processData(data))
  .catch(error => handleError(error));
```

### Error Propagation
- Errors automatically propagate down the promise chain
- Use `.catch()` to handle errors at any point
- Errors in `.then()` are caught by subsequent `.catch()`

### Promise.all() vs Promise.race()
- **Promise.all()**: Waits for ALL promises to resolve
- **Promise.race()**: Returns when the FIRST promise resolves

## 🔄 Common Patterns

### Error Handling Pattern
```javascript
promise
  .then(handleSuccess)
  .catch(handleError)
  .finally(cleanup);
```

### Sequential vs Parallel Execution
```javascript
// Sequential (one after another)
const result1 = await operation1();
const result2 = await operation2(result1);

// Parallel (simultaneously)
const [result1, result2] = await Promise.all([
  operation1(),
  operation2()
]);
```

### Promise Retry Pattern
```javascript
function retryOperation(operation, maxRetries) {
  return operation().catch(error => {
    if (maxRetries > 0) {
      return retryOperation(operation, maxRetries - 1);
    }
    throw error;
  });
}
```

## 🛠️ Best Practices

1. **Always handle errors**: Use `.catch()` or try/catch
2. **Return promises**: In promise chains, return the next promise
3. **Avoid nesting**: Use chaining instead of nested .then()
4. **Use async/await**: For more readable asynchronous code
5. **Handle edge cases**: Check for null/undefined values

## 🎯 Project Goals

This project helps you learn:
- **Asynchronous Programming**: Understanding non-blocking operations
- **Promise Patterns**: Common ways to structure async code
- **Error Handling**: Robust error management in async operations
- **Performance**: Optimizing async operations with concurrent execution

---

**Author:** Khaled  
**Language:** JavaScript (ES6+)  
**Environment:** Node.js  
**Focus:** Asynchronous Programming & Promises