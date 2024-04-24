import requests
import json

def fetch_sort_and_save_words_by_length(url):
    """
    Fetches a list of words from a specified URL, sorts them by their length,
    and then saves the sorted list to a JSON file.

    The function retrieves words from a predefined URL where words are stored
    in plain text format, one per line. It then categorizes these words into
    a dictionary where the keys are word lengths and the values are lists of
    words of that length. Finally, it serializes this dictionary into a JSON
    file named 'words_sorted.json'.

    Side Effects:
        - Makes a network request to the specified URL.
        - Writes to a file named 'words_sorted.json' in the current directory.

    Returns:
        None

    Raises:
        requests.exceptions.RequestException: If an error occurs during the network request.
        IOError: If an error occurs while writing to the file.
    """

    words_url = url
    
    try:
        response = requests.get(words_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        words = response.text.replace('\r\n', '\n').split('\n') # Fix for both windows and linux
    except requests.exceptions.RequestException as e:
        print(f"Error fetching words from URL: {e}")
        return

    sorted_words = {}
    for word in words:
        word_length = len(word)
        if word_length in sorted_words:
            sorted_words[word_length].append(word)
        else:
            sorted_words[word_length] = [word]

    try:
        with open("words_sorted.json", "w") as f:
            json.dump(sorted_words, f, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
