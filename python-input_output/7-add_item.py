#!/usr/bin/python3
"""Script that adds all arguments to a python list."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    arg_list = []

for arg in sys.argv[1:]:
    arg_list.append(arg)

save_to_json_file(arg_list, 'add_item.json')
