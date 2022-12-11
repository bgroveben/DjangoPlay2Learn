DROP DATABASE IF EXISTS play2learn;

CREATE DATABASE play2learn;

--
-- Table structure for users
--
CREATE TABLE play2learn.users (
	user_id int(11) NOT NULL auto_increment,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    username varchar(30) NOT NULL,
    pass_phrase varchar(500) NOT NULL,
    is_admin tinyint(4) NOT NULL DEFAULT 0,
    date_registered datetime NOT NULL DEFAULT current_timestamp,
    registration_confirmed tinyint(4) NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id)
);

--
-- Table structure for tokens
--
CREATE TABLE play2learn.tokens (
	token_id int(11) NOT NULL auto_increment,
    token char(64) DEFAULT NULL,
    user_id int(11) REFERENCES users (user_id),
    token_expires datetime DEFAULT NULL,
    PRIMARY KEY (token_id)
);

--
-- Table structure for reviews
--
CREATE TABLE play2learn.reviews (
	review_id int(11) NOT NULL auto_increment,
    user_id int(11) REFERENCES users(user_id),
    review longtext NOT NULL,
    featured tinyint(4) NOT NULL DEFAULT 0,
    PRIMARY KEY (review_id)
);

--
-- Table structure for math facts scores
--
CREATE TABLE play2learn.math_facts_scores (
	score_id int(11) NOT NULL auto_increment,
    user_id int(11) REFERENCES users(user_id),
    score int(11) NOT NULL,
    max_number int(11) NOT NULL,
    operation varchar(30),
    end_time datetime NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (score_id)
);

--
-- Table structure for anagram scores
--
CREATE TABLE play2learn.anagram_hunt_scores (
	score_id int(11) NOT NULL auto_increment,
    user_id int(11) REFERENCES users(user_id),
    score int(11) NOT NULL,
    max_number int(11) NOT NULL,
    operation varchar(30),
    end_time datetime NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (score_id)
);