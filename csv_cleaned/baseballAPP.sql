USE baseballapp;



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
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Pitching;
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS PlayerPositions;
DROP TABLE IF EXISTS PostSeasonSeries;
DROP TABLE IF EXISTS Salaries;
DROP TABLE IF EXISTS Schools;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS TeamsHalf;


CREATE TABLE AllStar (
AllStarRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10) NOT NULL, year smallint(6), gameNum smallint(6), gameID VARCHAR(12), teamID VARCHAR(3), leagueID VARCHAR(2), PlayedInGame VARCHAR(1), startingPos smallint(6),
PRIMARY KEY (AllStarRowID)
);

CREATE TABLE Awards (
AwardsRowID int NOT NULL AUTO_INCREMENT, awardName VARCHAR(75), year smallint(6), leagueID CHAR(2), personID VARCHAR(9), pointsWon double, pointsMax smallint(6), votesFirst double, tie VARCHAR(1), notes VARCHAR(100), isShared VARCHAR(1),
PRIMARY KEY (AwardsRowID)
);

CREATE TABLE Batting (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID CHAR(2), Games smallint(6), AtBats smallint(6), Runs smallint(6), Hits smallint(6), Doubles smallint(6), Triples smallint(6), HomeRuns smallint(6), RunsBattedIn smallint(6), StolenBases smallint(6), CaughtStealing smallint(6), BaseOnBalls smallint(6), StrikeOuts smallint(6), IntentionalWalks smallint(6), HitByPitch smallint(6), SacrificeHits smallint(6), SacrificeFlies smallint(6), GroundedIntoDoublePlays smallint(6), isPostSeason VARCHAR(2), round VARCHAR(10)
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
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID VARCHAR(2), Position VARCHAR(2), Games smallint(6), GamesStarted smallint(6), InnOuts smallint(6), Putouts smallint(6), Assists smallint(6), Errors smallint(6), DoublePlays smallint(6), TriplePlays smallint(6), PassedBallsByCatchers smallint(6), WildPitchesByCatchers smallint(6), OpponentStolenBasesByCatchers smallint(6), OpponentsCaughtStealingByCatchers smallint(6), ZoneRating double, round VARCHAR(10), isPostSeason CHAR(2)
);

CREATE TABLE FieldingOF (
personID VARCHAR(10), year smallint(6), stint smallint(6), GamesPlayedLeftField smallint(6), GamesPlayedCenterField smallint(6), GamesPlayedRightField smallint(6)
);

CREATE TABLE FieldingOFsplit (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID CHAR(2), Position VARCHAR(2), Games smallint(6), GamesStarted smallint(6), InnOuts smallint(6), Putouts smallint(6), Assists smallint(6), Errors smallint(6), DoublePlays smallint(6)
);

CREATE TABLE Franchises (
franchID VARCHAR(3), franchName VARCHAR(50), active VARCHAR(1), NAassoc VARCHAR(3),
PRIMARY KEY (franchID)
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
ManagerRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), teamID VARCHAR(3), leagueID CHAR(2), inseason smallint(6), half VARCHAR(100), GamesManaged smallint(6), Wins smallint(6), Losses smallint(6), rank smallint(6), plyrMgr VARCHAR(1), isSeasonHalf VARCHAR(2),
PRIMARY KEY (ManagerRowID)
);

CREATE TABLE Parks (
parkID VARCHAR(6), parkName VARCHAR(255), parkAlias VARCHAR(255), city VARCHAR(255), state VARCHAR(2), country VARCHAR(5),
PRIMARY KEY (parkID)
);

CREATE TABLE People (
personID VARCHAR(10) NOT NULL, nameFirst VARCHAR(255), nameLast VARCHAR(255), birthYear INT(11), birthMonth INT(11), birthDay INT(11), birthCountry VARCHAR(255), birthState VARCHAR(255), birthCity VARCHAR(255), deathYear INT(11), deathMonth INT(11), deathDay INT(11), deathCountry VARCHAR(255), deathState VARCHAR(255), deathCity VARCHAR(255), weight INT(11), height INT(11), bats VARCHAR(255), throws VARCHAR(255), debut VARCHAR(255), finalGame VARCHAR(255), retroID VARCHAR(255), bbrefID VARCHAR(255),
PRIMARY KEY(personID)
);

