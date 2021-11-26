USE baseballAPP;


DROP TABLE IF EXISTS AllStar;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Batting;
DROP TABLE IF EXISTS CollegePlaying;
DROP TABLE IF EXISTS Divisions;
DROP TABLE IF EXISTS Fielding;
DROP TABLE IF EXISTS FieldingOF;
DROP TABLE IF EXISTS FieldingOFsplit;
DROP TABLE IF EXISTS Franchises;
DROP TABLE IF EXISTS HallOfFame;
DROP TABLE IF EXISTS HomeGames;
DROP TABLE IF EXISTS Leagues;
DROP TABLE IF EXISTS Managers;
DROP TABLE IF EXISTS Parks;
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS Pitching;
DROP TABLE IF EXISTS PlayerPositions;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS PostSeasonSeries;
DROP TABLE IF EXISTS Salaries;
DROP TABLE IF EXISTS Schools;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS TeamsHalf;


CREATE TABLE AllStar (
AllStarRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(9) NOT NULL, year smallint(6), gameNum smallint(6), gameID VARCHAR(12), teamID VARCHAR(3), leagueID VARCHAR(2), PlayedInGame VARCHAR(1), startingPos smallint(6),
PRIMARY KEY (AllStarRowID)
);

CREATE TABLE Awards (
AwardsRowID int NOT NULL AUTO_INCREMENT, awardName VARCHAR(75), year smallint(6), leagueID CHAR(2), personID VARCHAR(9), pointsWon double, pointsMax smallint(6), votesFirst double, tie VARCHAR(1), notes VARCHAR(100), isShared VARCHAR(1),
PRIMARY KEY (AwardsRowID)
);

CREATE TABLE Batting (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID CHAR(2), Games smallint(6), AtBats smallint(6), Runs smallint(6), Hits smallint(6), Doubles smallint(6), Triples smallint(6), HomeRuns smallint(6), RunsBattedIn smallint(6), StolenBases smallint(6), CaughtStealing smallint(6), BaseOnBalls smallint(6), StrikeOuts smallint(6), IntentionalWalks smallint(6), HitByPitch smallint(6), SacrificeHits smallint(6), SacrificeFlies smallint(6), GroundedIntoDoublePlays smallint(6), isPostSeason VARCHAR(1), round VARCHAR(10)
);

CREATE TABLE CollegePlaying (
CollegePlayingRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(9), schoolID VARCHAR(15), year smallint(6),
PRIMARY KEY (CollegePlayingRowID)
);

CREATE TABLE Divisions (
DivisionRowID int NOT NULL AUTO_INCREMENT, divisionID VARCHAR(2), divisionName VARCHAR(50), isActive VARCHAR(1),
PRIMARY KEY (DivisionRowID)
);

CREATE TABLE Fielding (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID VARCHAR(2), Position VARCHAR(2), Games smallint(6), GamesStarted smallint(6), InnOuts smallint(6), Putouts smallint(6), Assists smallint(6), Errors smallint(6), DoublePlays smallint(6), TriplePlays smallint(6), PassedBallsByCatchers smallint(6), WildPitchesByCatchers smallint(6), OpponentStolenBasesByCatchers smallint(6), OpponentsCaughtStealingByCatchers smallint(6), ZoneRating double, round VARCHAR(10), isPostSeason VARCHAR(1)
);

CREATE TABLE FieldingOF (
personID VARCHAR(10), year smallint(6), stint smallint(6), GamesPlayedLeftField smallint(6), GamesPlayedCenterField smallint(6), GamesPlayedRightField smallint(6)
);

CREATE TABLE FieldingOFsplit (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID CHAR(2), Position VARCHAR(2), Games smallint(6), GamesStarted smallint(6), InnOuts smallint(6), Putouts smallint(6), Assists smallint(6), Errors smallint(6), DoublePlays smallint(6)
);

CREATE TABLE Franchises (
franchID VARCHAR(3), franchName VARCHAR(50), active VARCHAR(1), NAassoc VARCHAR(3)
);

CREATE TABLE HallOfFame (
HallOfFameRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), votedBy VARCHAR(64), ballots smallint(6), needed smallint(6), votes smallint(6), inducted VARCHAR(1), category VARCHAR(20), needed_note VARCHAR(25),
PRIMARY KEY (HallOfFameRowID)
);

