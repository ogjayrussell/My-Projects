from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os
import dotenv
import argparse
import autogen
from db import PostgresDatabase

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

    prompt = llm.add_cap_ref(args.prompt, "", "TABLE_DEFINITIONS", table_definitions)
    prompt = llm.add_cap_ref(prompt, "", "EXAMPLE", "SELECT * FROM patients")

    prompt_response = llm.prompt(prompt)

    sql_query = prompt_response.split('------------')[1].strip()

    with PostgresDatabase() as db:
        db.connect_with_url(DB_URL)
        result = db.run_sql(sql_query)

    print(result)







if __name__ == '__main__':
    main()
