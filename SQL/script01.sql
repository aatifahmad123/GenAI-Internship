CREATE DATABASE metabase_db;

-- SHOW DATABASES;

USE metabase_db;

DROP TABLE IF EXISTS Agents;
DROP TABLE IF EXISTS Calls;
DROP TABLE IF EXISTS Intents;

-- SHOW TABLES;

CREATE TABLE Agents (
    agent_id INT PRIMARY KEY, -- unique identifier for each agent
    chirp3_hd_voice VARCHAR(50), -- Chirp3 HD voice of the agent
    gender ENUM ('Male','Female'), -- gender of agent
    num_customers_handled INT, -- number of customers handled by the agent
    average_call_duration FLOAT, -- avg call duration handled by the agent (secs)
    average_professionalism FLOAT, -- avg professionalism rating of the agent (0-10)
    average_performance FLOAT, -- avg performance rating of the agent (0-10)
    average_customer_satisfaction FLOAT -- avg customer satisfaction rating of the agent (0-10)
);

CREATE TABLE Calls (
    call_id INT PRIMARY KEY, -- unique identifier for each call
    agent_id INT, -- link to Agents table
    duration FLOAT, -- Call duration in seconds
    summary TEXT, -- Summary of the call
    interruptions_by_customer INT, -- Number of customer interruptions
    interruptions_by_agent INT, -- Number of agent interruptions
    basic_greeting_closing BOOLEAN, -- Whether basic greeting/closing was used
    fatal_behavior BOOLEAN, -- Whether fatal behavior was observed
    agent_professionalism INT, -- Agent professionalism score (0-10)
    agent_performance INT, -- Agent performance score (0-10)
    customer_satisfaction INT, -- Customer satisfaction score (0-10)
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Intents (
    intent_id VARCHAR(50) PRIMARY KEY, -- Unique identifier for intent
    call_id INT, -- Links to the Calls table
    intent VARCHAR(255), -- Intent description (e.g., Billing Dispute)
    confidence FLOAT, -- Confidence score (0-100)
    keywords TEXT, -- Keywords associated with the intent
    intent_begin_timestamp FLOAT, -- Start timestamp of intent in seconds
    intent_end_timestamp FLOAT, -- End timestamp of intent in seconds
    products TEXT, -- Products mentioned (e.g., Credit Card)
    issues TEXT, -- Issues described (e.g., Duplicate charge)
    actions_of_agent TEXT, -- Actions taken by agent
    resolution_status ENUM('Resolved', 'Unresolved', 'Pending with Process Request', 'Pending with Customer'), -- Resolution status
    process_request TEXT, -- Details of process request
    resolution TEXT, -- Resolution description
    resolution_begin_timestamp FLOAT, -- Start timestamp of resolution
    resolution_end_timestamp FLOAT, -- End timestamp of resolution
    dominant_emotions_customer TEXT, -- Customer emotions (e.g., Frustration, Anger)
    conversation_sentiment ENUM('Positive', 'Negative', 'Neutral'), -- Sentiment of conversation
    customer_satisfaction INT, -- Customer satisfaction for this intent (0-100)
    callback_promise BOOLEAN, -- Whether a callback was promised
    callback_time VARCHAR(50), -- Callback time or N/A
    FOREIGN KEY (call_id) REFERENCES Calls(call_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- SHOW TABLES;

-- SELECT * FROM Agents;
-- SELECT * FROM Calls;
-- SELECT * FROM Intents;