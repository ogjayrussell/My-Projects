# UNFINISHED - Translating natural, colloquial language into SQL queries to fetch data



### Stack:
- Postgres sql database
- AWS
- HuggingFace
- Large Language Models
- API

# Function of the agent:
1. recieve initial prompt from user - colloqiual
2. modify the initial prompt to include information on:
- the database's table definitions
- the expected output with guidance on formatting
3. run the modified prompt against the llm
4. extract the llm's suggested SQL query from it's response
5. query the database

## TO DO:
1. Host local LLM on AWS
2. Fine tune the base model
3. Replace OpenAI API with 

# Example: "show me the patients with a gmail"

## Output
MODIFIED PROMPT: show me the patients with a gmail Use these TABLE_DEFINITIONS to satisfy the database query.

TABLE_DEFINITIONS

CREATE TABLE patients (
    id integer DEFAULT nextval('patients_patient_id_seq'::regclass) NOT NULL,
    email character varying NOT NULL,
    phone character varying,
    first_name character varying,
    last_name character varying
); 

Respond in this format TABLE_RESPONSE_FORMAT

TABLE_RESPONSE_FORMAT

<explanation of the sql query>
            ---------
<sql query exclusively as raw text>
            
prompt_response The following SQL query allows us to retrieve all records from the 'patients' table where the email is a Gmail address, meaning it ends with '@gmail.com'.

---------
SELECT * FROM patients WHERE email LIKE '%@gmail.com'<br>
sql_query SELECT * FROM patients WHERE email LIKE '%@gmail.com'
-------- POSTGRES DATA ANALYTICS AI AGENT RESPONSE ---------<br>
[(1, 'john.doe@gmail.com', '1234567890', 'John', 'Doe'), (4, 'emily.davis@gmail.com', '4567890123', 'Emily', 'Davis'), (7, 'james.taylor@gmail.com', '7890123456', 'James', 'Taylor'), (8, 'elizabeth.johnson@gmail.com', '8901234567', 'Elizabeth', 'Johnson'), (10, 'susan.clark@gmail.com', '1234567890', 'Susan', 'Clark'), (13, 'richard.thomas@gmail.com', '4567890123', 'Richard', 'Thomas'), (16, 'mary.martin@gmail.com', '7890123456', 'Mary', 'Martin'), (19, 'andrew.lee@gmail.com', '1234567890', 'Andrew', 'Lee')]