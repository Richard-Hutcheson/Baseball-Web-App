USE baseballAPP;


DROP TABLE IF EXISTS AllStarOccurences;
DROP TABLE IF EXISTS Appearances;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Batting;
DROP TABLE IF EXISTS CollegePlaying;
DROP TABLE IF EXISTS Divisions;
DROP TABLE IF EXISTS Fielding;
DROP TABLE IF EXISTS FieldingOF;
DROP TABLE IF EXISTS FieldingOFsplit;
DROP TABLE IF EXISTS Franchises;
DROP TABLE IF EXISTS HallOfFame;
DROP TABLE IF EXISTS Leagues;
DROP TABLE IF EXISTS Managers;
DROP TABLE IF EXISTS Parks;
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS Pitching;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS PostSeasonSeries;
DROP TABLE IF EXISTS Salaries;
DROP TABLE IF EXISTS Schools;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS TeamsHalf;


CREATE TABLE AllStarOccurences (
personID VARCHAR(100), year VARCHAR(100), gameNum VARCHAR(100), gameID VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), GP VARCHAR(100), startingPos VARCHAR(100)
);

CREATE TABLE Appearances (
personID VARCHAR(100), year VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), TotalGamesPlayed VARCHAR(100), GamesStarted VARCHAR(100), GamesPlayerBatted VARCHAR(100), GamesPlayerOnDefense VARCHAR(100), GamesAsPitcher VARCHAR(100), GamesAsCatcher VARCHAR(100), GamesAsFirstBaseman VARCHAR(100), GamesAsSecondBaseman VARCHAR(100), GamesAsThirdBaseman VARCHAR(100), GamesAsShortstop VARCHAR(100), GamesAsLeftfielder VARCHAR(100), GamesAsCenterfielder VARCHAR(100), GamesAsRightfielder VARCHAR(100), GamesAsOutfielder VARCHAR(100), GamesAsDesignatedHitter VARCHAR(100), GamesAsPinchHitter VARCHAR(100), GamesAsPinchRunner VARCHAR(100)
);

CREATE TABLE Awards (
awardID VARCHAR(100), year VARCHAR(100), leagueID VARCHAR(100), personID VARCHAR(100), pointsWon VARCHAR(100), pointsMax VARCHAR(100), votesFirst VARCHAR(100), tie VARCHAR(100), notes VARCHAR(100), isShared VARCHAR(100)
);

CREATE TABLE Batting (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), Games VARCHAR(100), AtBats VARCHAR(100), Runs VARCHAR(100), Hits VARCHAR(100), Doubles VARCHAR(100), Triples VARCHAR(100), HomeRuns VARCHAR(100), RunsBattedIn VARCHAR(100), StolenBases VARCHAR(100), CaughtStealing VARCHAR(100), BaseOnBalls VARCHAR(100), StrikeOuts VARCHAR(100), IntentionalWalks VARCHAR(100), HitByPitch VARCHAR(100), SacrificeHits VARCHAR(100), SacrificeFlies VARCHAR(100), GroundedIntoDoublePlays VARCHAR(100), isPostSeason VARCHAR(100), round VARCHAR(100)
);

CREATE TABLE CollegePlaying (
personID VARCHAR(100), schoolID VARCHAR(100), year VARCHAR(100)
);

CREATE TABLE Divisions (
rowID VARCHAR(100), divisionID VARCHAR(100), divisionName VARCHAR(100), isActive VARCHAR(100)
);

CREATE TABLE Fielding (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), Position VARCHAR(100), Games VARCHAR(100), GamesStarted VARCHAR(100), InnOuts VARCHAR(100), Putouts VARCHAR(100), Assists VARCHAR(100), Errors VARCHAR(100), DoublePlays VARCHAR(100), TP VARCHAR(100), PassedBallsByCatchers VARCHAR(100), WildPitchesByCatchers VARCHAR(100), OpponentStolenBasesByCatchers VARCHAR(100), OpponentsCaughtStealingByCatchers VARCHAR(100), ZoneRating VARCHAR(100), round VARCHAR(100), isPostSeason VARCHAR(100)
);

CREATE TABLE FieldingOF (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), Games played in left field VARCHAR(100), Games played in center field VARCHAR(100), Games played in right field VARCHAR(100)
);

CREATE TABLE FieldingOFsplit (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), POS VARCHAR(100), Games VARCHAR(100), GamesStarted VARCHAR(100), InnOuts VARCHAR(100), Putouts VARCHAR(100), Assists VARCHAR(100), Errors VARCHAR(100), DoublePlays VARCHAR(100)
);

CREATE TABLE Franchises (
franchID VARCHAR(100), franchName VARCHAR(100), active VARCHAR(100), NAassoc VARCHAR(100)
);

CREATE TABLE HallOfFame (
personID VARCHAR(100), year VARCHAR(100), votedBy VARCHAR(100), ballots VARCHAR(100), needed VARCHAR(100), votes VARCHAR(100), inducted VARCHAR(100), category VARCHAR(100), needed_note VARCHAR(100)
);

CREATE TABLE Leagues (
leagueID VARCHAR(100), leagueName VARCHAR(100), isActive VARCHAR(100)
);

