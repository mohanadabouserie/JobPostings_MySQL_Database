-- database definitions
CREATE DATABASE IF NOT EXISTS wuzzuf;

ALTER DATABASE wuzzuf
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE wuzzuf;


-- wuzzuf_user table
CREATE TABLE IF NOT EXISTS wuzzuf_user (
username              VARCHAR(50)               NOT NULL          PRIMARY KEY,
email_address         VARCHAR(255)              NOT NULL,
gpa                   DECIMAL(3,2)              NOT NULL,
birthdate             DATE                      NOT NULL,
gender                CHAR                      NOT NULL  
);

LOAD DATA INFILE 'wuzzuf_users.csv'
INTO TABLE wuzzuf_user
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(username, email_address, gpa, birthdate, gender);


-- user_skills table
CREATE TABLE IF NOT EXISTS user_skills (
username              VARCHAR(255)              NOT NULL,
skill                 VARCHAR(255)              NOT NULL,
PRIMARY KEY           (username, skill),
FOREIGN KEY           (username)                REFERENCES wuzzuf_user(username)                   ON DELETE CASCADE       ON UPDATE CASCADE
);

LOAD DATA INFILE 'users_skills.csv'
INTO TABLE user_skills
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(username, skill);


-- company table
CREATE TABLE IF NOT EXISTS company (
company_url           VARCHAR(2000),
company_name          VARCHAR(255)              NOT NULL          PRIMARY KEY,
foundation_date       INT,
minimum_size          DECIMAL(4,0),
maximum_size          DECIMAL(4,0),
company_about         TEXT,
city                  VARCHAR(255),
country               VARCHAR(255)     
);

LOAD DATA INFILE 'company_data_final.csv'
INTO TABLE company
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(company_url, company_name, foundation_date, minimum_size, maximum_size, company_about, city, country);

UPDATE company
SET foundation_date = NULL
WHERE foundation_date = -1;

UPDATE company
SET minimum_size = NULL
WHERE minimum_size = -1;

UPDATE company
SET maximum_size = NULL
WHERE maximum_size = -1;


-- company_industry table
CREATE TABLE IF NOT EXISTS company_industry (
company_name          VARCHAR(255)              NOT NULL,
industry              VARCHAR(255)              NOT NULL,
PRIMARY KEY           (company_name, industry)
);

LOAD DATA INFILE 'company_industries.csv'
INTO TABLE company_industry
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(company_name, industry);


-- job_posting table
CREATE TABLE IF NOT EXISTS job_posting (
title                 VARCHAR(255)              NOT NULL, 
experience_needed     DECIMAL(2,0),
career_level          VARCHAR(255),
educational_level     VARCHAR(255),
min_salary            DECIMAL(15,0),
max_salary            DECIMAL(15,0),
gender                VARCHAR(255),
job_description       VARCHAR(5000),
requirements          VARCHAR(5000),
vacancies             DECIMAL(2,0),
company_name          VARCHAR(255)              NOT NULL,
Location_Part1        VARCHAR(255),
Location_Part2        VARCHAR(255),
PRIMARY KEY           (title, company_name),
FOREIGN KEY           (company_name)            REFERENCES company(company_name)                   ON DELETE CASCADE       ON UPDATE CASCADE
);

LOAD DATA INFILE 'job_postings_data_final.csv'
INTO TABLE job_posting
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(title, experience_needed, career_level, educational_level, min_salary, max_salary, gender, job_description, requirements, vacancies, company_name, Location_Part1, Location_Part2);

UPDATE job_posting
SET experience_needed = NULL
WHERE experience_needed = -1;

UPDATE job_posting
SET min_salary = NULL
WHERE min_salary = -1;

UPDATE job_posting
SET max_salary = NULL
WHERE max_salary = -1;


-- job_posting_skills table
CREATE TABLE IF NOT EXISTS job_posting_skills (
title                 VARCHAR(255)              NOT NULL,
company_name          VARCHAR(255)              NOT NULL,
skill                 VARCHAR(255)              NOT NULL,
PRIMARY KEY           (title, company_name, skill),
FOREIGN KEY           (title, company_name)     REFERENCES job_posting(title, company_name)        ON DELETE CASCADE       ON UPDATE CASCADE
);

LOAD DATA INFILE 'job_skills.csv'
INTO TABLE job_posting_skills
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(title, company_name, skill);


-- job_posting_categories table
CREATE TABLE IF NOT EXISTS job_posting_categories (
title                 VARCHAR(255)              NOT NULL,
company_name          VARCHAR(255)              NOT NULL,
category              VARCHAR(255)              NOT NULL,
PRIMARY KEY           (title, company_name, category),
FOREIGN KEY           (title, company_name)     REFERENCES job_posting(title, company_name)        ON DELETE CASCADE       ON UPDATE CASCADE
);

LOAD DATA INFILE 'job_categories.csv'
INTO TABLE job_posting_categories
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(title, company_name, category);


-- job_posting_types table
CREATE TABLE IF NOT EXISTS job_posting_types (
title                 VARCHAR(255)              NOT NULL,
company_name          VARCHAR(255)              NOT NULL,
job_type              VARCHAR(255)              NOT NULL,
PRIMARY KEY           (title, company_name, job_type),
FOREIGN KEY           (title, company_name)     REFERENCES job_posting(title, company_name)        ON DELETE CASCADE       ON UPDATE CASCADE
);

LOAD DATA INFILE 'job_types.csv'
INTO TABLE job_posting_types
FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(title, company_name, job_type);


-- application table
CREATE TABLE IF NOT EXISTS application (
username              VARCHAR(50)               NOT NULL          PRIMARY KEY,
title                 VARCHAR(255)              NOT NULL,
company_name          VARCHAR(255)              NOT NULL,
application_date      DATE                      NOT NULL,
cover_letter          TEXT                      NOT NULL,      
FOREIGN KEY           (username)                REFERENCES wuzzuf_user(username)                   ON DELETE CASCADE       ON UPDATE CASCADE,
FOREIGN KEY           (title, company_name)     REFERENCES job_posting(title, company_name)        ON DELETE CASCADE       ON UPDATE CASCADE
);