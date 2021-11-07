# Import Module
import csv
import os
import pandas as pd
import pymysql
from dbconfigAPP import user

def loadIntoDB(cur, tableName, columnNames):

    params = columnNames

    params.insert(0, tableName)

    createTable = '''CREATE TABLE IF NOT EXISTS %s ( \
        
        
    );'''

    params = [os.getcwd() + '/Person.csv']

    loadIntoDB = '''LOAD DATA INFILE %s \
            INTO TABLE discounts \
            FIELDS TERMINATED BY ',' \
            ENCLOSED BY '"' \
            LINES TERMINATED BY '\n' \
            IGNORE 1 ROWS;'''

    cur.execute(loadIntoDB, params)

def saveCSV(dataFrame, cur):
    os.chdir("../csv_cleaned")
    dataFrame.to_csv('Person.csv', index=False)


def clean_peopleCSV(files, cur):
    file = 'People.csv'
    df = pd.read_csv(file, delimiter=',')

    columns = ['playerID', 'nameFirst', 'nameLast', 'birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity', 'deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','weight','height']

    df_clean = df[columns]

    saveCSV(df_clean, cur)
    loadIntoDB(cur, 'People', columns)

def main():

    con = pymysql.connect(user=user['username'], password=user['password'], host=user['host'], db=user['db'])

    cur = con.cursor()
    #change the current directory into folder with CSV files
    os.chdir("./csv_files")
    #get list of file names in directory
    fileList = os.listdir()

    print(os.listdir())

    clean_peopleCSV(fileList, cur)

    con.close()

        # with open(file) as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     line_count = 0
        #     for row in csv_reader:
        #         #column names
        #         if line_count == 0:
        #             for col in row:
        #                 print("\t", col)
        #         # if you want to print
        #         #else:
        #             #print(row)
        #
        #         line_count += 1
        #
        #     print("Processed ", line_count, " lines\n")

if __name__ == "__main__":
    main()