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

def clean_battingCSV():
    bat_file = 'Batting.csv'
    bat_post_file = 'BattingPost.csv'

    df_batting = pd.read_csv(bat_file, delimiter=',')
    df_batting_post = pd.read_csv(bat_post_file, delimiter=',')

    playerIDCol_post = df_batting_post.pop('playerID')
    df_batting_post.insert(loc=0, column='playerID', value=playerIDCol_post)

    roundCol_post = df_batting_post.pop('round')
    df_batting_post.insert(loc=21, column='round', value=roundCol_post)

    # insert empty stint column into batting_post data
    df_batting_post.insert(loc=2, column='stint', value=[None for i in range(0, df_batting_post.shape[0])])

    df_batting.insert(loc=22, column='round', value=[None for i in range(0, df_batting.shape[0])])

    # add is postSeason Column
    df_batting.insert(loc=22, column='isPostSeason', value=[False for i in range(0, df_batting.shape[0])])
    df_batting_post.insert(loc=22, column='isPostSeason', value=[True for i in range(0, df_batting_post.shape[0])])

    # check to make sure the
    assert(len(df_batting.columns.values) == len(df_batting_post.columns.values))

    df_combined = pd.concat([df_batting, df_batting_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    saveCSV(df_combined, bat_file)

def clean_pitchingCSV():
    pit_file = 'Pitching.csv'

    df_pit_file = pd.read_csv(pit_file, delimiter=',')


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

    print("cleaning Batting.csv...")
    os.chdir("../csv_files")
    clean_battingCSV()

    # print("cleaning Players...")
    # os.chdir("../csv_files")
    # clean_playerCSV()

if __name__ == "__main__":
    main()