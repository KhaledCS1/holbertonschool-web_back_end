# Node.js Basic

This project demonstrates fundamental Node.js concepts including file I/O, HTTP servers, and Express.js framework.

## 📁 Files Overview

| File | Description |
|------|-------------|
| `0-console.js` | Simple console output function |
| `1-stdin.js` | Interactive command-line input handling |
| `2-read_file.js` | Synchronous CSV file reading and parsing |
| `3-read_file_async.js` | Asynchronous CSV file reading with Promises |
| `4-http.js` | Basic HTTP server implementation |
| `5-http.js` | HTTP server with CSV data endpoints |
| `6-http_express.js` | Basic Express.js server |
| `7-http_express.js` | Express.js server with student data API |
| `full_server/` | Complete MVC server implementation |

## 🚀 How to Run

### Basic Functions

#### Console Output (0-console.js)
```bash
node -e "require('./0-console')('Hello Holberton School!')"
```

#### Interactive Input (1-stdin.js)
```bash
node 1-stdin.js
# Type your name and press Enter
```

#### File Reading - Sync (2-read_file.js)
```bash
node -e "require('./2-read_file')('database.csv')"
```

#### File Reading - Async (3-read_file_async.js)
```bash
node -e "require('./3-read_file_async')('database.csv')"
```

### HTTP Servers

#### Basic HTTP Server (4-http.js)
```bash
# Start server
node 4-http.js

# Test in another terminal
curl http://127.0.0.1:1245/
```

#### HTTP Server with Data (5-http.js)
```bash
# Start server with database
node 5-http.js database.csv

# Test endpoints
curl http://127.0.0.1:1245/
curl http://127.0.0.1:1245/students
```

#### Express.js Basic (6-http_express.js)
```bash
# Start Express server
node 6-http_express.js

# Test
curl http://127.0.0.1:1245/
```

#### Express.js with Data (7-http_express.js)
```bash
# Start Express server with database
node 7-http_express.js database.csv

# Test endpoints
curl http://127.0.0.1:1245/
curl http://127.0.0.1:1245/students
```

#### Full Server (full_server/)
```bash
# Start complete MVC server
node full_server/server.js full_server/database.csv

# Test endpoints
curl http://127.0.0.1:1245/
curl http://127.0.0.1:1245/students
curl http://127.0.0.1:1245/students/CS
curl http://127.0.0.1:1245/students/SWE
```

## 📊 Database Format

The `database.csv` file should follow this format:
```csv
firstname,lastname,age,field
Johann,Kepler,29,CS
Arielle,Dray,24,CS
Jonathan,Milhaud,27,CS
...
```

### Requirements:
- Header row with at least `firstname` and `field` columns
- Trailing blank lines are ignored
- Invalid rows (missing firstname or field) are skipped

## 🔧 Features Demonstrated

### File Operations
- **Synchronous file reading** with error handling
- **Asynchronous file reading** with Promises
- **CSV parsing** and data validation
- **Student counting** and grouping by field

### HTTP Concepts
- **Basic HTTP server** creation
- **Routing** and endpoint handling
- **Request/Response** processing
- **Error handling** for missing files

### Express.js Framework
- **Express app** setup and configuration
- **Route definition** and middleware
- **JSON responses** and data formatting
- **Static content** serving

### Advanced Patterns
- **MVC architecture** in full_server
- **Modular code** organization
- **Environment-based** server configuration
- **RESTful API** design

## 📝 Expected Output Examples

### Student Count Output:
```
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```

### HTTP Responses:
```
GET / → "Hello Holberton School!"
GET /students → Student count and list by field
```

## ⚠️ Notes

- All servers run on port **1245**
- CSV files must include header row
- Empty lines in CSV are automatically ignored
- Error handling includes "Cannot load the database" for missing files
- Use `Ctrl+C` to stop running servers

## 🎯 Learning Objectives

After completing this project, you should understand:
- Node.js fundamentals and modules
- File system operations (sync vs async)
- HTTP server creation and routing
- Express.js framework basics
- CSV data parsing and manipulation
- Error handling and validation
- MVC architecture patterns

---

**Author:** Khaled  
**Environment:** Node.js v24.7.0  
**Framework:** Express.js  
**Language:** JavaScript
