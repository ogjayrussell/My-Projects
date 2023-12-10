from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os
import dotenv
import argparse
import autogen
from db import PostgresDatabase
import llm

dotenv.load_dotenv()

DB_URL = os.environ.get('DB_URL')
key = os.environ.get('OPENAI_API_KEY')

POSTGRES_TABLE_DEFINITIONS_CAP_REF = "TABLE_DEFINITIONS"
TABLE_RESPONSE_FORMAT_CAP_REF = "TABLE_RESPONSE_FORMAT"

SQL_DELIMITER = "---------"

def main():
    #to accept command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", help="Prompt for the OpenAI API")
    args = parser.parse_args()

    #initial prompt
    prompt = args.prompt
    
    
    with PostgresDatabase() as db:
        
        # print('prompt v1', prompt)

        #connection to the db
        db.connect_with_url(DB_URL)

        table_definitions = db.get_table_definitions_for_prompt()
        

        #second iteration of prompt that will extract table definitions (structure)
        prompt = llm.add_cap_ref(
            args.prompt,
            f"Use these {POSTGRES_TABLE_DEFINITIONS_CAP_REF} to satisfy the database query.",
            POSTGRES_TABLE_DEFINITIONS_CAP_REF,
            table_definitions)
        
        # print('prompt v2', prompt)
        
        #third iteration of prompt that uses the table definitions and devises an SQL query that will answer the user request. Delimiter to make it easy to extract the SQL query.
        prompt = llm.add_cap_ref(
            prompt,
            f"Respond in the format found under {TABLE_RESPONSE_FORMAT_CAP_REF}. Write the relevant information within <>, don't include the <> symbols", 
            TABLE_RESPONSE_FORMAT_CAP_REF,
            f"""<explanation of the sql query>
            {SQL_DELIMITER}\n<sql query exclusively as raw text>
            """
            )
        
        print('MODIFIED PROMPT:', prompt)


        #Now that there is a well structured prompt with table definitions as context + understanding of what format is required, the llm will now attempt to respond with SQL terminology 
        prompt_response = llm.prompt(prompt)

        print('prompt_response',prompt_response)

        #taking the SQL query from the response
        sql_query = prompt_response.split(SQL_DELIMITER)[1].strip()

        print('sql_query', sql_query)

        #running the SQL query against the database
        result = db.run_sql(sql_query)

        print('-------- POSTGRES DATA ANALYTICS AI AGENT RESPONSE ---------')

        print(result)


if __name__ == '__main__':
    main()
 