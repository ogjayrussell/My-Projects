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

def main(prompt):
    #to accept command line arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--prompt", help="Prompt for the OpenAI API")
    # args = parser.parse_args()

    #initial prompt
    # prompt = args.prompt

    prompts_list = pd.read_csv('./data/prompts.csv')
    
    prompt = prompt
    
    
    with PostgresDatabase() as db:
        
        # print('prompt v1', prompt)

        #connection to the db
        db.connect_with_url(DB_URL)

        table_definitions = db.get_table_definitions_for_prompt()
    

        #visibility on table definitions (structure)
        prompt = llm.add_cap_ref(
            prompt, #args.prompt
            f"Use these {POSTGRES_TABLE_DEFINITIONS_CAP_REF} to satisfy the database query:",
            POSTGRES_TABLE_DEFINITIONS_CAP_REF,
            table_definitions)
        
        # print('prompt v2', prompt)
        
        #outlining required formatting to extract the SQL query.
        prompt = llm.add_cap_ref(
            prompt,
            f"Respond in the format found under {TABLE_RESPONSE_FORMAT_CAP_REF}. Insert the relevant information within <>, don't include the <> symbols, keep the {SQL_DELIMITER}.", 
            TABLE_RESPONSE_FORMAT_CAP_REF,
            f"""<insert an explanation of the sql query as raw text here>
            {SQL_DELIMITER}\n<insert sql query exclusively as raw text here>
            """
            )
        
        print('1. MODIFIED_PROMPT:', prompt)


        #devise an SQL query that will answer the user request with visibility on TABLE_DEFINITIONS as context. Answer with advised formatting. Delimiter to make it easy to extract the SQL query.
        prompt_response = llm.prompt(prompt)

        print('2. PROMPT_RESPONSE:',prompt_response)

        #extracting the SQL query from the response
        sql_query = prompt_response.split(SQL_DELIMITER)[1].strip()

        print('3. RUN_SQL_QUERY:', sql_query)

        #running the SQL query against the database
        result = db.run_sql(sql_query)

        print('-------- POSTGRES AI AGENT RESPONSE ---------')

        print(result)


if __name__ == '__main__':
    main()
 