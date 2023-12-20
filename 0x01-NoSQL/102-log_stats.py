#!/usr/bin/env python3
""" log stats for nginx """
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nb = client.logs.nginx
print(f"{nb.count_documents({})} logs")
print("Methods:")
print(f"\tmethod GET: {nb.count_documents({'method':'GET'})}")
print(f"\tmethod POST: {nb.count_documents({'method':'POST'})}")
print(f"\tmethod PUT: {nb.count_documents({'method':'PUT'})}")
print(f"\tmethod PATCH: {nb.count_documents({'method':'PATCH'})}")
print(f"\tmethod DELETE: {nb.count_documents({'method':'DELETE'})}")
print(f"{nb.count_documents({'method':'GET','path':'/status'})}"
      f" status check")

all_ips = {}
data = nb.find()
for n in data:
    ip = n.get('ip')
    if ip in all_ips:
        all_ips[ip] += 1
    else:
        all_ips[ip] = 1
result = sorted(all_ips, key=lambda x: all_ips[x], reverse=True)
for r in result[:10]:
    print(f"\t{r}: {all_ips[r]}")
