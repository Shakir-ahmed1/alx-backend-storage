#!/usr/bin/env python3
""" enables searching by topics """


def schools_by_topic(mongo_collection, topic):
    """ search a topic in schools and return how have it"""
    data = mongo_collection.find()
    result = []
    for d in data:
        if topic in d.get('topics', []):
            result.append(d)
    return result
