#!/usr/bin/python3
""" This program stores arguments passed to the terminal """


import os
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
temp = []
if not os.path.exists("add_item.json"):
    save_to_json_file(temp, "add_item.json")
plist = sys.argv[1:]
json_list = load_from_json_file("add_item.json")
newlist = json_list + plist
save_to_json_file(newlist, "add_item.json")
