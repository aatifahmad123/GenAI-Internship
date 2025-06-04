USE metabase_db;

-- Insert into Calls table

-- Insert into Intents table

-- Insert into Agents table
INSERT INTO Agents (
    agent_id,
    chirp3_hd_voice,
    gender,
    num_customers_handled,
    avg_performance_score,
    avg_customer_satisfaction
) VALUES
(1, 'Autonoe', 'Female', 10, 8.71, 7.00),
(2, 'Sulafat', 'Female', 10, 8.75, 7.08),
(3, 'Erinome', 'Female', 10, 8.86, 7.86),
(4, 'Sadaltager', 'Male', 10, 8.54, 7.15),
(5, 'Schedar', 'Male', 10, 8.54, 7.23);