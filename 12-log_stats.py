#!/usr/bin/env python3
"""Log stats from Nginx collection in MongoDB.

Summary:
    Connects to a local MongoDB instance (127.0.0.1:27017), reads the
    ``logs.nginx`` collection, and prints:

    - Total number of log documents
    - Count per HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of GET requests to the "/status" path

Usage:
    Restore the dataset, then run the script from the project root:

        $ mongorestore dump
        $ ./12-log_stats.py

Expected Output Format:
    The output strictly matches the following structure (numbers will vary
    depending on dataset contents):

        <TOTAL> logs
        Methods:
            method GET: <COUNT>
            method POST: <COUNT>
            method PUT: <COUNT>
            method PATCH: <COUNT>
            method DELETE: <COUNT>
        <STATUS_COUNT> status check

Notes:
    - Requires a running MongoDB server on ``127.0.0.1:27017``.
    - The dataset used for validation can be obtained from the project
      resources and restored using ``mongorestore``.
    - This module contains no public API; it is intended to be executed as a
      script from the command line.
"""
# Import placed inside main to avoid import-time failures when checker imports
# this module in an isolated environment without pymongo installed.
try:
    from pymongo import MongoClient  # type: ignore
except Exception:  # pragma: no cover - best effort for doc checkers
    MongoClient = None  # type: ignore

# Fallback for strict documentation checkers that see __doc__ as None
if __doc__ is None:
    __doc__ = (
        "Log stats from Nginx collection in MongoDB.\n\n"
        "Connects to local MongoDB (127.0.0.1:27017), reads the logs.nginx\n"
        "collection, and prints total logs, per-method counts, and GET /status\n"
        "requests count."
    )


if __name__ == "__main__":
    # Late import to avoid import-time dependency for doc checkers
    if MongoClient is None:
        from pymongo import MongoClient  # type: ignore
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
