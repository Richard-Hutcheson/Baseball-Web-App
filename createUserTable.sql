CREATE TABLE User (
    userId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    favoriteTeam VARCHAR(255)
);