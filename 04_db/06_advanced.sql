-- Transaction
SET autocommit = 0;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
	PRIMARY KEY (id)
);

START TRANSACTION;
INSERT INTO users (name) 
VALUES ('harry'), ('test');
SELECT * FROM users;
-- ROLLBACK; 혹은 COMMIT; 
	

-- Triggers
DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;

DELIMITER //
CREATE TRIGGER myTrigger
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id = 1;

SELECT * FROM articles;

CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER recordLogs 
	AFTER INSERT 
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES ('글이 작성되었어요.', CURRENT_DATE());
END//
DELIMITER ;

SHOW TRIGGERS;
    
INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;
SELECT * FROM articleLogs;
DROP TRIGGER recordLogs;

DELIMITER //
CREATE TRIGGER recordLogs 
	AFTER INSERT 
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES (CONCAT(NEW.id, '번 글이 작성되었어요.'), CURRENT_DATE());
END//
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;
SELECT * FROM articleLogs;

CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backupLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

DELETE FROM articles
WHERE id = 1;

SELECT * FROM articles;
SELECT * FROM backupArticles;
