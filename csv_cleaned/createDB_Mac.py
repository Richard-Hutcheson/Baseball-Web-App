import pymysql as sql
from csi3335fall2021 import user
import os
import re
import subprocess

def printCursor(cur):
    count = 0
    for row in cur:
        for col in row:
            print(col, end=" ")
        print()
        count += 1
    print("Result Set Size: " + str(count))

def main():

    con = sql.connect(user=user['username'], password=user['password'], host=user['host'], db=user['db'])

    with con:

        print("\ncreating CSVs...\n")
        subprocess.call("python csvParser.py", shell=True)

        cur = con.cursor()
        SQL_Script_fname = 'baseballapp_Mac.sql'

        file = open(SQL_Script_fname, 'r')

        sqlScript = file.readlines()
        file.close()

        regexp = re.compile('^--')

        sqlScript = [i for i in sqlScript if not regexp.match(i)]

        sqlScript = ' '.join(sqlScript)

        sqlScript = sqlScript.replace('\n', ' ').replace("\\n", '\\n')

        commands = sqlScript.split(";")

        commands.pop(len(commands) - 1)

        commands = list(map(lambda a: a + ';', commands))

        print("\nbuilding database...\n")
        for i in range(0, len(commands)):
            cur.execute(commands[i])


        cur.execute("SHOW TABLES;")

        print("DB Creation Successful: ")
        printCursor(cur)



if __name__ == "__main__":
    main()