CREATE TABLE Pitching (
personID VARCHAR(10), year smallint(6), stint smallint(6), teamID VARCHAR(3), leagueID VARCHAR(2), Wins smallint(6), Losses smallint(6), Games smallint(6), GamesStarted smallint(6), CompleteGames smallint(6), Shutouts smallint(6), Saves smallint(6), IPouts INT(11), Hits smallint(6), EarnedRuns smallint(6), Homeruns smallint(6), Walks smallint(6), Strikeouts smallint(6), OpponentsBattingAvg double, EarnedRunAvg double, IntentionalWalks smallint(6), WildPitches smallint(6), BattersHitByPitch smallint(6), Balks smallint(6), BattersFacedByPitcher smallint(6), GamesFinished smallint(6), RunsAllowed smallint(6), SacrificesByOpposingBatters smallint(6), SacrificeFliesByOpposingBatters smallint(6), GIDPByOpposingBatter smallint(6), round VARCHAR(10), isPostSeason VARCHAR(2),
PRIMARY KEY (personID)
);

CREATE TABLE PlayerPositions (
playerPosRowID int NOT NULL AUTO_INCREMENT, personID VARCHAR(10), year smallint(6), teamID VARCHAR(3), leagueID CHAR(2), TotalGamesPlayed smallint(6), GamesStarted smallint(6), GamesPlayerBatted smallint(6), GamesPlayerOnDefense smallint(6), GamesAsPitcher smallint(6), GamesAsCatcher smallint(6), GamesAs1Baseman smallint(6), GamesAs2Baseman smallint(6), GamesAs3Baseman smallint(6), GamesAsShortstop smallint(6), GamesAsLeftfielder smallint(6), GamesAsCenterfielder smallint(6), GamesAsRightfielder smallint(6), GamesAsOutfielder smallint(6), GamesAsDesignatedHitter smallint(6), GamesAsPinchHitter smallint(6), GamesAsPinchRunner smallint(6),
PRIMARY KEY (playerPosRowID)
);

CREATE TABLE Players (
personID VARCHAR(100), year smallint(6), stint VARCHAR(100), teamID VARCHAR(3), isPostSeason VARCHAR(2), isPitching VARCHAR(1), isBatting VARCHAR(1), isFielding VARCHAR(1),
FOREIGN KEY (personID) REFERENCES People(PersonID)
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
schoolID VARCHAR(50), schoolName CHAR(255), city CHAR(255), state CHAR(255), country CHAR(255),
PRIMARY KEY (schoolID)
);

CREATE TABLE Teams (
TeamsRowID INT NOT NULL AUTO_INCREMENT, year smallint(6), leagueID CHAR(2), teamID VARCHAR(3), teamName VARCHAR(255), franchID VARCHAR(3), divisionID VARCHAR(2), Rank smallint(6), GamesPlayed smallint(6), GamesPlayedAtHome smallint(6), Wins smallint(6), Losses smallint(6), DivisionWinner VARCHAR(1), WildcardWinner VARCHAR(1), LeagueChampion VARCHAR(1), WorldSeriesWinner VARCHAR(1), Runs smallint(6), AtBats smallint(6), HitsByBatters smallint(6), Doubles smallint(6), Triples smallint(6), HomeRunsByBatters smallint(6), WalksByBatters smallint(6), StrikeoutsByBatters smallint(6), StolenBases smallint(6), CaughtStealing smallint(6), BattersHitByPitch smallint(6), SacrificeFlies smallint(6), OpponentsRunsScored smallint(6), EarnedRunsAllowed smallint(6), EarnedRunAvg double, CompleteGames smallint(6), Shutouts smallint(6), Saves smallint(6), OutsPitched INT(11), HitsAllowed smallint(6), HomeRunsAllowed smallint(6), WalksAllowed smallint(6), StrikeoutsByPitchers smallint(6), Errors int(11), DoublePlays int(11), FieldingPercentage double, parkName varchar(50), attendance int(11), ThreeYearParkFactorBatters int(11), ThreeYearParkFactorPitchers int(11), teamIDBR VARCHAR(3), teamIDlahman45 VARCHAR(3), teamIDretro VARCHAR(3),
PRIMARY KEY (TeamsRowID)
);

