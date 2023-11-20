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
    #parse prompt param using arg parse

    with PostgresDatabase() as db:
        db.connect_with_url(DB_URL)
        

    #call PostgresDatabase.get_table_definition_for_prompt() to get tables in prompt ready form

    # create two blank calls to llm.add_cap_ref() that update our current prompt passed in from the command line

    # call llm.prompt to get a prompt_response variable

    # parse sql response from prompt_response using SQL_QUERY_DELIMITER '------------'

    # call PostgresDatabase.run_sql() with the parsed sql

    print(result)


if __name__ == '__main__':
    main()