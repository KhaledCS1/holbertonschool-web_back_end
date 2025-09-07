#!/usr/bin/env python3
"""
MongoDB Topics Update Module
Functions to update school topics in MongoDB collections
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update document with a specific attr: value
    Updates all documents where name matches the given name,
    setting their topics field to the new topics list
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })