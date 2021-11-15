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

    df_combined.rename(columns={"playerID" : "personID"}, inplace=True)

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

    df_combined.rename(columns={"playerID" : "personID"}, inplace=True)


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

    df_combined.rename(columns={"playerID" : "personID"}, inplace=True)

    saveCSV(df_combined, pit_file)

def clean_fieldingCSV():
    fielding_file = 'Fielding.csv'
    fielding_post_file = 'FieldingPost.csv'

    df_fielding = pd.read_csv(fielding_file, delimiter=',')
    df_fielding_post = pd.read_csv(fielding_post_file, delimiter=',')

    # moved round column
    fielding_post_round_col = df_fielding_post.pop('round')
    df_fielding_post.insert(loc=df_fielding_post.shape[1], column='round', value=fielding_post_round_col)

    # added empty stint column to post
    df_fielding_post.insert(loc=2, column='stint', value=[None for i in range(0, df_fielding_post.shape[0])])

    # added empty round column to the fielding table
    df_fielding.insert(loc=df_fielding.shape[1], column='round', value=[None for i in range(0, df_fielding.shape[0])])

    # added post season column
    df_fielding.insert(loc=df_fielding.shape[1], column='isPostSeason', value=[False for i in range(0, df_fielding.shape[0])])
    df_fielding_post.insert(loc=df_fielding_post.shape[1], column='isPostSeason', value=[True for i in range(0, df_fielding_post.shape[0])])

    # added empty TP column to fielding df
    df_fielding.insert(loc=13, column='TP', value=[None for i in range(0, df_fielding.shape[0])])

    # added empty WP to fielding post data
    df_fielding_post.insert(loc=15, column='WP', value=[None for i in range(0, df_fielding_post.shape[0])])

    df_fielding_post.insert(loc=18, column='ZR', value=[None for i in range(0, df_fielding_post.shape[0])])

    assert(len(df_fielding.columns.values) == len(df_fielding_post.columns.values))

    for i in range(0, len(df_fielding.columns.values)):
        assert(df_fielding.columns.values[i] == df_fielding_post.columns.values[i])

    df_combined = pd.concat([df_fielding, df_fielding_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    df_combined.rename(columns={"playerID" : "personID"}, inplace=True)

    saveCSV(df_combined, fielding_file)


def clean_playersCSV():
    out_file = 'Players.csv'
    pit_file = 'Pitching.csv'
    bat_file = 'Batting.csv'
    outfield_file = 'Fielding.csv'

    pit_file_df = pd.read_csv(pit_file, delimiter=',')
    bat_file_df = pd.read_csv(bat_file, delimiter=',')
    field_file_df = pd.read_csv(outfield_file, delimiter=',')

    pit_file_df = pit_file_df.loc[:, 'personID' : 'lgID']
    bat_file_df = bat_file_df.loc[:, 'personID' : 'lgID']
    field_file_df = field_file_df.loc[:, 'personID' : 'lgID']

    # added is pitching
    pit_file_df.insert(loc=pit_file_df.shape[1], column='isPitching', value=[True for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isPitching', value=[False for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isPitching', value=[False for i in range(0, field_file_df.shape[0])])


    pit_file_df.insert(loc=pit_file_df.shape[1], column='isBatting', value=[False for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isBatting', value=[True for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isBatting', value=[False for i in range(0, field_file_df.shape[0])])

    pit_file_df.insert(loc=pit_file_df.shape[1], column='isFielding', value=[False for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isFielding', value=[False for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isFielding', value=[True for i in range(0, field_file_df.shape[0])])

    # TODO: MUST ADD POST SEASON DATA AND ROUND DATA

    df_combined = pd.concat([pit_file_df, bat_file_df, field_file_df])

    df_combined.sort_values(by=['yearID', 'personID'], ascending=True, inplace=True)

    os.chdir("../csv_files")

    saveCSV(df_combined, out_file)



def main():

    #change the current directory into folder with CSV files
    os.chdir("./csv_files")
    #get list of file names in directory
    fileList = os.listdir()

    # clean People.csv
    print("cleaning People.csv...")
    clean_peopleCSV()

    # clean Managers.csv
    print("cleaning Managers.csv...")
    os.chdir("../csv_files")
    clean_managerCSV()

    # clean Batting.csv
    print("cleaning Batting.csv...")
    os.chdir("../csv_files")
    clean_battingCSV()

    # clean Pitching.csv
    print("cleaning Pitching.csv...")
    os.chdir("../csv_files")
    clean_pitchingCSV()

    # clean Fielding.csv
    print("cleaning Fielding.csv...")
    os.chdir("../csv_files")
    clean_fieldingCSV()

    print("cleaning Players.csv...")
    clean_playersCSV()

if __name__ == "__main__":
    main()