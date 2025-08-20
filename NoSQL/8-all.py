#!/usr/bin/env python3
"""
MongoDB collection operations - list all documents
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.
    
    Args:
        mongo_collection: A pymongo collection object
        
    Returns:
        list: A list of all documents in the collection, 
              or an empty list if no documents are found
    """
    return list(mongo_collection.find())
