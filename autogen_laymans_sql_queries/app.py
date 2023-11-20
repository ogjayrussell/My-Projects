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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Prompt for the OpenAI API")
    args = parser.parse_args()
    
    with PostgresDatabase() as db:
        
        db.connect_with_url(DB_URL)

        table_definitions = db.get_table_definitions_for_prompt()

        print('prompt v1', prompt)

        prompt = llm.add_cap_ref(
            args.prompt,
            f"Use these {TABLE_DEFINITIONS} to satisfy the database query.",
            TABLE_DEFINITIONS, 
            table_definitions)
        
        print('prompt v2', prompt)
        
        prompt = llm.add_cap_ref(
            prompt, 
            "Please provide the SQL query:", 
            "SQL_QUERY", 
            "")
        
        print('prompt v3', prompt)

        prompt_response = llm.prompt(prompt)

        sql_query = prompt_response.split('------------')[1].strip()

        result = db.run_sql(sql_query)

    print(result)


if __name__ == '__main__':
    main()
 