prompt_definition = """A model that receives an instruction from the user to show certain information from a postgres database in colloquial english. 
Followed by information on table definitions under TABLE_DEFINITIONS formatted as the output of this function:

    def get_table_definitions_for_prompt(self):
        table_names = self.get_all_table_names()
        return "\n".join([self.get_table_definition(table) for table in table_names])

With the instruction and the table definitions formatted like so:

<user instruction>

TABLE_DEFINITIONS

<output of function> """

response_definition = """

It is the model's job to then respond with an SQL query that will be run to fetch the requested data with an output that follows this formatting:

$insert an explanation of the sql query as raw text here
            ---------
$insert sql query exclusively as raw text here
"""

prompt = f'{prompt_definition}{response_definition}'