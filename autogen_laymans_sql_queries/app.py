from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os
import dotenv
import argparse
import autogen
from db import PostgresDatabase


engine = create_engine('postgresql://postgres:r2foru@localhost:5432/patient_data')
DB_URL = 'postgresql://postgres:r2foru@localhost:5432/patient_data'
OPEN_AI_KEY = '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'

def main():

    #parse prompt param using arg parse

    with PostgresDatabase() as db:
        db.connect_with_url(DB_URL)

        patients = db.get_all('patients')

        print(patients)

    # call db_manager.get_table_definition_for_prompt() to get tables in prompt ready form

    # create two blank calls to llm.add_cap_ref() that update our current prompt passed in from the commanc line

    # call llm.prompt to get a prompt_response variable

    # parse sql response from prompt_response using SQL_QUERY_DELIMITER '------------'

    # call db_manager.run_sql() with the parsed sql

pass







if __name__ == '__main__':
    main()