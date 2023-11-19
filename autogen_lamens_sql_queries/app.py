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
    with PostgresDatabase() as db:
        db.connect_with_url(DB_URL)

        patients = db.get_all('patients')

        print(patients)


# build the gpt_configuration object

# build the function map

# create our terminate msg function

# create a set of agents with specific roles
# admin user proxy agent - takes in the prompt and manages the group chat
# data engineer agent - generates the sql query
# sr data analyst agent - run the sql query and generate the response
# product manager - validate the response to make sure it's correct

# create a group chat and initiate the chat.



