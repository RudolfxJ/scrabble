import requests
import json
import os
from typing import Dict, Optional
from requests.exceptions import RequestException

def fetch_sort_and_save_words_by_length(
        url: str, 
        sorted_file_name: Optional[str] = "words_sorted.json"
    ) -> Optional[Dict[str, Dict[int, list]]]:
    """
    Fetches a list of words from a specified URL, sorts them by their first letter and length,
    and then saves the sorted list to a JSON file.

    Args:
        url (str): The URL from which to fetch the words.
        sorted_file_name (Optional[str]): The name of the file to save the sorted words. Defaults to "words_sorted.json".

    Returns:
        Optional[Dict[str, Dict[int, list]]]: A dictionary containing sorted words if successful, None otherwise.

    Raises:
        RequestException: If an error occurs during the network request.
        IOError: If an error occurs while writing to the file.
        json.JSONDecodeError: If an existing JSON file is not in a valid JSON format.
    """
    
    # Check if the file exists and is JSON readable
    if sorted_file_name and os.path.isfile(sorted_file_name):
        try:
            with open(sorted_file_name, 'r') as file:
                sorted_words = json.load(file)
            return sorted_words
        except json.JSONDecodeError:
            print("The file is not in a valid JSON format, and will be re-created.")
        except FileNotFoundError:
            print("The file was not found and will be created.")


    print("Fetching, sorting and caching words...")

    # Fetch words from the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        words = response.text.splitlines()  # Robust splitting of lines
    except RequestException as e:
        print(f"Error fetching words from URL: {e}")
        raise

    # Sort words
    sorted_words: Dict[str, Dict[int, list]] = {}
    for word in words:
        if not word:
            continue
        word_length = len(word)
        first_letter = word[0].lower()  # Normalize to lowercase

        if first_letter not in sorted_words:
            sorted_words[first_letter] = {}
        if word_length not in sorted_words[first_letter]:
            sorted_words[first_letter][word_length] = []

        sorted_words[first_letter][word_length].append(word)

    # Save to JSON file for caching
    try:
        with open(sorted_file_name, "w") as file:
            json.dump(sorted_words, file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise

    return sorted_words
