#!/usr/bin/env python3
"""Compute and print Nginx log stats from MongoDB.

Connects to ``127.0.0.1:27017`` and queries ``logs.nginx`` to print total logs,
per-method counts, and the GET ``/status`` count. Run after restoring the
dataset (e.g., ``mongorestore dump``).
"""
from pymongo import MongoClient


def helper(a: dict) -> int:
    """Return count of documents in ``logs.nginx`` matching filter ``a``."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(a)


def main():
    """Print total logs, per-method counts, and GET ``/status`` count."""
    print(f"{helper({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {helper({'method': 'GET'})}")
    print(f"\tmethod POST: {helper({'method': 'POST'})}")
    print(f"\tmethod PUT: {helper({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {helper({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {helper({'method': 'DELETE'})}")
    print(f"{helper({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()