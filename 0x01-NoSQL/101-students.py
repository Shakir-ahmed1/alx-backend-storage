#!/usr/bin/env python3
""" insert a document in python """


def top_students(mongo_collection):
    """ insert to school"""
    data = mongo_collection.find()
    result = []
    for d in data:
        total_score = 0
        for t in d.get('topics', []):
            total_score += t.get('score', 0)
        d['averageScore'] = total_score / len(d.get('topics', []))
        result.append(d)
    result = sorted(result, key = lambda x: x['averageScore'], reverse= True)
    return result