CREATE TABLE HomeGames (
year smallint(6), leagueID CHAR(2), teamID VARCHAR(3), parkID VARCHAR(6), debutGameDate VARCHAR(255), endGameDate VARCHAR(255), gamesPlayed int(11), datesPlayed VARCHAR(255), attendance int(11)
);

CREATE TABLE Leagues (
leagueID CHAR(2), leagueName VARCHAR(100), isActive VARCHAR(1),
PRIMARY KEY (leagueID)
);

CREATE TABLE Managers (
ManagerRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), teamID VARCHAR(3), leagueID CHAR(2), inseason smallint(6), half VARCHAR(100), GamesManaged smallint(6), Wins smallint(6), Losses smallint(6), rank smallint(6), plyrMgr VARCHAR(1), isSeasonHalf VARCHAR(1),
PRIMARY KEY (ManagerRowID)
);

CREATE TABLE Parks (
parkID VARCHAR(6), parkName VARCHAR(255), parkAlias VARCHAR(255), city VARCHAR(255), state VARCHAR(2), country VARCHAR(5),
PRIMARY KEY (parkID)
);

CREATE TABLE People (
personID VARCHAR(10) NOT NULL, nameFirst VARCHAR(255), nameLast VARCHAR(255), birthYear INT(11), birthMonth INT(11), birthDay INT(11), birthCountry INT(11), birthState VARCHAR(255), birthCity VARCHAR(255), deathYear INT(11), deathMonth INT(11), deathDay INT(11), deathCountry VARCHAR(255), deathState VARCHAR(255), deathCity VARCHAR(255), weight INT(11), height INT(11), bats VARCHAR(255), throws VARCHAR(255), debut VARCHAR(255), finalGame VARCHAR(255), retroID VARCHAR(255), bbrefID VARCHAR(255),
PRIMARY KEY(personID)
);

CREATE TABLE Pitching (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID VARCHAR(2), Wins smallint(6), Losses smallint(6), Games smallint(6), GamesStarted smallint(6), CompleteGames smallint(6), Shutouts smallint(6), Saves smallint(6), IPouts INT(11), Hits smallint(6), EarnedRuns smallint(6), Homeruns smallint(6), Walks smallint(6), Strikeouts smallint(6), OpponentsBattingAvg double, EarnedRunAvg double, IntentionalWalks smallint(6), WildPitches smallint(6), BattersHitByPitch smallint(6), Balks smallint(6), BattersFacedByPitcher smallint(6), GamesFinished smallint(6), RunsAllowed smallint(6), SacrificesByOpposingBatters smallint(6), SacrificeFliesByOpposingBatters smallint(6), GIDPByOpposingBatter smallint(6), round VARCHAR(10), isPostSeason VARCHAR(1),
);

CREATE TABLE PlayerPositions (
playerPosRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), teamID VARCHAR(3), leagueID CHAR(2), TotalGamesPlayed smallint(6), GamesStarted smallint(6), GamesPlayerBatted smallint(6), GamesPlayerOnDefense smallint(6), GamesAsPitcher smallint(6), GamesAsCatcher smallint(6), GamesAs1Baseman smallint(6), GamesAs2Baseman smallint(6), GamesAs3Baseman smallint(6), GamesAsShortstop smallint(6), GamesAsLeftfielder smallint(6), GamesAsCenterfielder smallint(6), GamesAsRightfielder smallint(6), GamesAsOutfielder smallint(6), GamesAsDesignatedHitter smallint(6), GamesAsPinchHitter smallint(6), GamesAsPinchRunner smallint(6),
PRIMARY KEY (playerPosRowID)
);

CREATE TABLE Players (
personID VARCHAR(100), year smallint(6), stint VARCHAR(100), teamID VARCHAR(3), isPostSeason VARCHAR(1), isPitching VARCHAR(1), isBatting VARCHAR(1), isFielding VARCHAR(1),
PRIMARY KEY (personID)
);

