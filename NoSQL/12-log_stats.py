#!/usr/bin/env python3
"""Log stats from Nginx collection in MongoDB.

This script connects to a local MongoDB instance (127.0.0.1:27017), reads the
`logs.nginx` collection, and prints:
- the total number of log documents,
- the count per HTTP method (GET, POST, PUT, PATCH, DELETE), and
- the number of GET requests to the "/status" path.

It is intended to be run after restoring the provided dataset with mongorestore.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = collection.count_documents({"method": m})
        print(f"    method {m}: {cnt}")

    status_cnt = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_cnt} status check")