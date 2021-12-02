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

    # create database SQL connection
    con = sql.connect(user=user['username'], password=user['password'], host=user['host'], db=user['db'])

    with con:
        # create database cursor
        cur = con.cursor()

        cur.execute("SELECT @@datadir;")

        databasePath = cur.fetchall()[0][0] + user['db'] + '/'
        databaseFiles = []

        # remove existing csvs to allow database to drop if needed
        if os.path.exists(databasePath):
            databaseFiles = os.listdir(databasePath)
            databaseFiles = ' '.join(databaseFiles)

            if '.csv' in databaseFiles:
                subprocess.call("rm " + databasePath + '*.csv', shell=True)

        SQL_Script_fname = 'baseballapp_Mac.sql'

        # open SQL file
        file = open(SQL_Script_fname, 'r')

        # read the SQL script
        sqlScript = file.readlines()

        # close the input file
        file.close()

        # regex match for sql comments
        regexp = re.compile('^--')

        # create SQL script without comments
        sqlScript = [i for i in sqlScript if not regexp.match(i)]

        # join the script as one string
        sqlScript = ' '.join(sqlScript)

        # replace the new line characters and preserve the '\n' for load data in file
        sqlScript = sqlScript.replace('\n', ' ').replace("\\n", '\\n')

        # split commands with array by semi colons
        commands = sqlScript.split(";")

        # remove empty line at the end of commands
        commands.pop(len(commands) - 1)

        # reconcat semi-colons back at the end of each command
        commands = list(map(lambda a: a + ';', commands))

        regexLoadTables = re.compile("^LOAD DATA INFILE")

        isCSVLoaded = False

        # execute data base commands
        print("\nbuilding database...\n")

        for i in range(0, len(commands)):

            commands[i] = commands[i].strip(' ')

            if regexLoadTables.match(commands[i]) and not isCSVLoaded:
                subprocess.call('python csvParser.py', shell=True)
                isCSVLoaded = True

            print(commands[i])
            cur.execute(commands[i])

        databaseFiles = os.listdir(databasePath)
        databaseFiles = ' '.join(databaseFiles)

        # clean up CSVs
        if '.csv' in databaseFiles:
            subprocess.call("rm " + databasePath + '*.csv', shell=True)

        # show tables from SQL
        cur.execute("SHOW TABLES;")

        # print database tables
        print("DB Creation Successful: ")
        printCursor(cur)

if __name__ == "__main__":
    main()