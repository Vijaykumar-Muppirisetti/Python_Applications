"""
app.py

This script provides a simple dictionary lookup functionality using a JSON file as the data source.
It allows users to enter a word and get its definition(s). If the word is not found, it suggests
similar words using string matching.

Author: Vijay Kumar M
Date: 19-August-2024
"""

import json # imports the "json" module for handling JSON data
from difflib import get_close_matches # imports the "get_close_matches" module for finding similar words

# Load the dictionary data from a JSON file
data = json.load(open("data.json"))

def definition_of(word):
    """Function to find the definition of a given word.
    
    Args:
    word (str): The word to look up in the dictionary.

    Returns:
    list or str: The definition(s) of the word if found, or an error message if not found.
    """
    # Check if the word is in the dictionary (case-sensitive)
    if word in data:
        return data[word]
    # Check if the word is in the dictionary (case-insensitive)
    elif word.lower() in data:
        return data[word.lower()]
    else:
        # If the word is not found, suggest a close match
        close_matches = get_close_matches(word, data.keys())
        if len(close_matches) > 0:
            # Ask the user if they meant the suggested word
            flag = (input(f"Did you mean \'{close_matches[0]}\' instead? Enter Y if yes, or N if no: "))
            if flag == 'Y':
                return data[close_matches[0]]
        # If no close match is found, return an error message    
        return "The word does not exist, Please double check it."

# Main program 

# Get user input
word = input("Enter a word: ")

# Look up the word and get the result
result = definition_of(word)

# Display result(s)
if isinstance(result, list):
    for index, definition in enumerate(result, 1):
        print(f"{index}. {definition}")
else:
    print(result)