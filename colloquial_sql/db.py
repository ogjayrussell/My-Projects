import psycopg2
from psycopg2 import sql

class PostgresDatabase:
    #connection with postgres server
    def __init__(self):
        self.conn = None
        self.cur = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def connect_with_url(self, url):
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor()

    #insert or update a row in a table if id is present in _dict
    # def upsert(self, table_name, _dict):
    #     columns = _dict.keys()
    #     values = _dict.values()
        
    #     upsert_stmt = sql.SQL(
    #         "INSERT INTO {} ({}) VALUES ({}) ON CONFLICT (id) DO UPDATE SET {}"
    #     ).format(
    #         sql.Identifier(table_name),
    #         sql.SQL(', ').join(map(sql.Identifier, columns)),
    #         sql.SQL(', ').join(sql.Placeholder() * len(values)),
    #         sql.SQL(', ').join(
    #             [sql.SQL("{} = EXCLUDED.{}").format(sql.Identifier(col), sql.Identifier(col)) for col in columns])
    #     )
        
    #     self.cur.execute(upsert_stmt, values)
    #     self.conn.commit()

    #delete a row in table by id
    # def delete(self, table_name, _id):
    #     delete_stmt = sql.SQL("DELETE FROM {} WHERE id = %s").format(sql.Identifier(table_name))
    #     self.cur.execute(delete_stmt, (_id,))
    #     self.conn.commit()

    # #get a row in a table by id
    # def get(self, table_name, _id):
    #     select_stmt = sql.SQL("SELECT * FROM {} WHERE id = %s").format(sql.Identifier(table_name))
    #     self.cur.execute(select_stmt, (_id,))
    #     return self.cur.fetchone()

    # #get all rows in a table
    # def get_all(self, table_name):
    #     select_stmt = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    #     self.cur.execute(select_stmt)
    #     return self.cur.fetchall()

    #run a sql statement made by llm
    def run_sql(self, sql_stmt):
        self.cur.execute(sql_stmt)
        return self.cur.fetchall()

    #get a table definition in a 'create table' format directly from postgres as a string. Passed to the llm to show what the tables look like
    def get_table_definition(self, table_name):
        # Query to get column details
        select_stmt = sql.SQL("""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
        """)
        self.cur.execute(select_stmt, (table_name,))
        columns_info = self.cur.fetchall()

        # Start the CREATE TABLE statement
        create_table_stmt = f"CREATE TABLE {table_name} (\n"

        # Define columns with data types and default values
        column_definitions = []
        for column in columns_info:
            col_def = f"    {column[0]} {column[1]}"
            if column[3] is not None:  # If there is a default value
                col_def += f" DEFAULT {column[3]}"
            if column[2] == 'NO':  # If the column is not nullable
                col_def += " NOT NULL"
            column_definitions.append(col_def)

        # Join all column definitions into the statement
        create_table_stmt += ",\n".join(column_definitions)
        create_table_stmt += "\n);"

        return create_table_stmt

    #list table names in postgres database. to get the table names to call get_table_definition
    def get_all_table_names(self):
        select_stmt = "SELECT tablename FROM pg_tables WHERE schemaname = 'public'"
        self.cur.execute(select_stmt)
        return [row[0] for row in self.cur.fetchall()]

    #combine get_table_definitions() and get_all_table_names() to get a list of table definitions in a 'create table' format for all tables in database as a string that can be used for our llm prompt
    def get_table_definitions_for_prompt(self):
        table_names = self.get_all_table_names()
        return "\n".join([self.get_table_definition(table) for table in table_names])