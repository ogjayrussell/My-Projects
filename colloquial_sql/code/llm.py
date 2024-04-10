"""
This module contains the functions that interact with the OpenAI API.
"""

import sys
from dotenv import load_dotenv
import os
from typing import Any, Dict
from openai import OpenAI
import requests

# load .env file
load_dotenv()

# get openai api key
openai_api_key = os.environ.get("OPENAI_API_KEY")


# ------------------ content generators ------------------


def prompt(prompt):
    """
    Sends a prompt to OpenAI's GPT-4 model and returns the generated text response.

    """
    # Your OpenAI API key (replace with your actual API key)
    
    # API request headers
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json',
    }
    
    # API request payload
    data = {
        'model': 'gpt-4',
        'messages':[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
            
        ],
        'temperature': 0.3,  # Adjust temperature as needed for creativity
        'max_tokens': 500,  # Adjust the max token limit as needed
    }
    
    # Making the API call
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        # Adjusting the parsing logic for chat responses
        # Assuming you want the last message in the conversation, which is the AI's response
        if response_json.get('choices') and response_json['choices'][0].get('message'):
            generated_text = response_json['choices'][0]['message']['content']
            return generated_text.strip()
        else:
            return "No response text found."
    else:
        return f"Failed to call OpenAI API: {response.status_code}, {response.text}"


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