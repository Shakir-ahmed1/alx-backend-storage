#!/usr/bin/env python3
""" list all documents in python"""
def list_all(mongo_collection):
    """ lists all documents in school collection"""
    results = []
    data = mongo_collection.find()
    for d in data:
        results.append(d)
    return results
