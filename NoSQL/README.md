# NoSQL - MongoDB

This project demonstrates MongoDB operations and Python integration with PyMongo.

## 📁 Files Overview

| File | Type | Description |
|------|------|-------------|
| `0-list_databases` | Shell Script | Lists all databases in MongoDB |
| `1-use_or_create_database` | Shell Script | Creates or uses a database named 'my_db' |
| `2-insert` | Shell Script | Inserts a document in the collection 'school' |
| `3-all` | Shell Script | Lists all documents in the collection 'school' |
| `4-match` | Shell Script | Lists documents with name="Holberton school" |
| `5-count` | Shell Script | Displays the number of documents in 'school' |
| `6-update` | Shell Script | Updates documents with name="Holberton school" |
| `7-delete` | Shell Script | Deletes documents with name="Holberton school" |
| `8-all.py` | Python | Lists all documents in a collection using PyMongo |
| `9-insert_school.py` | Python | Inserts a new document in a collection using PyMongo |

## 🚀 MongoDB Operations Covered

### 1. Database Operations
- **List databases**: `show dbs`
- **Create/Use database**: `use database_name`
- **Drop database**: `db.dropDatabase()`

### 2. Collection Operations
- **Insert documents**: `db.collection.insertOne()`, `db.collection.insertMany()`
- **Find documents**: `db.collection.find()`, `db.collection.findOne()`
- **Update documents**: `db.collection.updateOne()`, `db.collection.updateMany()`
- **Delete documents**: `db.collection.deleteOne()`, `db.collection.deleteMany()`
- **Count documents**: `db.collection.countDocuments()`

### 3. Python Integration
- **PyMongo library**: MongoDB driver for Python
- **Connection**: `MongoClient()`
- **CRUD operations**: Create, Read, Update, Delete

## 💡 Usage Examples

### MongoDB Shell Commands
```bash
# List all databases
mongo < 0-list_databases

# Create and use database
mongo < 1-use_or_create_database

# Insert document
mongo my_db < 2-insert

# Find all documents
mongo my_db < 3-all
```

### Python with PyMongo
```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.my_db
collection = db.school

# Insert document
collection.insert_one({"name": "Holberton school"})

# Find documents
docs = collection.find()
for doc in docs:
    print(doc)
```

## 🔧 Prerequisites

### Install MongoDB
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mongodb

# macOS (using Homebrew)
brew tap mongodb/brew
brew install mongodb-community
```

### Install PyMongo
```bash
pip3 install pymongo
```

### Start MongoDB Service
```bash
# Ubuntu/Debian
sudo systemctl start mongod

# macOS
brew services start mongodb-community
```

## 🎯 How to Run

### Shell Scripts
```bash
# Make scripts executable
chmod +x 0-list_databases
chmod +x 1-use_or_create_database
# ... etc

# Run MongoDB shell scripts
mongo < 0-list_databases
mongo < 1-use_or_create_database
mongo my_db < 2-insert
```

### Python Scripts
```bash
# Run Python scripts
python3 8-all.py
python3 9-insert_school.py
```

## 📚 Learning Objectives

After completing this project, you should understand:
- What NoSQL databases are and their advantages
- How to use MongoDB shell commands
- CRUD operations in MongoDB
- How to integrate MongoDB with Python using PyMongo
- Document-oriented database concepts
- Querying and filtering documents

## 🎯 Project Goals

This project helps you learn:
- **MongoDB fundamentals**: Understanding NoSQL concepts
- **Shell operations**: Direct database manipulation
- **Python integration**: Using PyMongo for application development
- **Document structure**: Working with JSON-like documents
- **Database administration**: Basic MongoDB management

## 📖 Key Concepts

- **NoSQL**: Not Only SQL - flexible schema databases
- **Documents**: JSON-like records stored in collections
- **Collections**: Groups of documents (similar to tables in SQL)
- **BSON**: Binary JSON format used by MongoDB
- **PyMongo**: Official Python driver for MongoDB

---

**Author:** Khaled  
**Language:** JavaScript (MongoDB Shell), Python  
**Database:** MongoDB  
**Environment:** Linux/macOS