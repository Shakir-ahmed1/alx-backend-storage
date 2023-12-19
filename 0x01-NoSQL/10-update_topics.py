#!/usr/bin/env python3
""" update a document in python """
def update_topics(mongo_collection, name, topics):
    """ update documents's topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics" :topics}})
