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

    # make sure half data and regular data have the same columns
    assert(len(df.columns.values) == len(df_half.columns.values))

    for i in range(0, len(df.columns.values)):
        assert(df.columns.values[i] == df_half.columns.values[i])

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

    # check to make sure the number of columns is equal
    assert(len(df_batting.columns.values) == len(df_batting_post.columns.values))

    for i in range(0, len(df_batting.columns.values)):
        assert(df_batting.columns.values[i] == df_batting_post.columns.values[i])

    df_combined = pd.concat([df_batting, df_batting_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    saveCSV(df_combined, bat_file)

def clean_pitchingCSV():
    pit_file = 'Pitching.csv'
    pit_file_post = 'PitchingPost.csv'

    # create data frames for pitching and pitching post
    df_pit = pd.read_csv(pit_file, delimiter=',')
    df_pit_post = pd.read_csv(pit_file_post, delimiter=',')

    # move the round column to the end of the row
    df_pit_post_round_col = df_pit_post.pop('round')
    df_pit_post.insert(loc=df_pit_post.shape[1], column='round', value=df_pit_post_round_col)

    # add empty stint column to the post data
    df_pit_post.insert(loc=2, column='stint', value=[None for i in range(0, df_pit_post.shape[0])])

    # add empty round column to the end of pitching data frame
    df_pit.insert(loc=df_pit.shape[1], column='round', value=[None for i in range(0, df_pit.shape[0])])

    df_pit.insert(loc=df_pit.shape[1], column='isPostSeason', value=[False for i in range(0, df_pit.shape[0])])
    df_pit_post.insert(loc=df_pit_post.shape[1], column='isPostSeason', value=[True for i in range(0, df_pit_post.shape[0])])

    # check that the pitching data and the post pitching data has the same columns
    assert(len(df_pit.columns.values) == len(df_pit_post.columns))

    for i in range(0, len(df_pit.columns.values)):
        assert(df_pit.columns.values[i] == df_pit_post.columns.values[i])

    df_combined = pd.concat([df_pit, df_pit_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    saveCSV(df_combined, pit_file)


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

    print("cleaning Pitching.csv...")
    os.chdir("../csv_files")
    clean_pitchingCSV()

if __name__ == "__main__":
    main()