#!/usr/bin/env python3
"""
MongoDB School Search Module
Functions to find schools that teach specific topics
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find schools that teach a specific topic
    Returns all schools where the topics array contains the given topic
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})