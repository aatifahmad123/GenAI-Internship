USE metabase_db;

UPDATE Agents
SET
    num_customers_handled = 30,
    average_call_duration = 35.21,
    average_professionalism = 8.57,
    average_performance = 8.50,
    average_customer_satisfaction = 7.73
WHERE agent_id = 1;

UPDATE Agents
SET
    num_customers_handled = 30,
    average_call_duration = 31.91,
    average_professionalism = 8.63,
    average_performance = 8.50,
    average_customer_satisfaction = 7.73
WHERE agent_id = 2;

UPDATE Agents
SET
    num_customers_handled = 30,
    average_call_duration = 32.14,
    average_professionalism = 8.70,
    average_performance = 8.57,
    average_customer_satisfaction = 7.97
WHERE agent_id = 3;

UPDATE Agents
SET
    num_customers_handled = 30,
    average_call_duration = 30.68,
    average_professionalism = 8.50,
    average_performance = 8.37,
    average_customer_satisfaction = 7.60
WHERE agent_id = 4;

UPDATE Agents
SET
    num_customers_handled = 30,
    average_call_duration = 29.43,
    average_professionalism = 8.63,
    average_performance = 8.53,
    average_customer_satisfaction = 8.07
WHERE agent_id = 5;

SELECT * FROM Agents

ALTER TABLE Calls
ADD COLUMN Language VARCHAR(20);

UPDATE Calls
SET Language = 'English'
WHERE call_id <= 50;

SELECT * FROM Calls;