CREATE TABLE Managers (
personID VARCHAR(100), year VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), inseason VARCHAR(100), half VARCHAR(100), GamesManaged VARCHAR(100), Wins VARCHAR(100), Losses VARCHAR(100), rank VARCHAR(100), plyrMgr VARCHAR(100), isSeasonHalf VARCHAR(100)
);

CREATE TABLE Parks (
parkID VARCHAR(100), parkName VARCHAR(100), parkAlias VARCHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100)
);

CREATE TABLE People (
personID VARCHAR(100), nameFirst VARCHAR(100), nameLast VARCHAR(100), birthYear VARCHAR(100), birthMonth VARCHAR(100), birthDay VARCHAR(100), birthCountry VARCHAR(100), birthState VARCHAR(100), birthCity VARCHAR(100), deathYear VARCHAR(100), deathMonth VARCHAR(100), deathDay VARCHAR(100), deathCountry VARCHAR(100), deathState VARCHAR(100), deathCity VARCHAR(100), weight VARCHAR(100), height VARCHAR(100), bats VARCHAR(100), throws VARCHAR(100), debut VARCHAR(100), finalGame VARCHAR(100), retroID VARCHAR(100), bbrefID VARCHAR(100)
);

CREATE TABLE Pitching (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), Wins VARCHAR(100), Losses VARCHAR(100), Games VARCHAR(100), GamesStarted VARCHAR(100), CompleteGames VARCHAR(100), Shutouts VARCHAR(100), Saves VARCHAR(100), IPouts VARCHAR(100), Hits VARCHAR(100), EarnedRuns VARCHAR(100), Homeruns VARCHAR(100), Walks VARCHAR(100), Strikeouts VARCHAR(100), OpponentsBattingAvg VARCHAR(100), EarnedRunAvg VARCHAR(100), IntentionalWalks VARCHAR(100), WildPitches VARCHAR(100), BattersHitByPitch VARCHAR(100), Balks VARCHAR(100), BattersFacedByPitcher VARCHAR(100), GamesFinished VARCHAR(100), RunsAllowed VARCHAR(100), SacrificesByOpposingBatters VARCHAR(100), SacrificeFliesByOpposingBatters VARCHAR(100), GIDPByOpposingBatter VARCHAR(100), round VARCHAR(100), isPostSeason VARCHAR(100)
);

CREATE TABLE Players (
personID VARCHAR(100), year VARCHAR(100), stint VARCHAR(100), teamID VARCHAR(100), isPostSeason VARCHAR(100), isPitching VARCHAR(100), isBatting VARCHAR(100), isFielding VARCHAR(100)
);

CREATE TABLE PostSeasonSeries (
year VARCHAR(100), round VARCHAR(100), teamIDwinner VARCHAR(100), leagueIDWinner VARCHAR(100), teamIDloser VARCHAR(100), leagueIDLoser VARCHAR(100), wins VARCHAR(100), losses VARCHAR(100), ties VARCHAR(100)
);

CREATE TABLE Salaries (
personID VARCHAR(100), year VARCHAR(100), teamID VARCHAR(100), leagueID VARCHAR(100), salary VARCHAR(100)
);

CREATE TABLE Schools (
schoolID VARCHAR(100), name_full VARCHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100)
);

CREATE TABLE Teams (
year VARCHAR(100), leagueID VARCHAR(100), teamID VARCHAR(100), teamName VARCHAR(100), franchID VARCHAR(100), divisionID VARCHAR(100), Rank VARCHAR(100), GamesPlayed VARCHAR(100), GamesPlayedAtHome VARCHAR(100), Wins VARCHAR(100), Losses VARCHAR(100), DivisionWinner VARCHAR(100), WildcardWinner VARCHAR(100), LeagueChampion VARCHAR(100), WorldSeriesWinner VARCHAR(100), Runs VARCHAR(100), AtBats VARCHAR(100), HitsByBatters VARCHAR(100), Doubles VARCHAR(100), Triples VARCHAR(100), HomeRunsByBatters VARCHAR(100), WalksByBatters VARCHAR(100), StrikeoutsByBatters VARCHAR(100), StolenBases VARCHAR(100), CaughtStealing VARCHAR(100), BattersHitByPitch VARCHAR(100), SacrificeFlies VARCHAR(100), OpponentsRunsScored VARCHAR(100), EarnedRunsAllowed VARCHAR(100), EarnedRunAvg VARCHAR(100), CompleteGames VARCHAR(100), Shutouts VARCHAR(100), Saves VARCHAR(100), OutsPitched VARCHAR(100), HitsAllowed VARCHAR(100), HomeRunsAllowed VARCHAR(100), WalksAllowed VARCHAR(100), StrikeoutsByPitchers VARCHAR(100), Errors VARCHAR(100), DoublePlays VARCHAR(100), FieldingPercentage VARCHAR(100), parkName VARCHAR(100), attendance VARCHAR(100), ThreeYearParkFactorBatters VARCHAR(100), ThreeYearParkFactorPitchers VARCHAR(100), teamIDBR VARCHAR(100), teamIDlahman45 VARCHAR(100), teamIDretro VARCHAR(100)
);

CREATE TABLE TeamsHalf (
year VARCHAR(100), leagueID VARCHAR(100), teamID VARCHAR(100), Half VARCHAR(100), divID VARCHAR(100), DivWin VARCHAR(100), Rank VARCHAR(100), G VARCHAR(100), W VARCHAR(100), L VARCHAR(100)
);