CREATE TABLE TeamsHalf (
TeamsHalfRowID int NOT NULL AUTO_INCREMENT, year smallint(6), leagueID CHAR(2), teamID VARCHAR(3), Half VARCHAR(1), divisionID VARCHAR(2), DivWin VARCHAR(1), Rank smallint(6), GamesPlayed smallint(6), Wins smallint(6), Losses smallint(6),
PRIMARY KEY (TeamsHalfRowID)
);


LOAD DATA INFILE 'AllStar.csv'
IGNORE INTO TABLE AllStar
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone, @vtwo, @vthree, @vfour, @vfive, @vsix, @vseven, @veight, @vnine)
SET
AllStarRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
gameNum = NULLIF(@vfour, 'NULL'),
gameID = NULLIF(@vfive, 'NULL'),
teamID = NULLIF(@vsix, 'NULL'),
leagueID = NULLIF(@vseven, 'NULL'),
PlayedInGame = NULLIF(@veight, 'NULL'),
startingPos = NULLIF(@vnine, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Awards.csv'
IGNORE INTO TABLE Awards
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone, @vtwo, @vthree, @vfour, @vfive, @vsix, @vseven, @veight, @vnine, @vten, @veleven)
SET
AwardsRowID = NULLIF(@vone, 'NULL'),
awardName = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
leagueID = NULLIF(@vfour, 'NULL'),
personID = NULLIF(@vfive, 'NULL'),
pointsWon = NULLIF(@vsix, 'NULL'),
pointsMax = NULLIF(@vseven, 'NULL'),
votesFirst = NULLIF(@veight, 'NULL'),
tie = NULLIF(@vnine, 'NULL'),
notes = NULLIF(@vten, 'NULL'),
isShared = NULLIF(@veleven, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Batting.csv'
IGNORE INTO TABLE Batting
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@vtwentyone,@vtwentytwo,@vtwentythree,@vtwentyfour)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
Games = NULLIF(@vsix, 'NULL'),
AtBats = NULLIF(@vseven, 'NULL'),
Runs = NULLIF(@veight, 'NULL'),
Hits = NULLIF(@vnine, 'NULL'),
Doubles = NULLIF(@vten, 'NULL'),
Triples = NULLIF(@veleven, 'NULL'),
HomeRuns = NULLIF(@vtwelve, 'NULL'),
RunsBattedIn = NULLIF(@vthirteen, 'NULL'),
StolenBases = NULLIF(@vfourteen, 'NULL'),
CaughtStealing = NULLIF(@vfifteen, 'NULL'),
BaseOnBalls = NULLIF(@vsixteen, 'NULL'),
StrikeOuts = NULLIF(@vseventeen, 'NULL'),
IntentionalWalks = NULLIF(@veighteen, 'NULL'),
HitByPitch = NULLIF(@vnineteen, 'NULL'),
SacrificeHits = NULLIF(@vtwenty, 'NULL'),
SacrificeFlies = NULLIF(@vtwentyone, 'NULL'),
GroundedIntoDoublePlays = NULLIF(@vtwentytwo, 'NULL'),
isPostSeason = NULLIF(@vtwentythree, 'NULL'),
round = NULLIF(@vtwentyfour, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'CollegePlaying.csv'
IGNORE INTO TABLE CollegePlaying
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour)
SET
CollegePlayingRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
schoolID = NULLIF(@vthree, 'NULL'),
year = NULLIF(@vfour, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Divisions.csv'
IGNORE INTO TABLE Divisions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour)
SET
DivisionRowID = NULLIF(@vone, 'NULL'),
divisionID = NULLIF(@vtwo, 'NULL'),
divisionName = NULLIF(@vthree, 'NULL'),
isActive = NULLIF(@vfour, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Fielding.csv'
IGNORE INTO TABLE Fielding
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@twentyone)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
Position = NULLIF(@vsix, 'NULL'),
Games = NULLIF(@vseven, 'NULL'),
GamesStarted = NULLIF(@veight, 'NULL'),
InnOuts = NULLIF(@vnine, 'NULL'),
Putouts = NULLIF(@vten, 'NULL'),
Assists = NULLIF(@veleven, 'NULL'),
Errors = NULLIF(@vtwelve, 'NULL'),
DoublePlays = NULLIF(@vthirteen, 'NULL'),
TriplePlays = NULLIF(@vfourteen, 'NULL'),
PassedBallsByCatchers = NULLIF(@vfifteen, 'NULL'),
WildPitchesByCatchers = NULLIF(@vsixteen, 'NULL'),
OpponentStolenBasesByCatchers = NULLIF(@vseventeen, 'NULL'),
OpponentsCaughtStealingByCatchers = NULLIF(@veighteen, 'NULL'),
ZoneRating = NULLIF(@vnineteen, 'NULL'),
round = NULLIF(@vtwenty, 'NULL'),
isPostSeason = NULLIF(@vtwentyone, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'FieldingOF.csv'
IGNORE INTO TABLE FieldingOF
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
GamesPlayedLeftField = NULLIF(@vfour, 'NULL'),
GamesPlayedCenterField = NULLIF(@vfive, 'NULL'),
GamesPlayedRightField = NULLIF(@vsix, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'FieldingOFsplit.csv'
IGNORE INTO TABLE FieldingOFsplit
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
Position = NULLIF(@vsix, 'NULL'),
Games = NULLIF(@vseven, 'NULL'),
GamesStarted = NULLIF(@veight, 'NULL'),
InnOuts = NULLIF(@vnine, 'NULL'),
Putouts = NULLIF(@vten, 'NULL'),
Assists = NULLIF(@veleven, 'NULL'),
Errors = NULLIF(@vtwelve, 'NULL'),
DoublePlays = NULLIF(@vthirteen, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Franchises.csv'
IGNORE INTO TABLE Franchises
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour)
SET
franchID = NULLIF(@vone, 'NULL'),
franchName = NULLIF(@vtwo, 'NULL'),
active = NULLIF(@vthree, 'NULL'),
NAassoc = NULLIF(@vfour, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'HallOfFame.csv'
IGNORE INTO TABLE HallOfFame
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten)
SET
HallOfFameRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
votedBy = NULLIF(@vfour, 'NULL'),
ballots = NULLIF(@vfive, 'NULL'),
needed = NULLIF(@vsix, 'NULL'),
votes = NULLIF(@vseven, 'NULL'),
inducted = NULLIF(@veight, 'NULL'),
category = NULLIF(@vnine, 'NULL'),
needed_note = NULLIF(@vten, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'HomeGames.csv'
IGNORE INTO TABLE HomeGames
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine)
SET
year = NULLIF(@vone, 'NULL'),
leagueID = NULLIF(@vtwo, 'NULL'),
teamID = NULLIF(@vthree, 'NULL'),
parkID = NULLIF(@vfour, 'NULL'),
debutGameDate = NULLIF(@vfive, 'NULL'),
endGameDate = NULLIF(@vsix, 'NULL'),
gamesPlayed = NULLIF(@vseven, 'NULL'),
datesPlayed = NULLIF(@veight, 'NULL'),
attendance = NULLIF(@vnine, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Leagues.csv'
IGNORE INTO TABLE Leagues
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree)
SET
leagueID = NULLIF(@vone, 'NULL'),
leagueName = NULLIF(@vtwo, 'NULL'),
isActive = NULLIF(@vthree, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Managers.csv'
IGNORE INTO TABLE Managers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen)
SET
ManagerRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
inseason = NULLIF(@vsix, 'NULL'),
half = NULLIF(@vseven, 'NULL'),
GamesManaged = NULLIF(@veight, 'NULL'),
Wins = NULLIF(@vnine, 'NULL'),
Losses = NULLIF(@vten, 'NULL'),
rank = NULLIF(@veleven, 'NULL'),
plyrMgr = NULLIF(@vtwelve, 'NULL'),
isSeasonHalf = NULLIF(@vthirteen, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Parks.csv'
IGNORE INTO TABLE Parks
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix)
SET
parkID = NULLIF(@vone, 'NULL'),
parkName = NULLIF(@vtwo, 'NULL'),
parkAlias = NULLIF(@vthree, 'NULL'),
city = NULLIF(@vfour, 'NULL'),
state = NULLIF(@vfive, 'NULL'),
country = NULLIF(@vsix, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'People.csv'
IGNORE INTO TABLE People
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@vtwentyone,@vtwentytwo,@vtwentythree,@vtwentyfour)
SET
personID = NULLIF(@vone, 'NULL'),
nameFirst = NULLIF(@vtwo, 'NULL'),
nameLast = NULLIF(@vthree, 'NULL'),
birthYear = NULLIF(@vfour, 'NULL'),
birthMonth = NULLIF(@vfive, 'NULL'),
birthDay = NULLIF(@vsix, 'NULL'),
birthCountry = NULLIF(@vseven, 'NULL'),
birthState = NULLIF(@veight, 'NULL'),
birthCity = NULLIF(@vnine, 'NULL'),
deathYear = NULLIF(@vten, 'NULL'),
deathMonth = NULLIF(@veleven, 'NULL'),
deathDay = NULLIF(@vtwelve, 'NULL'),
deathCountry = NULLIF(@vthirteen, 'NULL'),
deathState = NULLIF(@vfourteen, 'NULL'),
deathCity = NULLIF(@vfifteen, 'NULL'),
weight = NULLIF(@vsixteen, 'NULL'),
height = NULLIF(@vseventeen, 'NULL'),
bats = NULLIF(@veighteen, 'NULL'),
throws = NULLIF(@vnineteen, 'NULL'),
debut = NULLIF(@vtwenty, 'NULL'),
finalGame = NULLIF(@vtwentyone, 'NULL'),
retroID = NULLIF(@vtwentytwo, 'NULL'),
bbrefID = NULLIF(@vtwentythree, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Pitching.csv'
IGNORE INTO TABLE Pitching
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@vtwentyone,@vtwentytwo,@vtwentythree,@vtwentyfour,@vtwentyfive,@vtwentysix,@vtwentyseven,@vtwentyeight,@vtwentynine,@vthirty,@vthirtyone,@vthirtytwo)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
Wins = NULLIF(@vsix, 'NULL'),
Losses = NULLIF(@vseven, 'NULL'),
Games = NULLIF(@veight, 'NULL'),
GamesStarted = NULLIF(@vnine, 'NULL'),
CompleteGames = NULLIF(@vten, 'NULL'),
Shutouts = NULLIF(@veleven, 'NULL'),
Saves = NULLIF(@vtwelve, 'NULL'),
IPouts = NULLIF(@vthirteen, 'NULL'),
Hits = NULLIF(@vfourteen, 'NULL'),
EarnedRuns = NULLIF(@vfifteen, 'NULL'),
Homeruns = NULLIF(@vsixteen, 'NULL'),
Walks = NULLIF(@vseventeen, 'NULL'),
Strikeouts = NULLIF(@veighteen, 'NULL'),
OpponentsBattingAvg = NULLIF(@vnineteen, 'NULL'),
EarnedRunAvg = NULLIF(@vtwenty, 'NULL'),
IntentionalWalks = NULLIF(@vtwentyone, 'NULL'),
WildPitches = NULLIF(@vtwentytwo, 'NULL'),
BattersHitByPitch = NULLIF(@vtwentythree, 'NULL'),
Balks = NULLIF(@vtwentyfour, 'NULL'),
BattersFacedByPitcher = NULLIF(@vtwentyfive, 'NULL'),
GamesFinished = NULLIF(@vtwentysix, 'NULL'),
RunsAllowed = NULLIF(@vtwentyseven, 'NULL'),
SacrificesByOpposingBatters = NULLIF(@vtwentyeight, 'NULL'),
SacrificeFliesByOpposingBatters = NULLIF(@vtwentynine, 'NULL'),
GIDPByOpposingBatter = NULLIF(@vthirty, 'NULL'),
round = NULLIF(@vthirtyone, 'NULL'),
isPostSeason = NULLIF(@vthirtytwo, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'PlayerPositions.csv'
IGNORE INTO TABLE PlayerPositions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@vtwentyone,@vtwentytwo)
SET
playerPosRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
TotalGamesPlayed = NULLIF(@vsix, 'NULL'),
GamesStarted = NULLIF(@vseven, 'NULL'),
GamesPlayerBatted = NULLIF(@veight, 'NULL'),
GamesPlayerOnDefense = NULLIF(@vnine, 'NULL'),
GamesAsPitcher = NULLIF(@vten, 'NULL'),
GamesAsCatcher = NULLIF(@veleven, 'NULL'),
GamesAs1Baseman = NULLIF(@vtwelve, 'NULL'),
GamesAs2Baseman = NULLIF(@vthirteen, 'NULL'),
GamesAs3Baseman = NULLIF(@vfourteen, 'NULL'),
GamesAsShortstop = NULLIF(@vfifteen, 'NULL'),
GamesAsLeftfielder = NULLIF(@vsixteen, 'NULL'),
GamesAsCenterfielder = NULLIF(@vseventeen, 'NULL'),
GamesAsRightfielder = NULLIF(@veighteen, 'NULL'),
GamesAsOutfielder = NULLIF(@vnineteen, 'NULL'),
GamesAsDesignatedHitter = NULLIF(@vtwenty, 'NULL'),
GamesAsPinchHitter = NULLIF(@vtwentyone, 'NULL'),
GamesAsPinchRunner = NULLIF(@vtwentytwo, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Players.csv'
IGNORE INTO TABLE Players
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight)
SET
personID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
stint = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
isPostSeason = NULLIF(@vfive, 'NULL'),
isPitching = NULLIF(@vsix, 'NULL'),
isBatting = NULLIF(@vseven, 'NULL'),
isFielding = NULLIF(@veight, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'PostSeasonSeries.csv'
IGNORE INTO TABLE PostSeasonSeries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten)
SET
PostSeasonRowID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
round = NULLIF(@vthree, 'NULL'),
teamIDwinner = NULLIF(@vfour, 'NULL'),
leagueIDWinner = NULLIF(@vfive, 'NULL'),
teamIDloser = NULLIF(@vsix, 'NULL'),
leagueIDLoser = NULLIF(@vseven, 'NULL'),
wins = NULLIF(@veight, 'NULL'),
losses = NULLIF(@vnine, 'NULL'),
ties = NULLIF(@vten, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Salaries.csv'
IGNORE INTO TABLE Salaries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix)
SET
salaryRowID = NULLIF(@vone, 'NULL'),
personID = NULLIF(@vtwo, 'NULL'),
year = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
leagueID = NULLIF(@vfive, 'NULL'),
salary = NULLIF(@vsix, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Schools.csv'
IGNORE INTO TABLE Schools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive)
SET
schoolID = NULLIF(@vone, 'NULL'),
schoolName = NULLIF(@vtwo, 'NULL'),
city = NULLIF(@vthree, 'NULL'),
state = NULLIF(@vfour, 'NULL'),
country = NULLIF(@vfive, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'Teams.csv'
IGNORE INTO TABLE Teams
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven,@vtwelve,@vthirteen,@vfourteen,@vfifteen,@vsixteen,@vseventeen,@veighteen,@vnineteen,@vtwenty,@vtwentyone,@vtwentytwo,@vtwentythree,@vtwentyfour,@vtwentyfive,@vtwentysix,@vtwentyseven,@vtwentyeight,@vtwentynine,@vthirty,@vthirtyone,@vthirtytwo,@thirtythree,@thirtyfour,@thirtyfive,@thirtysix,@thirtyseven,@thirtyeight,@thirtynine,@fourty,@fourtyone,@fourtytwo,@fourtythree,@fourtyfour,@fourtyfive,@fourtysix,@fourtyseven,@fourtyeight,@fourtynine)
SET
TeamsRowID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
leagueID = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
teamName = NULLIF(@vfive, 'NULL'),
franchID = NULLIF(@vsix, 'NULL'),
divisionID = NULLIF(@vseven, 'NULL'),
Rank = NULLIF(@veight, 'NULL'),
GamesPlayed = NULLIF(@vnine, 'NULL'),
GamesPlayedAtHome = NULLIF(@vten, 'NULL'),
Wins = NULLIF(@veleven, 'NULL'),
Losses = NULLIF(@vtweleve, 'NULL'),
DivisionWinner = NULLIF(@vthirteen, 'NULL'),
WildcardWinner = NULLIF(@vfourteen, 'NULL'),
LeagueChampion = NULLIF(@vfifteen, 'NULL'),
WorldSeriesWinner = NULLIF(@vsixteen, 'NULL'),
Runs = NULLIF(@vseventeen, 'NULL'),
AtBats= NULLIF(@veighteen, 'NULL'),
HitsByBatters = NULLIF(@vnineteen, 'NULL'),
Doubles = NULLIF(@vtwenty, 'NULL'),
Triples = NULLIF(@vtwentyone, 'NULL'),
HomeRunsByBatters = NULLIF(@vtwentytwo, 'NULL'),
WalksByBatters = NULLIF(@vtwentythree, 'NULL'),
StrikeoutsByBatters = NULLIF(@vtwentyfour, 'NULL'),
StolenBases = NULLIF(@vtwentyfive, 'NULL'),
CaughtStealing = NULLIF(@vtwentysix, 'NULL'),
BattersHitByPitch = NULLIF(@vtwentyseven, 'NULL'),
SacrificeFlies = NULLIF(@vtwentyeight, 'NULL'),
OpponentsRunsScored = NULLIF(@vtwentynine, 'NULL'),
EarnedRunsAllowed = NULLIF(@vthirty, 'NULL'),
EarnedRunAvg = NULLIF(@vthirtyone, 'NULL'),
CompleteGames = NULLIF(@vthirtytwo, 'NULL'),
Shutouts = NULLIF(@vthirtythree, 'NULL'),
Saves = NULLIF(@vthirtyfour, 'NULL'),
OutsPitched = NULLIF(@vthirtyfive, 'NULL'),
HitsAllowed = NULLIF(@vthirtysix, 'NULL'),
HomeRunsAllowed = NULLIF(@vthirtyseven, 'NULL'),
WalksAllowed = NULLIF(@vthirtyeight, 'NULL'),
StrikeoutsByPitchers = NULLIF(@vthirtynine, 'NULL'),
Errors = NULLIF(@vfourty, 'NULL'),
DoublePlays = NULLIF(@vfourtyone, 'NULL'),
FieldingPercentage = NULLIF(@vfourtytwo, 'NULL'),
parkName = NULLIF(@vfourtythree, 'NULL'),
attendance = NULLIF(@vfourtyfour, 'NULL'),
ThreeYearParkFactorBatters = NULLIF(@vfourtyfive, 'NULL'),
ThreeYearParkFactorPitchers = NULLIF(@vfourtysix, 'NULL'),
teamIDBR = NULLIF(@vfourtyseven, 'NULL'),
teamIDlahman45 = NULLIF(@vfourtyeight, 'NULL'),
teamIDretro = NULLIF(@vfourtynine, 'NULL')
;

SHOW WARNINGS;

LOAD DATA INFILE 'TeamsHalf.csv'
IGNORE INTO TABLE TeamsHalf
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@vone,@vtwo,@vthree,@vfour,@vfive,@vsix,@vseven,@veight,@vnine,@vten,@veleven)
SET
TeamsHalfRowID = NULLIF(@vone, 'NULL'),
year = NULLIF(@vtwo, 'NULL'),
leagueID = NULLIF(@vthree, 'NULL'),
teamID = NULLIF(@vfour, 'NULL'),
Half = NULLIF(@vfive, 'NULL'),
divisionID = NULLIF(@vsix, 'NULL'),
DivWin = NULLIF(@vseven, 'NULL'),
Rank = NULLIF(@veight, 'NULL'),
GamesPlayed = NULLIF(@vnine, 'NULL'),
Wins = NULLIF(@vten, 'NULL'),
Losses = NULLIF(@veleven, 'NULL')
;

SHOW WARNINGS;
