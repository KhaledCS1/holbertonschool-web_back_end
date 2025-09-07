# Full Server - MVC Architecture

A complete Express.js server implementation following MVC (Model-View-Controller) architecture pattern.

## 🏗️ Project Structure

```
full_server/
├── controllers/          # Request handlers
│   ├── AppController.js  # Home page controller
│   └── StudentsController.js  # Student data controller
├── routes/              # Route definitions
│   └── index.js         # Main router configuration
├── utils.js             # Utility functions
├── database.csv         # Student data
├── server.js            # Express app entry point
└── README.md           # This file
```

## 🚀 How to Run

### From project root:
```bash
node Node_JS_basic/full_server/server.js Node_JS_basic/full_server/database.csv
```

### From Node_JS_basic directory:
```bash
node full_server/server.js full_server/database.csv
```

### From full_server directory:
```bash
node server.js database.csv
```

## 🌐 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Welcome message | `Hello Holberton School!` |
| `GET` | `/students` | All students grouped by field | Student count and lists |
| `GET` | `/students/CS` | Computer Science students only | `List: [CS students]` |
| `GET` | `/students/SWE` | Software Engineering students only | `List: [SWE students]` |

## 📊 Response Examples

### GET /
```
Hello Holberton School!
```

### GET /students
```
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```

### GET /students/CS
```
List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
```

### GET /students/SWE
```
List: Guillaume, Joseph, Paul, Tommy
```

### Error Responses
```
Major parameter must be CS or SWE
Cannot load the database
```

## 🔧 Architecture Components

### Controllers
- **AppController**: Handles homepage requests
- **StudentsController**: Manages student data operations

### Routes
- **index.js**: Centralizes all route definitions
- RESTful API design with proper HTTP methods

### Utils
- **readDatabase()**: Asynchronous CSV file reading
- Data parsing and validation
- Error handling for file operations

### Server
- **Express.js** application setup
- **Port 1245** configuration
- **Environment-based** listening (skips in test mode)

## 📋 Database Requirements

The CSV file must include:
- **Header row** with `firstname` and `field` columns
- **Valid data rows** (empty lines ignored)
- **Supported fields**: CS, SWE

### Sample Format:
```csv
firstname,lastname,age,field
Johann,Kepler,29,CS
Arielle,Dray,24,CS
Guillaume,Salou,23,SWE
Joseph,Crispon,34,SWE
```

## 🧪 Testing

### Manual Testing
```bash
# Start server
node server.js database.csv

# Test endpoints (in another terminal)
curl http://localhost:1245/
curl http://localhost:1245/students
curl http://localhost:1245/students/CS
curl http://localhost:1245/students/SWE
curl http://localhost:1245/students/INVALID
```

### Environment Configuration
- **Development**: Server listens on port 1245
- **Test** (`NODE_ENV=test`): Server doesn't listen (for unit tests)

## 🎯 Key Features

### MVC Pattern
- **Separation of concerns** between routes, controllers, and utilities
- **Modular architecture** for maintainability
- **Clean code organization** following best practices

### Asynchronous Operations
- **Promise-based** file reading
- **Non-blocking** CSV parsing
- **Error handling** with try/catch

### RESTful API
- **Resource-based** URLs (`/students`, `/students/:major`)
- **HTTP status codes** for different responses
- **JSON/text** response formatting

### Error Handling
- **File not found** scenarios
- **Invalid major** parameter validation
- **Graceful error** responses

## 🔍 Troubleshooting

### Common Issues:
1. **Port already in use**: Kill existing Node processes
2. **File not found**: Check CSV file path
3. **Invalid responses**: Verify CSV format and headers

### Debug Commands:
```bash
# Check running Node processes
ps aux | grep node

# Kill specific process
pkill -f "node.*server.js"

# Check file permissions
ls -la database.csv
```

---

**Author:** Khaled  
**Framework:** Express.js  
**Architecture:** MVC Pattern  
**Port:** 1245 Quick Guide

Run
- node Node_JS_basic/full_server/server.js Node_JS_basic/full_server/database.csv

Endpoints
- GET / → Hello Holberton School!
- GET /students → Aggregated list by field (CS, SWE)
- GET /students/:major → CS or SWE only (returns "List: ...")

Notes
- CSV must include header with firstname and field columns.
- In tests, server won’t listen (NODE_ENV=test).