INSERT INTO Calls (call_id, agent_id, duration, summary, interruptions_by_customer, interruptions_by_agent, basic_greeting_closing, fatal_behavior, agent_professionalism, agent_performance, customer_satisfaction, callback_promise, callback_time, Language)
VALUES
    (51, 1, 45.56, 'The agent resolved the customer''s debit card issue.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (52, 1, 38, 'Customer''s home loan EMI was not deducted, agent assisted.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (53, 1, 33.96, 'The customer reported a fraudulent transaction on their credit card.', 0, 0, TRUE, FALSE, 8, 8, 7, FALSE, 'N/A', 'Hindi'),
    (54, 1, 29.80, 'Customer inquired about fixed deposit interest credit not received.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (55, 1, 30, 'Agent blocked the lost ATM card and informed about replacement.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (56, 1, 33.56, 'Agent initiated fraud claim for unauthorized transaction and refund.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (57, 1, 33, 'The agent assisted with credit card limit increase request.', 0, 0, FALSE, FALSE, 8, 8, 7, FALSE, 'N/A', 'Hindi'),
    (58, 1, 29, 'Customer inquired about loan application rejection and sought guidance.', 0, 0, TRUE, FALSE, 9, 8, 7, FALSE, 'N/A', 'Hindi'),
    (59, 1, 26, 'The customer requests an update to their passbook.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (60, 1, 32, 'Customer inquired about redeeming credit card reward points.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (61, 2, 36, 'The customer reported an incorrect interest credit in their account.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (62, 2, 33, 'Agent initiated refund for duplicate debit card transaction.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (63, 2, 26, 'The agent helped the customer reset his net banking password.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (64, 2, 29, 'Customer inquired about a sudden increase in loan interest rate.', 0, 0, TRUE, FALSE, 8, 7, 6, FALSE, 'N/A', 'Hindi'),
    (65, 2, 26, 'Customer forgot ATM pin, agent initiated pin reset request.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (66, 2, 31.20, 'Customer reports incorrect transaction in account statement, agent resolves.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (67, 2, 33, 'Agent processed customer''s request for annual fee waiver.', 0, 0, TRUE, FALSE, 9, 8, 7, FALSE, 'N/A', 'Hindi'),
    (68, 2, 28, 'Agent assisted customer with KYC update for locked account.', 0, 0, TRUE, FALSE, 9, 8, 8, FALSE, 'N/A', 'Hindi'),
    (69, 2, 31.92, 'Customer is facing issues with X registration, agent provides resolution.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (70, 2, 31.84, 'The agent resolved the customer''s issue of not receiving statements.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (71, 3, 34, 'Customer reported an unknown charge, agent processed refund request.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (72, 3, 37, 'The agent resolved the customer''s international transaction issue.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (73, 3, 31, 'Customer inquired about home loan prepayment charges and waiver.', 0, 0, TRUE, FALSE, 8, 7, 7, FALSE, 'N/A', 'Hindi'),
    (74, 3, 30, 'Customer unable to login to mobile banking app, issue resolved.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (75, 3, 29, 'Agent helped customer with maturity details and sent statement.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (76, 3, 31, 'The customer reported a name discrepancy on their account.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (77, 3, 33, 'Customer reported EMI conversion issue, agent resolved it.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (78, 3, 30, 'Agent addressed loan statement error and submitted update request.', 0, 0, TRUE, FALSE, 9, 8, 7, FALSE, 'N/A', 'Hindi'),
    (79, 3, 32, 'Agent assisted customer with failed NEFT transfer.', 0, 0, TRUE, FALSE, 9, 8, 7, FALSE, 'N/A', 'Hindi'),
    (80, 3, 30.76, 'Customer inquired about missing cashback on credit card.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (81, 4, 32, 'Agent assisted customer with balance update issue.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (82, 4, 32, 'Customer reported credit card PIN generation failure, agent reinitiated process.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (83, 4, 27.20, 'The agent helped the customer check loan approval status.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (84, 4, 33, 'Agent issued a new card due to CVV error.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (85, 4, 32, 'Customer reports incorrect name linked to account, agent assists.', 0, 0, TRUE, FALSE, 9, 8, 8, FALSE, 'N/A', 'Hindi'),
    (86, 4, 32.92, 'Customer is unhappy with the credit card reward program change.', 0, 0, TRUE, FALSE, 8, 7, 5, FALSE, 'N/A', 'Hindi'),
    (87, 4, 29, 'Customer reported a failed RTGS transfer, agent identified incorrect details.', 0, 0, TRUE, FALSE, 8, 7, 6, FALSE, 'N/A', 'Hindi'),
    (88, 4, 28, 'The customer inquired about their loan insurance coverage.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (89, 4, 32, 'The customer inquired about a decrease in their debit card limit.', 0, 0, TRUE, FALSE, 8, 8, 7, FALSE, 'N/A', 'Hindi'),
    (90, 4, 32.92, 'The agent updated the customer''s mobile number.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (91, 5, 31, 'Customer reported direct debit setup issue, agent provided resolution.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (92, 5, 30.88, 'Customer reported non-delivery of credit card statement, resolved by email.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (93, 5, 29, 'Customer inquired about the delay in loan processing fee refund.', 0, 0, TRUE, FALSE, 9, 8, 8, FALSE, 'N/A', 'Hindi'),
    (94, 5, 32, 'Agent assisted customer with unauthorized debit card transaction.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (95, 5, 26, 'Agent manually renewed customer''s FB due to technical error.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (96, 5, 30, 'Customer reported an incorrect email address and agent updated it.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi'),
    (97, 5, 37, 'Customer requests to revert credit card billing cycle.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (98, 5, 27, 'Customer requests loan repayment schedule, agent provides resolution.', 0, 0, TRUE, FALSE, 9, 9, 9, FALSE, 'N/A', 'Hindi'),
    (99, 5, 29, 'Customer is unable to set online limit for debit card.', 0, 0, TRUE, FALSE, 9, 8, 7, FALSE, 'N/A', 'Hindi'),
    (100, 5, 31, 'Customer inquired about mutual fund amount not credited.', 0, 0, TRUE, FALSE, 9, 9, 8, FALSE, 'N/A', 'Hindi');


SELECT * FROM Calls;

INSERT INTO Intents (intent_id, call_id, intent, confidence, keywords, intent_begin_timestamp, intent_end_timestamp, products, issues, actions_of_agent, resolution_status, process_request, resolution, resolution_begin_timestamp, resolution_end_timestamp, dominant_emotions_customer, conversation_sentiment, customer_satisfaction)
VALUES
    ('51_1', 51, 'Billing Dispute', 95, 'Duplicate charge on credit card', 0.0, 16.0, 'Credit Card', 'Duplicate charge', 'Agent initiated a chargeback request.', 'Pending with Callback', 'Chargeback request initiated.', 'Refund will be processed in 5-7 business days.', 51.0, 55.0, 'Frustration', 'Negative', 50),
    ('52_1', 52, 'EMI Deduction Issue', 95, 'Home loan EMI not deducted', 0.0, 10.0, 'Home Loan', 'EMI not deducted', 'Agent informed the customer about insufficient balance.', 'Resolved', 'N/A', 'Customer advised to deposit balance and retry auto-debit.', 31.0, 36.0, 'Surprise', 'Neutral', 85),
    ('53_1', 53, 'Fraudulent Transaction Report', 95, 'Fraudulent transaction on credit card', 0.0, 16.0, 'Credit Card', 'Fraudulent transaction', 'Agent blocked the card and initiated a refund.', 'Resolved', 'Refund initiated', 'Card blocked and refund process started.', 20.0, 24.0, 'Anxiety', 'Negative', 70),
    ('54_1', 54, 'Fixed Deposit Inquiry', 95, 'FD interest credit not received', 0.0, 10.0, 'Fixed Deposit', 'Interest credit issue', 'Agent informed about quarterly credit cycle.', 'Resolved', 'N/A', 'Interest will be credited next week.', 17.0, 21.0, 'Concern', 'Neutral', 80),
    ('55_1', 55, 'Block Lost ATM Card', 95, 'ATM card lost', 0.0, 9.0, 'ATM Card', 'Lost ATM card', 'Blocked the ATM card after verifying the account number.', 'Resolved', 'Backend process to block the card.', 'ATM card blocked and new card will be sent in 5 days.', 18.0, 24.0, 'Urgency', 'Neutral', 90),
    ('55_2', 55, 'Inquire about Replacement Charges', 90, 'Replacement charges', 20.0, 27.0, 'ATM Card', NULL, 'Informed the customer that the first replacement is free.', 'Resolved', 'N/A', 'First replacement is free of charge.', 26.0, 29.0, 'Inquisitive', 'Neutral', 100),
    ('56_1', 56, 'Fraudulent Transaction Reporting', 95, 'Unauthorized transaction on debit card', 0.0, 29.0, 'Debit Card', 'Unauthorized transaction', 'Agent initiated fraud claim and refund process.', 'Resolved', 'Fraud claim initiated.', 'Refund will be processed in 7-10 working days.', 28.0, 33.0, 'Frustration', 'Negative', 80),
    ('57_1', 57, 'Credit Card Limit Inquiry', 95, 'Credit card limit increase request', 0.0, 8.0, 'Credit Card', 'Limit increase request', 'Agent initiated a request to increase the limit.', 'Pending with Callback', 'Limit increase request submitted.', 'Limit increase will take 3-5 days.', 27.0, 32.0, 'Inquiry', 'Neutral', 75),
    ('58_1', 58, 'Loan Application Status Inquiry', 95, 'Loan application rejection inquiry', 0.0, 16.0, 'Loan', 'Application rejected', 'Agent provided reason for rejection and guidance for re-application.', 'Unresolved', 'N/A', 'Credit improvement tips emailed.', 24.0, 30.0, 'Inquiry', 'Neutral', 70),
    ('59_1', 59, 'Passbook Update Request', 95, 'Passbook update request', 0.0, 8.0, 'Passbook', 'Update request', 'Agent processed digital statement request.', 'Resolved', 'Digital statement sent.', 'Statement sent to registered email.', 22.0, 27.0, 'Neutral', 'Neutral', 90),
    ('60_1', 60, 'Reward Points Redemption', 95, 'Redeeming credit card reward points', 0.0, 9.0, 'Credit Card', 'Reward points redemption', 'Agent provided guidance on redemption.', 'Resolved', 'N/A', 'Steps emailed to customer.', 26.0, 29.0, 'Neutral', 'Neutral', 90),
    ('61_1', 61, 'Billing Inquiry', 95, 'Incorrect interest credit in account', 0.0, 9.0, 'Savings Account', 'Incorrect interest credit', 'Agent initiated correction request.', 'Resolved', 'Interest correction request submitted.', 'Interest will be updated in 3-5 days.', 26.0, 30.0, 'Neutral', 'Neutral', 80),
    ('62_1', 62, 'Fraudulent Transaction Reporting', 95, 'Duplicate debit card transaction', 0.0, 8.0, 'Debit Card', 'Duplicate transaction', 'Agent initiated refund process.', 'Resolved', 'Refund initiated.', 'Refund will be processed in 7 days.', 22.0, 28.0, 'Anxiety', 'Neutral', 80),
    ('63_1', 63, 'Password Reset', 95, 'Net banking password reset request', 0.0, 8.0, 'Net Banking', 'Password reset', 'Agent sent password reset link.', 'Resolved', 'Password reset link sent.', 'Reset link sent to registered email.', 12.0, 18.0, 'Frustration', 'Neutral', 90),
    ('64_1', 64, 'Interest Rate Inquiry', 95, 'Loan interest rate increase inquiry', 0.0, 8.0, 'Loan', 'Interest rate increase', 'Agent submitted review request.', 'Pending with Callback', 'Review request submitted.', 'Details emailed to customer.', 21.0, 26.0, 'Surprise', 'Neutral', 60),
    ('65_1', 65, 'ATM Pin Reset', 95, 'Forgot ATM PIN', 0.0, 19.0, 'ATM Card', 'Forgotten PIN', 'Verified customer details and initiated a request to generate a new ATM PIN.', 'Resolved', 'New ATM PIN generation request.', 'New ATM PIN will be sent via SMS in 48 hours.', 13.0, 19.0, 'Neutral', 'Neutral', 90),
    ('65_2', 65, 'Check for Charges', 90, 'Charges for PIN reset', 18.0, 21.0, 'ATM Card', NULL, 'Informed the customer that there are no charges for the service.', 'Resolved', 'N/A', 'Confirmed that the service is free of charge.', 21.0, 23.0, 'Neutral', 'Neutral', 100),
    ('66_1', 66, 'Statement Issue', 95, 'Incorrect transaction in account statement', 0.0, 8.0, 'Account Statement', 'Incorrect transaction', 'Agent submitted correction request.', 'Resolved', 'Correction request submitted.', 'Issue will be resolved in 3 days.', 26.0, 27.0, 'Neutral', 'Neutral', 80),
    ('67_1', 67, 'Fee Waiver Request', 95, 'Annual fee waiver request', 0.0, 9.0, 'Credit Card', 'Fee waiver request', 'Agent submitted fee waiver request.', 'Pending with Callback', 'Fee waiver request submitted.', 'Update in 5-7 days.', 20.0, 29.0, 'Inquisitive', 'Neutral', 75),
    ('68_1', 68, 'Account Access Issue', 95, 'KYC update for locked account', 0.0, 13.0, 'Bank Account', 'KYC update', 'Agent sent online KYC link.', 'Resolved', 'KYC link sent.', 'Online KYC link sent to customer.', 21.0, 24.0, 'Concerned', 'Neutral', 80),
    ('69_1', 69, 'Technical Issue', 95, 'X registration issue', 0.0, 9.0, 'X Registration', 'Incomplete form', 'Identified the issue, provided a new form link.', 'Resolved', 'Sending new form link to customer.', 'Agent sent a new form link to the customer to complete the X registration.', 21.0, 24.0, 'Concerned', 'Neutral', 80),
    ('69_2', 69, 'Inquiry about Resolution Time', 90, 'Resolution time', 22.0, 26.0, 'X Registration', NULL, 'Provided the estimated time for the X registration to be set up.', 'Resolved', 'N/A', 'Agent informed that it will take 3 days after form submission.', 25.0, 28.0, 'Neutral', 'Neutral', 90),
    ('70_1', 70, 'Inquiry about Credit Card Statement', 95, 'Credit card statement not received', 0.0, 9.0, 'Credit Card', 'Statement not received', 'Agent updated email and resent statement.', 'Resolved', 'Statement resent.', 'Statement resent to updated email.', 16.0, 23.0, 'Concern', 'Neutral', 90),
    ('71_1', 71, 'Billing Dispute', 95, 'Unknown charge on account', 0.0, 9.0, 'Bank Account', 'Unknown charge', 'Agent initiated refund request.', 'Resolved', 'Refund request submitted.', 'Refund will be processed in 5 days.', 28.0, 31.0, 'Inquiry', 'Neutral', 85),
    ('72_1', 72, 'Credit Card Issue', 95, 'International transaction issue', 0.0, 9.0, 'Credit Card', 'International transaction blocked', 'Agent activated international transactions.', 'Resolved', 'International transactions activated.', 'Transactions will be activated in 24 hours.', 23.0, 28.0, 'Concerned', 'Neutral', 80),
    ('73_1', 73, 'Prepayment Charge Inquiry', 95, 'Prepayment charges', 0.0, 9.0, 'Home Loan', 'Prepayment charge details', 'Agent checked the prepayment charges associated with the customer\'s loan account.', 'Unresolved', 'N/A', 'Agent informed the customer about the 2% prepayment charge.', 15.0, 21.0, 'Neutral', 'Neutral', 60),
    ('73_2', 73, 'Prepayment Charge Waiver Request', 90, 'Waiver request', 20.0, 23.0, 'Home Loan', 'Request for waiver', 'Agent agreed to submit a request for a waiver of the prepayment charges.', 'Pending with Callback', 'Agent will submit a waiver request.', 'Agent will provide an update to the customer in 3-5 days regarding the waiver request.', 22.0, 29.0, 'Hopeful', 'Neutral', 70),
    ('74_1', 74, 'Technical Support', 95, 'Mobile banking app login issue', 0.0, 9.0, 'Mobile Banking App', 'Login issue', 'Agent reset registration and sent login link.', 'Resolved', 'Registration reset.', 'Login link sent via SMS.', 22.0, 26.0, 'Frustration', 'Neutral', 85),
    ('75_1', 75, 'Check Fixed Deposit Maturity Details', 95, 'FD maturity details', 0.0, 8.0, 'Fixed Deposit', 'Maturity details not found', 'Agent checked the FD details and confirmed the maturity amount was credited.', 'Resolved', 'Send account statement to customer.', 'Agent confirmed that the maturity amount including interest was credited.', 14.0, 25.0, 'Neutral', 'Neutral', 90),
    ('75_2', 75, 'Inquire about Interest', 90, 'Interest included', 19.0, 22.0, 'Fixed Deposit', NULL, 'Agent confirmed interest was included.', 'Resolved', 'N/A', 'Agent confirmed interest was included in the credited amount.', 21.0, 25.0, 'Neutral', 'Neutral', 95),
    ('76_1', 76, 'Account Information Update', 95, 'Incorrect name on account', 0.0, 8.0, 'Bank Account', 'Incorrect name', 'The agent apologized, collected the correct account number and name, and initiated the update process.', 'Resolved', 'Agent initiated account update process and sent KYC link.', 'Agent initiated the process to update the customer\'s name.', 17.0, 23.0, 'Neutral', 'Neutral', 85),
    ('76_2', 76, 'KYC Document Submission Inquiry', 90, 'Online KYC submission', 22.0, 25.0, 'Bank Account', NULL, 'The agent confirmed that the customer could submit the documents online and offered to send a link.', 'Resolved', 'N/A', 'Agent confirmed online submission and offered to send a link.', 24.0, 27.0, 'Neutral', 'Positive', 90),
    ('77_1', 77, 'EMI Conversion Issue', 95, 'EMI conversion issue', 0.0, 9.0, 'Credit Card', 'EMI conversion issue', 'Agent initiated EMI conversion.', 'Resolved', 'EMI conversion initiated.', 'EMI conversion for 12 months initiated.', 22.0, 25.0, 'Neutral', 'Neutral', 85),
    ('78_1', 78, 'Report Loan Statement Error', 95, 'Loan statement error', 0.0, 17.0, 'Loan', 'Statement error', 'Agent submitted correction request.', 'Pending with Callback', 'Correction request submitted.', 'Update in 3-5 days.', 19.0, 27.0, 'Inquiry', 'Neutral', 75),
    ('79_1', 79, 'NEFT Transfer Issue', 95, 'Failed NEFT transfer', 0.0, 18.0, 'NEFT', 'Transfer failed', 'Agent identified incorrect IFSC code.', 'Pending with Callback', 'Reinitiate transfer with correct IFSC.', 'Customer needs to provide correct IFSC code.', 26.0, 29.0, 'Neutral', 'Neutral', 70),
    ('80_1', 80, 'Cashback Inquiry', 95, 'Missing cashback on credit card', 0.0, 9.0, 'Credit Card', 'Cashback missing', 'Agent checked offer details.', 'Resolved', 'N/A', 'Cashback will be credited in next billing cycle.', 27.0, 33.0, 'Neutral', 'Neutral', 80),
    ('81_1', 81, 'Balance Inquiry/Update', 95, 'Balance not updated', 0.0, 9.0, 'Bank Account', 'Deposit not reflected', 'Checked the deposit status and informed the customer about the processing time.', 'Resolved', 'N/A', 'Informed customer that the deposit is processing and will be updated within 24 hours.', 18.0, 23.0, 'Concerned', 'Neutral', 85),
    ('81_2', 81, 'Confirmation Request', 90, 'Confirmation for deposit', 23.0, 26.0, 'Bank Account', NULL, 'Confirmed that the customer will receive an SMS and email confirmation.', 'Resolved', 'N/A', 'Agent confirmed that customer will receive confirmation via SMS and email.', 25.0, 28.0, 'Inquisitive', 'Positive', 90),
    ('82_1', 82, 'PIN Generation Issue', 95, 'Credit card PIN generation failure', 0.0, 8.0, 'Credit Card', 'PIN generation failed', 'Agent reinitiated PIN generation process.', 'Resolved', 'PIN generation reinitiated.', 'PIN will be sent via SMS in 48 hours.', 25.0, 29.0, 'Neutral', 'Neutral', 80),
    ('83_1', 83, 'Loan Approval Status Inquiry', 95, 'Loan approval status', 0.0, 8.0, 'Loan', 'Approval status', 'Checked the loan application status and informed the customer.', 'Resolved', 'N/A', 'Agent informed the customer about the loan approval status.', 14.0, 20.0, 'Neutral', 'Neutral', 90),
    ('83_2', 83, 'Inquire about Document Submission', 90, 'Document submission inquiry', 18.0, 22.0, 'Loan', NULL, 'Agent offered to send an online link for document submission.', 'Resolved', 'Send online link.', 'Agent will send an online link for document submission.', 20.0, 24.0, 'Neutral', 'Positive', 95),
    ('84_1', 84, 'Debit Card Issue', 95, 'CVV error on debit card', 0.0, 5.0, 'Debit Card', 'CVV error', 'Agent initiated a new card issuance.', 'Resolved', 'New card issuance request.', 'A new debit card will be issued and delivered in 5-7 days.', 23.0, 29.0, 'Concern', 'Neutral', 85),
    ('85_1', 85, 'Account Information Update', 95, 'Incorrect name linked to account', 0.0, 9.0, 'Account', 'Name discrepancy', 'Agent initiated name update request.', 'Pending with Callback', 'Name update request initiated.', 'Name update will take 3-5 working days.', 21.0, 28.0, 'Neutral', 'Neutral', 75),
    ('86_1', 86, 'Reward Program Change', 95, 'Credit card reward program change', 0.0, 9.0, 'Credit Card', 'Reward program change', 'Agent raised a request to revert to the old program.', 'Pending with Callback', 'Request to revert to old reward program.', 'Agent will provide an update after the review.', 26.0, 31.0, 'Dissatisfaction', 'Negative', 50),
    ('87_1', 87, 'Failed Transaction', 95, 'Failed RTGS transfer', 0.0, 8.0, 'RTGS', 'Transfer failed', 'Agent identified incorrect beneficiary details.', 'Unresolved', 'N/A', 'Customer needs to retry with correct details.', 16.0, 21.0, 'Concern', 'Neutral', 60),
    ('88_1', 88, 'Loan Insurance Coverage Inquiry', 95, 'Loan insurance coverage', 0.0, 9.0, 'Loan', 'Insurance coverage', 'Agent provided details about loan insurance coverage.', 'Resolved', 'N/A', 'Agent explained the loan insurance coverage details.', 18.0, 24.0, 'Neutral', 'Neutral', 80),
    ('89_1', 89, 'Debit Card Limit Inquiry', 95, 'Decrease in debit card limit', 0.0, 9.0, 'Debit Card', 'Limit decrease', 'Agent explained the reason for the limit decrease.', 'Resolved', 'N/A', 'Agent informed the customer about the updated limit policy.', 20.0, 26.0, 'Neutral', 'Neutral', 70),
    ('90_1', 90, 'Mobile Number Update', 95, 'Update mobile number', 0.0, 9.0, 'Account', 'Mobile number update', 'Agent updated the customer\'s mobile number.', 'Resolved', 'Mobile number updated.', 'Mobile number updated successfully.', 18.0, 24.0, 'Neutral', 'Neutral', 85),
    ('91_1', 91, 'Direct Debit Setup Issue', 95, 'Direct debit setup issue', 0.0, 9.0, 'Bank Account', 'Direct debit setup', 'Agent resolved the direct debit setup issue.', 'Resolved', 'Direct debit setup resolved.', 'Direct debit setup issue resolved successfully.', 20.0, 26.0, 'Neutral', 'Neutral', 80),
    ('92_1', 92, 'Statement Issue', 95, 'Credit card statement not delivered', 0.0, 8.0, 'Credit Card', 'Statement not received', 'Agent emailed the digital statement to the customer.', 'Resolved', 'N/A', 'Agent emailed the digital statement to the customer.', 21.0, 23.0, 'Concern', 'Neutral', 80),
    ('92_2', 92, 'Inquiry about Future Statements', 90, 'Future physical statements', 21.0, 26.0, 'Credit Card', NULL, 'Agent assured the customer that they would receive physical statements in the future.', 'Resolved', 'N/A', 'Agent confirmed future physical statements.', 24.0, 28.0, 'Inquiry', 'Positive', 90),
    ('93_1', 93, 'Loan Processing Fee Refund', 95, 'Delay in loan processing fee refund', 0.0, 9.0, 'Loan', 'Processing fee refund', 'Agent initiated a follow-up for the refund.', 'Pending with Callback', 'Follow-up initiated.', 'Refund will be processed in 3-5 days.', 20.0, 26.0, 'Concern', 'Neutral', 75),
    ('94_1', 94, 'Report Unauthorized Transaction', 95, 'Unauthorized transaction on debit card', 0.0, 8.0, 'Debit Card', 'Unauthorized transaction', 'Agent initiated fraud claim and refund process.', 'Resolved', 'Fraud claim initiated.', 'Refund will be processed in 7-10 working days.', 20.0, 28.0, 'Concern', 'Negative', 80),
    ('94_2', 94, 'Inquire Refund Time', 90, 'Refund time', 23.0, 27.0, 'Debit Card', NULL, 'Provided the estimated refund time frame.', 'Resolved', 'N/A', 'Refund will be processed in 7-10 working days.', 25.0, 28.0, 'Neutral', 'Neutral', 90),
    ('95_1', 95, 'Renewal Issue', 95, 'FB auto-renewal failed', 0.0, 9.0, 'FB', 'Auto renewal failed', 'Identified the issue, manually renewed the customer\'s FB.', 'Resolved', 'Manual renewal of FB.', 'Agent manually renewed the FB.', 17.0, 19.0, 'Concerned', 'Neutral', 85),
    ('95_2', 95, 'Rate Confirmation', 90, 'Interest rate confirmation', 17.0, 23.0, 'FB', NULL, 'Confirmed that the interest rate would remain the same.', 'Resolved', 'N/A', 'Confirmed the interest rate will remain same.', 20.0, 23.0, 'Inquiry', 'Neutral', 90),
    ('96_1', 96, 'Email Address Update', 95, 'Incorrect email address', 0.0, 9.0, 'Account', 'Email update', 'Agent updated the customer\'s email address.', 'Resolved', 'Email address updated.', 'Email address updated successfully.', 18.0, 24.0, 'Neutral', 'Neutral', 85),
    ('97_1', 97, 'Billing Cycle Reversion', 95, 'Revert credit card billing cycle', 0.0, 9.0, 'Credit Card', 'Billing cycle reversion', 'Agent submitted a request to revert the billing cycle.', 'Pending with Callback', 'Request submitted.', 'Billing cycle reversion will take 3-5 days.', 20.0, 26.0, 'Neutral', 'Neutral', 80),
    ('98_1', 98, 'Request Loan Repayment Schedule', 95, 'Loan repayment schedule', 0.0, 8.0, 'Loan', 'Repayment schedule not received', 'Agent checked and confirmed the schedule was sent to the registered email and offered to resend it.', 'Resolved', 'Resending the repayment schedule via email.', 'Agent resent the loan repayment schedule to the customer\'s registered email address.', 16.0, 18.0, 'Neutral', 'Neutral', 85),
    ('98_2', 98, 'Request for Physical Copy', 90, 'Physical copy of schedule', 18.0, 21.0, 'Loan', NULL, 'Agent informed the customer that they can obtain a physical copy from the branch.', 'Resolved', 'N/A', 'Customer can get the physical copy from the branch.', 20.0, 23.0, 'Neutral', 'Neutral', 90),
    ('99_1', 99, 'Debit Card Limit Issue', 95, 'Unable to set online limit', 0.0, 9.0, 'Debit Card', 'Online limit issue', 'Agent checked the customer\'s details and informed about the KYC update requirement and promised to send a link.', 'Pending with Callback', 'Send KYC update link to customer.', 'Agent informed the customer that KYC update is required and will send a link for the same.', 16.0, 22.0, 'Neutral', 'Neutral', 70),
    ('99_2', 99, 'Inquiry about Resolution Time', 90, 'Resolution time for limit', 21.0, 24.0, 'Debit Card', NULL, 'Agent informed the customer about the time required for the limit to be set after KYC submission.', 'Resolved', 'N/A', 'Agent informed that it will take two working days after KYC submission.', 23.0, 27.0, 'Neutral', 'Neutral', 80),
    ('100_1', 100, 'Fund Credit Inquiry', 95, 'Mutual fund amount not credited', 0.0, 9.0, 'Mutual Funds', 'Amount not credited', 'Agent checked the account and informed the customer that the amount is in processing and will be credited in three working days.', 'Resolved', 'N/A', 'The agent confirmed that the amount is in processing and will be credited within three working days.', 17.0, 21.0, 'Concerned', 'Neutral', 85),
    ('100_2', 100, 'Confirmation Request', 90, 'Confirmation for credit', 21.0, 26.0, 'Mutual Funds', NULL, 'Agent confirmed that the customer will receive confirmation via SMS and email.', 'Resolved', 'N/A', 'The agent confirmed that the customer will receive confirmation via SMS and email.', 23.0, 26.0, 'Inquisitive', 'Positive', 90);


SELECT * FROM Intents;

