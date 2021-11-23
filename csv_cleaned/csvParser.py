# Import Module
import csv
import os
import pandas as pd
import pymysql
from dbconfigAPP import user
import RenameColumns as cols
import numpy


def saveCSV(dataFrame, name):
    os.chdir("../csv_cleaned")
    dataFrame.to_csv(name, index=False)


def clean_peopleCSV():
    file = 'People.csv'
    df = pd.read_csv(file, delimiter=',')

    columnNames = ['playerID', 'nameFirst', 'nameLast', 'birthYear','birthMonth',
                   'birthDay','birthCountry','birthState','birthCity', 'deathYear',
                   'deathMonth','deathDay','deathCountry','deathState','deathCity',
                   'weight','height','bats','throws','debut','finalGame','retroID','bbrefID']

    df_clean = df[columnNames]

    #make sure all the columns were included in dataframe
    assert(len(df_clean.columns.values) == len(columnNames))

    for i in range(0, len(columnNames)):
        assert(df_clean.columns.values[i] == columnNames[i])

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

    df_combined.sort_values(by=['playerID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.ManagerCols, inplace=True)

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

    df_combined.sort_values(by=['yearID', 'playerID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.BattingCols, inplace=True)

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

    df_combined.rename(columns=cols.PitchingCols, inplace=True)

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

    df_combined.rename(columns=cols.FieldingCols, inplace=True)

    saveCSV(df_combined, fielding_file)


def clean_playersCSV():
    out_file = 'Players.csv'
    pit_file = 'Pitching.csv'
    bat_file = 'Batting.csv'
    outfield_file = 'Fielding.csv'

    pit_file_df = pd.read_csv(pit_file, delimiter=',')
    bat_file_df = pd.read_csv(bat_file, delimiter=',')
    field_file_df = pd.read_csv(outfield_file, delimiter=',')

    pit_file_df = pit_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])
    bat_file_df = bat_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])
    field_file_df = field_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])

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

    # TODO: MUST ADD ROUND DATA

    assert(len(pit_file_df.columns.values) == len(bat_file_df.columns.values))
    assert(len(bat_file_df.columns.values) == len(field_file_df.columns.values))

    for i in range(0, len(pit_file_df.columns.values)):
        assert (pit_file_df.columns.values[i] == bat_file_df.columns.values[i])
        assert (bat_file_df.columns.values[i] == field_file_df.columns.values[i])

    df_combined = pd.concat([pit_file_df, bat_file_df, field_file_df])

    df_combined.sort_values(by=['year', 'personID'], ascending=True, inplace=True)

    df_combined.rename(columns={'lgID' : 'leagueID'} , inplace=True)

    os.chdir("../csv_files")

    saveCSV(df_combined, out_file)

def clean_salaryCSV():
    salary_file = 'Salaries.csv'

    df_salary = pd.read_csv(salary_file, delimiter=',')

    playerID_col = df_salary.pop('playerID')
    df_salary.insert(loc=0, column='personID', value=playerID_col)

    saveCSV(df_salary, salary_file)

def clean_appearancesCSV():
    appearances_file = 'Appearances.csv'

    df_appearances = pd.read_csv(appearances_file, delimiter=',')

    playerID_col = df_appearances.pop('playerID')
    df_appearances.insert(loc=0, column='personID', value=playerID_col)

    saveCSV(df_appearances, appearances_file)

def clean_parksCSV():
    parks_file = 'Parks.csv'

    df_park = pd.read_csv(parks_file, delimiter=',')

    df_park.rename(columns={'park.key' : 'parkID',
                    'park.name' : 'parkName',
                    'park.alias' : 'parkAlias'}, inplace=True)

    saveCSV(df_park, parks_file)

