# Import Module
import csv
import os
import pandas as pd
import pymysql as sql
from csi3335fall2021 import user
import RenameColumns as cols
import numpy

def saveCSV(dataFrame, outpath):
    os.chdir("../csv_cleaned")
    dataFrame.to_csv(outpath, index=False)


def clean_peopleCSV(db_path):
    file = 'People.csv'
    df = pd.read_csv(file, delimiter=',')
    out_file = db_path + file

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

    df_clean.fillna("NULL", inplace=True)

    saveCSV(df_clean, out_file)

def clean_managerCSV(db_path):
    file = 'Managers.csv'
    file2 = 'ManagersHalf.csv'
    out_file = db_path + file

    df = pd.read_csv(file, delimiter=',')
    df_half = pd.read_csv(file2, delimiter=',')

    # pandas interprets the "NA" league id as a null value
    df.loc[df['lgID'].isnull(), 'lgID'] = "NA"

    df.insert(loc=5, column='half', value=["NULL" for i in range(0, df.shape[0])])
    df_half.insert(loc=10, column='plyrMgr', value=["NULL" for i in range(0, df_half.shape[0])])

    df_half['isSeasonHalf'] = 'Y'
    df['isSeasonHalf'] = 'N'

    # make sure half data and regular data have the same columns
    assert(len(df.columns.values) == len(df_half.columns.values))

    for i in range(0, len(df.columns.values)):
        assert(df.columns.values[i] == df_half.columns.values[i])

    df_combined = pd.concat([df, df_half])

    df_combined.sort_values(by=['playerID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.ManagerCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_combined.loc[df_combined['leagueID'].isnull(), 'leagueID'] = "NA"

    df_combined.insert(loc=0, column='ManagerRowID', value=range(1, df_combined.shape[0] + 1))

    df_combined.fillna("NULL", inplace=True)

    saveCSV(df_combined, out_file)

def clean_battingCSV(db_path):
    bat_file = 'Batting.csv'
    bat_post_file = 'BattingPost.csv'
    out_file = db_path + bat_file

    df_batting = pd.read_csv(bat_file, delimiter=',')
    df_batting_post = pd.read_csv(bat_post_file, delimiter=',')

    playerIDCol_post = df_batting_post.pop('playerID')
    df_batting_post.insert(loc=0, column='playerID', value=playerIDCol_post)

    roundCol_post = df_batting_post.pop('round')
    df_batting_post.insert(loc=21, column='round', value=roundCol_post)

    # insert empty stint column into batting_post data
    df_batting_post.insert(loc=2, column='stint', value=["NULL" for i in range(0, df_batting_post.shape[0])])

    df_batting.insert(loc=22, column='round', value=["NULL" for i in range(0, df_batting.shape[0])])

    # add is postSeason Column
    df_batting.insert(loc=22, column='isPostSeason', value=['N' for i in range(0, df_batting.shape[0])])
    df_batting_post.insert(loc=22, column='isPostSeason', value=['Y' for i in range(0, df_batting_post.shape[0])])

    # check to make sure the number of columns is equal
    assert(len(df_batting.columns.values) == len(df_batting_post.columns.values))

    for i in range(0, len(df_batting.columns.values)):
        assert(df_batting.columns.values[i] == df_batting_post.columns.values[i])

    df_combined = pd.concat([df_batting, df_batting_post])

    df_combined.sort_values(by=['yearID', 'playerID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.BattingCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_combined.loc[df_combined['leagueID'].isnull(), 'leagueID'] = "NA"

    df_combined.fillna("NULL", inplace=True)

    saveCSV(df_combined, out_file)

def clean_pitchingCSV(db_path):
    pit_file = 'Pitching.csv'
    pit_file_post = 'PitchingPost.csv'
    out_file = db_path + pit_file

    # create data frames for pitching and pitching post
    df_pit = pd.read_csv(pit_file, delimiter=',')
    df_pit_post = pd.read_csv(pit_file_post, delimiter=',')

    # move the round column to the end of the row
    df_pit_post_round_col = df_pit_post.pop('round')
    df_pit_post.insert(loc=df_pit_post.shape[1], column='round', value=df_pit_post_round_col)

    # add empty stint column to the post data
    df_pit_post.insert(loc=2, column='stint', value=["NULL" for i in range(0, df_pit_post.shape[0])])

    # add empty round column to the end of pitching data frame
    df_pit.insert(loc=df_pit.shape[1], column='round', value=["NULL" for i in range(0, df_pit.shape[0])])

    df_pit.insert(loc=df_pit.shape[1], column='isPostSeason', value=['N' for i in range(0, df_pit.shape[0])])
    df_pit_post.insert(loc=df_pit_post.shape[1], column='isPostSeason', value=['Y' for i in range(0, df_pit_post.shape[0])])

    # check that the pitching data and the post pitching data has the same columns
    assert(len(df_pit.columns.values) == len(df_pit_post.columns))

    for i in range(0, len(df_pit.columns.values)):
        assert(df_pit.columns.values[i] == df_pit_post.columns.values[i])

    df_combined = pd.concat([df_pit, df_pit_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.PitchingCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_combined.loc[df_combined['leagueID'].isnull(), 'leagueID'] = "NA"

    # change inf ERA to NULL as it is an undefined value (aka ER > 0 and no outs ER/IPOUTS)
    df_combined['EarnedRunAvg'] = df_combined['EarnedRunAvg'].astype(dtype='string')
    df_combined.loc[df_combined['EarnedRunAvg'] == 'inf', 'EarnedRunAvg'] = 'NULL'
    # df_combined['EarnedRunAvg'] = df_combined['EarnedRunAvg'].astype(dtype='float64')

    df_combined.fillna("NULL", inplace=True)

    saveCSV(df_combined, out_file)

def clean_fieldingCSV(db_path):
    fielding_file = 'Fielding.csv'
    fielding_post_file = 'FieldingPost.csv'
    out_file = db_path + fielding_file

    df_fielding = pd.read_csv(fielding_file, delimiter=',')
    df_fielding_post = pd.read_csv(fielding_post_file, delimiter=',')

    # moved round column
    fielding_post_round_col = df_fielding_post.pop('round')
    df_fielding_post.insert(loc=df_fielding_post.shape[1], column='round', value=fielding_post_round_col)

    # added empty stint column to post
    df_fielding_post.insert(loc=2, column='stint', value=["NULL" for i in range(0, df_fielding_post.shape[0])])

    # added empty round column to the fielding table
    df_fielding.insert(loc=df_fielding.shape[1], column='round', value=["NULL" for i in range(0, df_fielding.shape[0])])

    # added post season column
    df_fielding.insert(loc=df_fielding.shape[1], column='isPostSeason', value=["N" for i in range(0, df_fielding.shape[0])])
    df_fielding_post.insert(loc=df_fielding_post.shape[1], column='isPostSeason', value=["Y" for i in range(0, df_fielding_post.shape[0])])

    # added empty TP column to fielding df
    df_fielding.insert(loc=13, column='TP', value=["NULL" for i in range(0, df_fielding.shape[0])])

    # added empty WP to fielding post data
    df_fielding_post.insert(loc=15, column='WP', value=["NULL" for i in range(0, df_fielding_post.shape[0])])

    df_fielding_post.insert(loc=18, column='ZR', value=["NULL" for i in range(0, df_fielding_post.shape[0])])

    assert(len(df_fielding.columns.values) == len(df_fielding_post.columns.values))

    for i in range(0, len(df_fielding.columns.values)):
        assert(df_fielding.columns.values[i] == df_fielding_post.columns.values[i])

    df_combined = pd.concat([df_fielding, df_fielding_post])

    df_combined.sort_values(by=['yearID'], ascending=True, inplace=True)

    df_combined.rename(columns=cols.FieldingCols, inplace=True)

    # df_combined_isPostSeasonCol = df_combined.pop('isPostSeason')
    # df_combined.insert(loc=df_combined.shape[1] - 1, column='isPostSeason', value=df_combined_isPostSeasonCol)

    # df_combined['isPostSeason'] = df_combined['isPostSeason'].astype('string')

    # pandas interprets the "NA" league id as a null value
    df_combined.loc[df_combined['leagueID'].isnull(), 'leagueID'] = "NA"

    df_combined.fillna("NULL", inplace=True)

    saveCSV(df_combined, out_file)


def clean_playersCSV(db_path):
    out_file = db_path + 'Players.csv'
    pit_file = db_path + 'Pitching.csv'
    bat_file = db_path + 'Batting.csv'
    outfield_file = db_path + 'Fielding.csv'

    pit_file_df = pd.read_csv(pit_file, delimiter=',')
    bat_file_df = pd.read_csv(bat_file, delimiter=',')
    field_file_df = pd.read_csv(outfield_file, delimiter=',')

    pit_file_df = pit_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])
    bat_file_df = bat_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])
    field_file_df = field_file_df.filter(['personID','year','stint','teamID','lgID','isPostSeason'])

    # added is pitching
    pit_file_df.insert(loc=pit_file_df.shape[1], column='isPitching', value=['Y' for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isPitching', value=['N' for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isPitching', value=['N' for i in range(0, field_file_df.shape[0])])

    pit_file_df.insert(loc=pit_file_df.shape[1], column='isBatting', value=['N' for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isBatting', value=['Y' for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isBatting', value=['N' for i in range(0, field_file_df.shape[0])])

    pit_file_df.insert(loc=pit_file_df.shape[1], column='isFielding', value=['N' for i in range(0, pit_file_df.shape[0])])
    bat_file_df.insert(loc=bat_file_df.shape[1], column='isFielding', value=['N' for i in range(0, bat_file_df.shape[0])])
    field_file_df.insert(loc=field_file_df.shape[1], column='isFielding', value=['Y' for i in range(0, field_file_df.shape[0])])


    assert(len(pit_file_df.columns.values) == len(bat_file_df.columns.values))
    assert(len(bat_file_df.columns.values) == len(field_file_df.columns.values))

    for i in range(0, len(pit_file_df.columns.values)):
        assert (pit_file_df.columns.values[i] == bat_file_df.columns.values[i])
        assert (bat_file_df.columns.values[i] == field_file_df.columns.values[i])

    df_combined = pd.concat([pit_file_df, bat_file_df, field_file_df])

    df_combined.sort_values(by=['year', 'personID'], ascending=True, inplace=True)

    df_combined.fillna("NULL", inplace=True)

    os.chdir("../csv_files")

    saveCSV(df_combined, out_file)

def clean_salaryCSV(db_path):
    salary_file = 'Salaries.csv'
    out_file = db_path + salary_file

    df_salary = pd.read_csv(salary_file, delimiter=',')

    playerID_col = df_salary.pop('playerID')
    df_salary.insert(loc=0, column='personID', value=playerID_col)

    df_salary.rename(columns={'yearID' : 'year', 'lgID' : 'leagueID'}, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_salary.loc[df_salary['leagueID'].isnull(), 'leagueID'] = "NA"

    df_salary.insert(loc=0, column='salaryRowID', value=range(1, df_salary.shape[0] + 1))

    df_salary.fillna("NULL", inplace=True)

    saveCSV(df_salary, out_file)

def clean_playerPositionsCSV(db_path):
    appearances_file = 'Appearances.csv'
    out_file = db_path + 'PlayerPositions.csv'

    df_playerPos = pd.read_csv(appearances_file, delimiter=',')

    playerID_col = df_playerPos.pop('playerID')
    df_playerPos.insert(loc=0, column='personID', value=playerID_col)

    df_playerPos.rename(columns=cols.PlayerPositionsCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_playerPos.loc[df_playerPos['leagueID'].isnull(), 'leagueID'] = "NA"

    df_playerPos.insert(loc=0, column='playerPosRowID', value=range(1, df_playerPos.shape[0] + 1))

    df_playerPos.fillna("NULL", inplace=True)

    saveCSV(df_playerPos, out_file)

def clean_parksCSV(db_path):
    parks_file = 'Parks.csv'
    out_file = db_path + parks_file

    df_park = pd.read_csv(parks_file, delimiter=',')

    df_park.rename(columns={'park.key' : 'parkID',
                    'park.name' : 'parkName',
                    'park.alias' : 'parkAlias'}, inplace=True)

    df_park.fillna("NULL", inplace=True)


    saveCSV(df_park, out_file)

def clean_teamsCSV(db_path):
    teams_file = 'Teams.csv'
    parks_file = db_path + 'Parks.csv'
    out_file = db_path + teams_file

    df_teams = pd.read_csv(teams_file, delimiter=',')
    os.chdir("../csv_cleaned")
    df_parks = pd.read_csv(parks_file, delimiter=',')
    os.chdir("../csv_files")

    df_teamName_col = df_teams.pop('name')

    df_teams.insert(loc=3, column='teamName', value=df_teamName_col)

    df_teams.rename(columns=cols.TeamsCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_teams.loc[df_teams['leagueID'].isnull(), 'leagueID'] = "NA"

    df_teams.insert(loc=0, column='TeamsRowID', value=range(1, df_teams.shape[0] + 1))

    df_teams.fillna("NULL", inplace=True)

    saveCSV(df_teams, out_file)

def clean_divisionCSV(db_path):
    div_file = 'Divisions.csv'
    out_file = db_path + div_file

    df_division = pd.read_csv(div_file, delimiter=',', usecols=['rowID', 'divID', 'divisionName', 'isActive'])

    df_division.rename(columns={'divID' : 'divisionID', 'rowID' : 'DivisionRowID'}, inplace=True)

    df_division.fillna("NULL", inplace=True)

    saveCSV(df_division, out_file)

def clean_leaguesCSV(db_path):
    league_file = 'Leagues.csv'
    out_file = db_path + league_file

    df_league = pd.read_csv(league_file, delimiter=',')

    df_league.rename(columns={'lgID' : 'leagueID'}, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_league.loc[df_league['leagueID'].isnull(), 'leagueID'] = "NA"

    df_league.fillna("NULL", inplace=True)


    saveCSV(df_league, out_file)

def clean_franchisesCSV(db_path):
    franchises_file = 'TeamsFranchises.csv'
    out_file = db_path + 'Franchises.csv'

    df_franchises = pd.read_csv(franchises_file, delimiter=',')

    df_franchises.fillna("NULL", inplace=True)


    saveCSV(df_franchises, out_file)

def clean_awardsCSV(db_path):

    # awards file dependencies
    awards_man_file = 'AwardsManagers.csv'
    awards_players_file = 'AwardsPlayers.csv'
    awards_man_share_file = 'AwardsShareManagers.csv'
    awards_players_share_file = 'AwardsSharePlayers.csv'
    out_file = db_path + 'Awards.csv'

    # create dataframes of all the file dependencies
    df_awards_man = pd.read_csv(awards_man_file, delimiter=',')
    df_awards_players = pd.read_csv(awards_players_file, delimiter=',')
    df_awards_man_share = pd.read_csv(awards_man_share_file, delimiter=',')
    df_awards_players_share = pd.read_csv(awards_players_share_file, delimiter=',')

    # make sure awards data columns are the same before combining
    assert(len(df_awards_man.columns.values) == len(df_awards_players.columns.values))

    for i in range(0, len(df_awards_man.columns.values)):
        assert(df_awards_man.columns.values[i] == df_awards_players.columns.values[i])

    # combine the managers and players table
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

    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='tie', value=["NULL" for i in range(0, df_awards_combined_share.shape[0])])
    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='notes', value=["NULL" for i in range(0, df_awards_combined_share.shape[0])])

    df_awards_combined.insert(loc=4, column='votesFirst', value=["NULL" for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined.insert(loc=4, column='pointsMax', value=["NULL" for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined.insert(loc=4, column='pointsWon', value=["NULL" for i in range(0, df_awards_combined.shape[0])])

    df_awards_combined.insert(loc=df_awards_combined.shape[1], column='isShared', value=['N' for i in range(0, df_awards_combined.shape[0])])
    df_awards_combined_share.insert(loc=df_awards_combined_share.shape[1], column='isShared', value=['Y' for i in range(0, df_awards_combined_share.shape[0])])

    assert(len(df_awards_combined.columns.values) == len(df_awards_combined_share.columns.values))

    for i in range(0, len(df_awards_combined.columns.values)):
        assert(df_awards_combined.columns.values[i] == df_awards_combined_share.columns.values[i])

    df_awards = pd.concat([df_awards_combined, df_awards_combined_share])

    df_awards.sort_values(by=['yearID', 'personID'], ascending=True, inplace=True)

    df_awards.rename(columns=cols.AwardsCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_awards.loc[df_awards['leagueID'].isnull(), 'leagueID'] = "NA"

    # add primary key to table
    df_awards.insert(loc=0, column='AwardsRowID', value=range(1, df_awards.shape[0] + 1))

    df_awards.fillna("NULL", inplace=True)

    saveCSV(df_awards, out_file)

def clean_schoolCSV(db_path):
    school_file = 'Schools.csv'
    out_file = db_path + school_file

    df_schools = pd.read_csv(school_file, delimiter=',')

    df_schools.rename(columns={'name_full' : 'schoolName'}, inplace=True)

    df_schools.fillna("NULL", inplace=True)

    saveCSV(df_schools, out_file)

def clean_HallOfFameCSV(db_path):
    hallOfFame_file = 'HallOfFame.csv'
    out_file = db_path + hallOfFame_file

    df_halloffame = pd.read_csv(hallOfFame_file, delimiter=',')

    df_halloffame.rename(columns={'playerID' : 'personID',
                                       'yearID' : 'year'}, inplace=True)

    df_halloffame.insert(loc=0, column='HallOfFameRowID', value=range(1, df_halloffame.shape[0] + 1))

    df_halloffame.fillna("NULL", inplace=True)


    saveCSV(df_halloffame, out_file)

def clean_collegePlayerCSV(db_path):
    collegePlayer_file = 'CollegePlaying.csv'
    out_file = db_path + collegePlayer_file

    df_collegePlayer = pd.read_csv(collegePlayer_file, delimiter=',')

    df_collegePlayer.rename(columns={'playerID' : 'personID',
                                       'yearID' : 'year'}, inplace=True)

    df_collegePlayer.insert(loc=0, column='CollegePlayingRowID', value=range(1, df_collegePlayer.shape[0] + 1))

    df_collegePlayer.fillna("NULL", inplace=True)

    saveCSV(df_collegePlayer, out_file)

def clean_allStarCSV(db_path):
    allStarFull_file = 'AllstarFull.csv'
    outFile = db_path + 'AllStar.csv'

    df_allstarfull = pd.read_csv(allStarFull_file, delimiter=',')

    df_allstarfull.rename(columns={'playerID' : 'personID',
                                       'lgID' : 'leagueID',
                                       'yearID' : 'year',
                                       'GP' : 'PlayedInGame'}, inplace=True)

    # replace the 1/0 with Y/N
    df_allstarfull.loc[df_allstarfull['PlayedInGame'] == 1, 'PlayedInGame'] = 'Y'
    df_allstarfull.loc[df_allstarfull['PlayedInGame'] == 0, 'PlayedInGame'] = 'N'

    # pandas interprets the "NA" league id as a null value
    df_allstarfull.loc[df_allstarfull['leagueID'].isnull(), 'leagueID'] = "NA"

    df_allstarfull.insert(loc=0, column='AllStarRowID', value=range(1, df_allstarfull.shape[0] + 1))

    df_allstarfull.fillna("NULL", inplace=True)


    saveCSV(df_allstarfull, outFile)

def clean_teamsHalfCSV(db_path):
    teamsHalf_file = 'TeamsHalf.csv'
    out_file = db_path + teamsHalf_file

    df_teamsHalf = pd.read_csv(teamsHalf_file, delimiter=',')

    df_teamsHalf.rename(columns=cols.TeamsHalfCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_teamsHalf.loc[df_teamsHalf['leagueID'].isnull(), 'leagueID'] = "NA"

    df_teamsHalf.insert(loc=0, column='TeamsHalfRowID', value=range(1, df_teamsHalf.shape[0] + 1))

    df_teamsHalf.fillna("NULL", inplace=True)

    saveCSV(df_teamsHalf, out_file)

def clean_seriesPostCSV(db_path):
    seriesPost_file = 'SeriesPost.csv'
    outFile = db_path + 'PostSeasonSeries.csv'

    df_post = pd.read_csv(seriesPost_file, delimiter=',')

    df_post.rename(columns={'yearID' : 'year',
                            'lgIDwinner' : 'leagueIDWinner',
                            'lgIDloser' : 'leagueIDLoser'}, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_post.loc[df_post['leagueIDWinner'].isnull(), 'leagueIDWinner'] = "NA"

    # pandas interprets the "NA" league id as a null value
    df_post.loc[df_post['leagueIDLoser'].isnull(), 'leagueIDLoser'] = "NA"

    df_post.insert(loc=0, column='PostSeasonRowID', value=range(1, df_post.shape[0] + 1))

    df_post.fillna("NULL", inplace=True)

    saveCSV(df_post, outFile)

def clean_fieldingOFCSV(db_path):
    fieldingOF_file = 'FieldingOF.csv'
    out_file = db_path + fieldingOF_file

    df_fieldingOF = pd.read_csv(fieldingOF_file, delimiter=',')

    df_fieldingOF.rename(columns=cols.FieldingOFCols, inplace=True)

    df_fieldingOF.fillna("NULL", inplace=True)

    saveCSV(df_fieldingOF, out_file)

def clean_fieldingOFSplitCSV(db_path):
    fieldingOFSplit_file = 'FieldingOFsplit.csv'
    out_file = db_path + fieldingOFSplit_file

    df_fieldingOFSplit = pd.read_csv(fieldingOFSplit_file, delimiter=',')

    df_fieldingOFSplit.rename(columns=cols.FieldingOFSplitCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_fieldingOFSplit.loc[df_fieldingOFSplit['leagueID'].isnull(), 'leagueID'] = "NA"

    # columns are not in use and lahmann doesnt even include them in docs
    df_fieldingOFSplit.drop(columns=['PB','WP','SB','CS','ZR'], inplace=True)

    df_fieldingOFSplit.fillna("NULL", inplace=True)


    saveCSV(df_fieldingOFSplit, out_file)

def clean_homegamesCSV(db_path):
    homegames_file = 'HomeGames.csv'
    out_file = db_path + homegames_file

    df_homegames = pd.read_csv(homegames_file, delimiter=',')

    df_homegames.rename(columns=cols.HomeGamesCols, inplace=True)

    # pandas interprets the "NA" league id as a null value
    df_homegames.loc[df_homegames['leagueID'].isnull(), 'leagueID'] = "NA"

    df_homegames.fillna("NULL", inplace=True)

    saveCSV(df_homegames, out_file)

def main():

    conn = sql.connect(user=user['username'], password=user['password'], host=user['host'], db=user['db'])

    cur = conn.cursor()

    cur.execute("SELECT @@datadir;")

    databasePath = cur.fetchall()[0][0]
    databasePath = databasePath + user['db'] + '/'

    #change the current directory into folder with CSV files
    os.chdir("../csv_files")

    #get list of file names in directory
    fileList = os.listdir()

    # clean People.csv
    print("cleaning People.csv...")
    clean_peopleCSV(databasePath)

    # clean Managers.csv
    print("cleaning Managers.csv...")
    os.chdir("../csv_files")
    clean_managerCSV(databasePath)

    # clean Batting.csv
    print("cleaning Batting.csv...")
    os.chdir("../csv_files")
    clean_battingCSV(databasePath)

    # clean Pitching.csv
    print("cleaning Pitching.csv...")
    os.chdir("../csv_files")
    clean_pitchingCSV(databasePath)

    # clean Fielding.csv
    print("cleaning Fielding.csv...")
    os.chdir("../csv_files")
    clean_fieldingCSV(databasePath)

    # clean Players.csv dependencies: Batting.csv, Pitching.csv, Fielding.csv (in csv_cleaned)
    print("cleaning Players.csv...")
    clean_playersCSV(databasePath)

    # clean Salaries.csv
    print("cleaning Salaries.csv...")
    os.chdir("../csv_files")
    clean_salaryCSV(databasePath)

    # clean Appearances.csv
    print("cleaning PlayerPositions.csv...")
    os.chdir("../csv_files")
    clean_playerPositionsCSV(databasePath)

    # clean Parks.csv
    print("cleaning Parks.csv...")
    os.chdir("../csv_files")
    clean_parksCSV(databasePath)

    # clean Teams.csv dependencies csv_cleaned/Parks.csv
    print("cleaning Teams.csv...")
    os.chdir("../csv_files")
    clean_teamsCSV(databasePath)

    # clean Division.csv
    print("cleaning Division.csv...")
    os.chdir("../csv_files")
    clean_divisionCSV(databasePath)

    # clean Leagues.csv
    print("cleaning Leagues.csv...")
    os.chdir("../csv_files")
    clean_leaguesCSV(databasePath)

    # clean Franchises.csv
    print("cleaning Franchises.csv...")
    os.chdir("../csv_files")
    clean_franchisesCSV(databasePath)

    print("cleaning Awards.csv...")
    os.chdir("../csv_files")
    clean_awardsCSV(databasePath)

    print("cleaning Schools.csv...")
    os.chdir("../csv_files")
    clean_schoolCSV(databasePath)

    print("cleaning HallOfFame.csv...")
    os.chdir("../csv_files")
    clean_HallOfFameCSV(databasePath)

    print("cleaning CollegePlaying.csv...")
    os.chdir("../csv_files")
    clean_collegePlayerCSV(databasePath)

    print("cleaning AllStar.csv...")
    os.chdir("../csv_files")
    clean_allStarCSV(databasePath)

    print("cleaning TeamsHalf.csv...")
    os.chdir("../csv_files")
    clean_teamsHalfCSV(databasePath)

    print("cleaning SeriesPost.csv...")
    os.chdir("../csv_files")
    clean_seriesPostCSV(databasePath)

    print("cleaning FieldingOF.csv...")
    os.chdir("../csv_files")
    clean_fieldingOFCSV(databasePath)

    print("cleaning FieldingOFSplit.csv...")
    os.chdir("../csv_files")
    clean_fieldingOFSplitCSV(databasePath)

    print("cleaning HomeGames.csv...")
    os.chdir("../csv_files")
    clean_homegamesCSV(databasePath)

if __name__ == "__main__":
    main()