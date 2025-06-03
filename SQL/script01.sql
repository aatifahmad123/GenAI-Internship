SHOW DATABASES;

USE metabase_db;

CREATE TABLE Agents (
    agent_id INT PRIMARY KEY,
    chirp3_hd_voice VARCHAR(50),
    gender ENUM('Male', 'Female'),
    num_customers_handled INT,
    avg_performance_score FLOAT,
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
    interruptions_by_agent INT
);

CREATE TABLE Intents (
    intent_id VARCHAR(10) PRIMARY KEY,
    intent VARCHAR(255),
    confidence FLOAT,
    keywords TEXT,
    products TEXT,
    issues TEXT,
    actions_of_agent TEXT,
    resolution_status ENUM('Resolved', 'Unresolved', 'Pending'),
    resolution TEXT,
    dominant_emotions_customer TEXT,
    conversation_sentiment VARCHAR(50),
    agent_professionalism TEXT,
    agent_performance INT,
    customer_satisfaction INT,
    callback_promise BOOLEAN,
    callback_time TEXT
);

SHOW TABLES;

SELECT * FROM Agents;
SELECT * FROM Calls;
SELECT * FROM Intents;