def clean_teamsCSV():
    teams_file = 'Teams.csv'
    parks_file = 'Parks.csv'

    df_teams = pd.read_csv(teams_file, delimiter=',')
    os.chdir("../csv_cleaned")
    df_parks = pd.read_csv(parks_file, delimiter=',')
    os.chdir("../csv_files")

    df_teamName_col = df_teams.pop('name')

    df_teams.insert(loc=3, column='teamName', value=df_teamName_col)

    df_teams.rename(columns=cols.TeamsCols, inplace=True)

    # This code is adding park ID to teams 
    # TODO: fix conflicting park names in dictionary

    # parkName_parkID_dict = pd.Series(df_parks.parkID.values, index=[x.lower() for x in df_parks.parkName.values]).to_dict()
    #
    # df_parkAlias = df_parks[~df_parks['parkAlias'].isnull()]
    #
    # parkAlias_parkID_dict = pd.Series(df_parkAlias.parkID.values, index=[x.lower() for x in df_parkAlias.parkAlias.values]).to_dict()
    #
    # parkID_teams_col = []
    #
    # for i in df_teams.parkName.values:
    #
    #     if isinstance(i, float):
    #         parkID_teams_col.append(None)
    #         continue
    #
    #     entry = parkName_parkID_dict.get(i.lower())
    #
    #     if entry == None:
    #         entry = parkAlias_parkID_dict.get(i.lower())
    #         parkID_teams_col.append(entry)
    #     else:
    #         parkID_teams_col.append(entry)
    #
    #
    # df_teams.insert(loc=20, column='parkID', value=parkID_teams_col)

    saveCSV(df_teams, teams_file)

def clean_divisionCSV():
    div_file = 'Divisions.csv'

    df_division = pd.read_csv(div_file, delimiter=',', usecols=['rowID', 'divID', 'divisionName', 'isActive'])

    df_division.rename(columns={'divID' : 'divisionID'}, inplace=True)

    saveCSV(df_division, div_file)

def clean_leaguesCSV():
    league_file = 'Leagues.csv'

    df_league = pd.read_csv(league_file, delimiter=',')

    df_league.rename(columns={'lgID' : 'leagueID'}, inplace=True)

    saveCSV(df_league, league_file)

def clean_franchisesCSV():
    franchises_file = 'TeamsFranchises.csv'
    out_file = 'Franchises.csv'

    df_franchises = pd.read_csv(franchises_file, delimiter=',')

    saveCSV(df_franchises, out_file)

def clean_awardsCSV():
    awards_man_file = 'AwardsManagers.csv'
    awards_players_file = 'AwardsPlayers.csv'
    awards_man_share_file = 'AwardsShareManagers.csv'
    awards_players_share_file = 'AwardsSharePlayers.csv'
    out_file = 'Awards.csv'

    df_awards_man = pd.read_csv(awards_man_file, delimiter=',')
    df_awards_players = pd.read_csv(awards_players_file, delimiter=',')
    df_awards_man_share = pd.read_csv(awards_man_share_file, delimiter=',')
    df_awards_players_share = pd.read_csv(awards_players_share_file, delimiter=',')

    # make sure awards data columns are the same before combining
    assert(len(df_awards_man.columns.values) == len(df_awards_players.columns.values))

    for i in range(0, len(df_awards_man.columns.values)):
        assert(df_awards_man.columns.values[i] == df_awards_players.columns.values[i])

    df_awards_combined = pd.concat([df_awards_man, df_awards_players])

    # insert awardID Column at the front of the data frame
    personID_col = df_awards_combined.pop('playerID')
    df_awards_combined.insert(loc=3, column='playerID', value=personID_col)

    df_awards_combined.rename(columns={'playerID': 'personID'}, inplace=True)

    # make sure the share data columns is equal before combining
    assert (len(df_awards_man_share.columns.values) == len(df_awards_players_share.columns.values))

    for i in range(0, len(df_awards_man_share.columns.values)):
        assert (df_awards_man_share.columns.values[i] == df_awards_players_share.columns.values[i])

    df_awards_combined_share = pd.concat([df_awards_man_share, df_awards_players_share])

    df_awards_combined_share.rename(columns={'playerID' : 'personID'}, inplace=True)

    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='tie', value=[None for i in range(0, df_awards_combined_share.shape[0])])
    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='notes', value=[None for i in range(0, df_awards_combined_share.shape[0])])

    df_awards_combined.insert(loc=4, column='votesFirst', value=[None for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined.insert(loc=4, column='pointsMax', value=[None for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined.insert(loc=4, column='pointsWon', value=[None for i in range(0, df_awards_combined.shape[0])])

    df_awards_combined.insert(loc=df_awards_combined.shape[1], column='isShared', value=[False for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='isShared', value=[True for i in range(0, df_awards_combined_share.shape[0])])

    assert(len(df_awards_combined.columns.values) == len(df_awards_combined_share.columns.values))

    for i in range(0, len(df_awards_combined.columns.values)):
        assert(df_awards_combined.columns.values[i] == df_awards_combined_share.columns.values[i])

    df_awards = pd.concat([df_awards_combined, df_awards_combined_share])

    df_awards.sort_values(by=['yearID', 'personID'], ascending=True, inplace=True)

    df_awards.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_awards, out_file)

def clean_schoolCSV():
    school_file = 'Schools.csv'

    df_schools = pd.read_csv(school_file, delimiter=',')

    df_schools.rename(columns={'name_full' : 'name'})

    saveCSV(df_schools, school_file)

def clean_HallOfFameCSV():
    hallOfFame_file = 'HallOfFame.csv'

    df_halloffame = pd.read_csv(hallOfFame_file, delimiter=',')

    df_halloffame.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_halloffame, hallOfFame_file)

def clean_collegePlayerCSV():
    collegePlayer_file = 'CollegePlaying.csv'

    df_collegePlayer = pd.read_csv(collegePlayer_file, delimiter=',')

    df_collegePlayer.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_collegePlayer, collegePlayer_file)

def clean_allStarOccurences():
    allStarFull_file = 'AllstarFull.csv'
    outFile = 'AllStarOccurences.csv'

    df_allstarfull = pd.read_csv(allStarFull_file, delimiter=',')

    df_allstarfull.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_allstarfull, outFile)

def clean_teamsHalfCSV():
    teamsHalf_file = 'TeamsHalf.csv'

    df_teamsHalf = pd.read_csv(teamsHalf_file, delimiter=',')

    df_teamsHalf.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_teamsHalf, teamsHalf_file)

