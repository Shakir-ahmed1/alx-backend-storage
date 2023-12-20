#!/usr/bin/env python3
""" log stats for nginx """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nb = client.logs.nginx
    e = {}
    print(f"{nb.count_documents(e)} logs")
    print("Methods:")
    print(f"\tmethod GET: {nb.count_documents({'method':'GET'})}")
    print(f"\tmethod POST: {nb.count_documents({'method':'POST'})}")
    print(f"\tmethod PUT: {nb.count_documents({'method':'PUT'})}")
    print(f"\tmethod PATCH: {nb.count_documents({'method':'PATCH'})}")
    print(f"\tmethod DELETE: {nb.count_documents({'method':'DELETE'})}")
    print(f"{nb.count_documents({'method':'GET','path':'/status'})}"
          f" status check")
