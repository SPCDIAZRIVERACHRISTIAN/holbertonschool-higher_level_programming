#!/usr/bin/python3
import importlib
module = importlib.import_module("add_0")
add = module.add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a,b)))
