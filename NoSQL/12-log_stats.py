#!/usr/bin/env python3
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