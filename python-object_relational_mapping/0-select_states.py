#!/usr/bin/python3
import MySQLdb
from sys import argv
'''Get all states from database'''


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
