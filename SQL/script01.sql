SHOW DATABASES;

USE metabase_db;

DROP TABLE IF EXISTS Agents;
DROP TABLE IF EXISTS Calls;
DROP TABLE IF EXISTS Intents;

SHOW TABLES;

CREATE TABLE Agents (
    agent_id INT PRIMARY KEY,
    chirp3_hd_voice VARCHAR(50),
    gender ENUM('Male', 'Female'),
    num_customers_handled INT,
    avg_call_duration FLOAT,
    avg_professionalism FLOAT,
    avg_performance FLOAT,
    avg_customer_satisfaction FLOAT
);

CREATE TABLE Calls (
    call_id INT PRIMARY KEY,
    agent_id INT,
    duration FLOAT,
    summary TEXT,
    num_intents INT,
    intent_1_id VARCHAR(50),
    intent_2_id VARCHAR(50),
    interruptions_by_customer INT,
    interruptions_by_agent INT,
    basic_greeting_closing BOOLEAN,
    fatal_behavior BOOLEAN,
    agent_professionalism INT,
    agent_performance INT,
);

CREATE TABLE Intents (
    intent_id VARCHAR(10) PRIMARY KEY,
    intent VARCHAR(255),
    confidence FLOAT,
    keywords TEXT,
    intent_begin_timestamp INT,
    intent_end_timestamp INT,
    products TEXT,
    issues TEXT,
    actions_of_agent TEXT,
    resolution_status ENUM('Resolved', 'Unresolved', 'Pending with Process Request','Pending with Customer'),
    process_request TEXT,
    resolution TEXT,
    resolution_begin_timestamp INT,
    resolution_end_timestamp INT,
    dominant_emotions_customer TEXT,
    conversation_sentiment ENUM('Positive', 'Negative', 'Neutral'),
    customer_satisfaction INT,
    callback_promise BOOLEAN,
    callback_time TEXT
);

SHOW TABLES;

SELECT * FROM Agents;
SELECT * FROM Calls;
SELECT * FROM Intents;

