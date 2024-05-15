#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        points = 0
        dbest = ""
        for i in my_list:
            if a_dictionary[i] > points:
                points = a_dictionary[i]
                dbest = i
        return dbest
