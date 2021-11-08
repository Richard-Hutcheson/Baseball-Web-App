# Import Module
import csv
import os
import pandas as pd
import pymysql
from dbconfigAPP import user

def saveCSV(dataFrame, name):
    os.chdir("../csv_cleaned")
    dataFrame.to_csv(name, index=False)


def clean_peopleCSV():
    file = 'People.csv'
    df = pd.read_csv(file, delimiter=',')

    columnNames = ['playerID', 'nameFirst', 'nameLast', 'birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity', 'deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','weight','height']

    df_clean = df[columnNames]

    df_clean = df_clean.rename(columns={"playerID" : "personID"})

    saveCSV(df_clean, file)

def clean_managerCSV():
    file = 'Managers.csv'
    file2 = 'ManagersHalf.csv'

    df = pd.read_csv(file, delimiter=',')
    df_half = pd.read_csv(file2, delimiter=',')

    df.loc[df['lgID'].isnull(), 'lgID'] = "NA"

    df.insert(loc=5, column='half', value=[None for i in range(0, df.shape[0])])
    df_half.insert(loc=10, column='plyrMgr', value=[None for i in range(0, df_half.shape[0])])

    df_half['isSeasonHalf'] = True
    df['isSeasonHalf'] = False

    df_combined = pd.concat([df, df_half])

    df_combined = df_combined.rename(columns={'playerID' : 'personID'})

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    saveCSV(df_combined, file)

def clean_playerCSV():
    out_file = 'players.csv'
    pit_file = 'Pitching.csv'
    bat_file = 'Batting.csv'
    outfield_file = 'Fielding.csv'

    df_pit_file = pd.read_csv(pit_file, delimiter=',')
    df_bat_file = pd.read_csv(bat_file, delimiter=',')
    df_outfield_file = pd.read_csv(outfield_file, delimiter=',')

def main():

    #change the current directory into folder with CSV files
    os.chdir("./csv_files")
    #get list of file names in directory
    fileList = os.listdir()

    print("cleaning People.csv...")
    clean_peopleCSV()

    print("cleaning Manager.csv...")
    os.chdir("../csv_files")
    clean_managerCSV()

    print("cleaning Players")
    os.chdir("../csv_files")
    clean_playerCSV()



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