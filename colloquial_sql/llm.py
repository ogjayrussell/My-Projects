"""
This module contains the functions that interact with the OpenAI API.
"""

import sys
from dotenv import load_dotenv
import os
from typing import Any, Dict
import openai

# load .env file
load_dotenv()

# get openai api key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# ------------------ helpers ------------------


def safe_get(data, dot_chained_keys):
    """
    {'a': {'b': [{'c': 1}]}}
    safe_get(data, 'a.b.0.c') -> 1
    """
    keys = dot_chained_keys.split(".")
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data


def response_parser(response: Dict[str, Any]):
    return safe_get(response, "choices.0.message.content")


def make_client(gpt_api_key: str):
    return openai


# ------------------ content generators ------------------


def prompt(prompt: str, model: str = "gpt-4") -> str:
    # validate the openai api key - if it's not valid, raise an error
    if not openai.api_key:
        sys.exit(
            """

ERORR: OpenAI API key not found. Please export your key to OPENAI_API_KEY

Example bash command:
    export OPENAI_API_KEY=<your openai apikey>
            """
        )

    openai_client = openai

    response = openai_client.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response_parser(response)

def add_cap_ref(prompt: str, prompt_suffix: str, cap_ref: str, cap_ref_content: str) -> str:
    """
    Attaches a capitalized reference to the prompt.
    
    Example
    prompt = 'Refactor this code.'
    prompt_suffix = 'Make it more readable using this EXAMPLE.'
    cap_ref = 'EXAMPLE'
    cap_ref_content = 'def foo():\n    return True'
    
    returns 'Refactor this code. Make it more readable using this EXAMPLE.\n\nEXAMPLE\n\ndef foo():\n    return True'
    """
    new_prompt = f"""{prompt} {prompt_suffix}\n\n{cap_ref}\n\n{cap_ref_content}"""
    return new_prompt

#find out what the end of AWS code needs to look like. How does the model feed into this app?
#Function needs an input of the propmt from console, then request the AWS model through the API.

def mistral(prompt):
    import boto3
    import json

    # Initialize a SageMaker runtime client with the AWS region
    client = boto3.client('runtime.sagemaker', region_name='your-region')

    # Specify your SageMaker endpoint name
    endpoint_name = 'your-endpoint-name'

    # Prepare your input data as a JSON string (format may vary based on the model)
    data = {
        "instances": [
            # Your input data here
        ]
    }
    payload = json.dumps(data)

    # Make the inference request
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',  # Adjust based on the expected content type of your model
        Body=payload
    )

    # Parse the response
    result = json.loads(response['Body'].read().decode())

    print(result)