def clean_seriesPostCSV():
    seriesPost_file = 'SeriesPost.csv'
    outFile = 'PostSeasonSeries.csv'

    df_post = pd.read_csv(seriesPost_file, delimiter=',')

    saveCSV(df_post, outFile)

def clean_fieldingOF():
    fieldingOF_file = 'FieldingOF.csv'

    df_fieldingOF = pd.read_csv(fieldingOF_file, delimiter=',')

    df_fieldingOF.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_fieldingOF, fieldingOF_file)

def clean_fieldingOFSplit():
    fieldingOFSplit_file = 'FieldingOFsplit.csv'

    df_fieldingOFSplit = pd.read_csv(fieldingOFSplit_file, delimiter=',')

    df_fieldingOFSplit.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year'}, inplace=True)

    saveCSV(df_fieldingOFSplit, fieldingOFSplit_file)


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

    # clean Players.csv dependencies: Batting.csv, Pitching.csv, Fielding.csv (in csv_cleaned)
    print("cleaning Players.csv...")
    clean_playersCSV()

    # clean Salaries.csv
    print("cleaning Salaries.csv...")
    os.chdir("../csv_files")
    clean_salaryCSV()

    # clean Appearances.csv
    print("cleaning Appearances.csv...")
    os.chdir("../csv_files")
    clean_appearancesCSV()

    # clean Parks.csv
    print("cleaning Parks.csv...")
    os.chdir("../csv_files")
    clean_parksCSV()

    # clean Teams.csv dependencies csv_cleaned/Parks.csv
    print("cleaning Teams.csv...")
    os.chdir("../csv_files")
    clean_teamsCSV()

    # clean Division.csv
    print("cleaning Division.csv...")
    os.chdir("../csv_files")
    clean_divisionCSV()

    # clean Leagues.csv
    print("cleaning Leagues.csv...")
    os.chdir("../csv_files")
    clean_leaguesCSV()

    # clean Franchises.csv
    print("cleaning Franchises.csv...")
    os.chdir("../csv_files")
    clean_franchisesCSV()

    print("cleaning Awards.csv...")
    os.chdir("../csv_files")
    clean_awardsCSV()

    print("cleaning Schools.csv...")
    os.chdir("../csv_files")
    clean_schoolCSV()

    print("cleaning HallOfFame.csv...")
    os.chdir("../csv_files")
    clean_HallOfFameCSV()

    print("cleaning CollegePlaying.csv...")
    os.chdir("../csv_files")
    clean_collegePlayerCSV()

    print("cleaning AllStarOccurences.csv...")
    os.chdir("../csv_files")
    clean_allStarOccurences()

    print("cleaning TeamsHalf.csv...")
    os.chdir("../csv_files")
    clean_teamsHalfCSV()

    print("cleaning SeriesPost.csv...")
    os.chdir("../csv_files")
    clean_seriesPostCSV()

    print("cleaning FieldingOF.csv...")
    os.chdir("../csv_files")
    clean_fieldingOF()

    print("cleaning FieldingOFSplit.csv...")
    os.chdir("../csv_files")
    clean_fieldingOFSplit()

if __name__ == "__main__":
    main()