CREATE TABLE PostSeasonSeries (
PostSeasonRowID int NOT NULL AUTO_INCREMENT, year smallint(6), round VARCHAR(100), teamIDwinner CHAR(3), leagueIDWinner CHAR(2), teamIDloser CHAR(3), leagueIDLoser CHAR(2), wins smallint(6), losses smallint(6), ties smallint(6),
PRIMARY KEY (PostSeasonRowID)
);

CREATE TABLE Salaries (
salaryRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), teamID VARCHAR(3), leagueID CHAR(2), salary double,
PRIMARY KEY (salaryRowID)
);

CREATE TABLE Schools (
schoolID VARCHAR(15), schoolName VARCHAR(255), city VARCHAR(55), state VARCHAR(55), country VARCHAR(55),
PRIMARY KEY (schoolID)
);

CREATE TABLE Teams (
TeamsRowID INT NOT NULL AUTO_INCREMENT, year smallint(6), leagueID CHAR(2), teamID VARCHAR(3), teamName VARCHAR(255), franchID VARCHAR(3), divisionID VARCHAR(2), Rank smallint(6), GamesPlayed smallint(6), GamesPlayedAtHome smallint(6), Wins smallint(6), Losses smallint(6), DivisionWinner VARCHAR(1), WildcardWinner VARCHAR(1), LeagueChampion VARCHAR(1), WorldSeriesWinner VARCHAR(1), Runs smallint(6), AtBats smallint(6), HitsByBatters smallint(6), Doubles smallint(6), Triples smallint(6), HomeRunsByBatters smallint(6), WalksByBatters smallint(6), StrikeoutsByBatters smallint(6), StolenBases smallint(6), CaughtStealing smallint(6), BattersHitByPitch smallint(6), SacrificeFlies smallint(6), OpponentsRunsScored smallint(6), EarnedRunsAllowed smallint(6), EarnedRunAvg double, CompleteGames smallint(6), Shutouts smallint(6), Saves smallint(6), OutsPitched INT(11), HitsAllowed smallint(6), HomeRunsAllowed smallint(6), WalksAllowed smallint(6), StrikeoutsByPitchers smallint(6), Errors int(11), DoublePlays int(11), FieldingPercentage double, parkName varchar(50), attendance int(11), ThreeYearParkFactorBatters int(11), ThreeYearParkFactorPitchers int(11), teamIDBR VARCHAR(3), teamIDlahman45 VARCHAR(3), teamIDretro VARCHAR(3),
PRIMARY KEY (TeamsRowID)
);

CREATE TABLE TeamsHalf (
TeamsHalfRowID int NOT NULL AUTO_INCREMENT, year smallint(6), leagueID CHAR(2), teamID VARCHAR(3), Half VARCHAR(1), divisionID VARCHAR(2), DivWin smallint(6), Rank smallint(6), GamesPlayed smallint(6), Wins smallint(6), Losses smallint(6),
PRIMARY KEY (TeamsHalfRowID)
);



LOAD DATA INFILE 'AllStar.csv'
INTO TABLE AllStar
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Awards.csv'
INTO TABLE Awards
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Batting.csv'
INTO TABLE Batting
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'CollegePlaying.csv'
INTO TABLE CollegePlaying
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Divisions.csv'
INTO TABLE Divisions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Fielding.csv'
INTO TABLE Fielding
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'FieldingOF.csv'
INTO TABLE FieldingOF
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'FieldingOFsplit.csv'
INTO TABLE FieldingOFsplit
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Franchises.csv'
INTO TABLE Franchises
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'HallOfFame.csv'
INTO TABLE HallOfFame
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'HomeGames.csv'
INTO TABLE HomeGames
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Leagues.csv'
INTO TABLE Leagues
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Managers.csv'
INTO TABLE Managers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Parks.csv'
INTO TABLE Parks
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'People.csv'
INTO TABLE People
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Pitching.csv'
INTO TABLE Pitching
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'PlayerPositions.csv'
INTO TABLE PlayerPositions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Players.csv'
INTO TABLE Players
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'PostSeasonSeries.csv'
INTO TABLE PostSeasonSeries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Salaries.csv'
INTO TABLE Salaries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Schools.csv'
INTO TABLE Schools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'Teams.csv'
INTO TABLE Teams
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'TeamsHalf.csv'
INTO TABLE TeamsHalf
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

