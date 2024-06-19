#!/usr/bin/python3
import MySQLdb
from sys import argv
'''Get all states from database'''


def list_all_states(mysql_username, mysql_password, mysql_db):
    '''connects to a database and lists all states from the states table

    Args:
        mysql_username (string): mysql username
        mysql_password (string): mysql password
        mysql_db (string): mysql database name
    '''
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=mysql_db)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_all_states(argv[1], argv[2], argv[3])
