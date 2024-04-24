import random
from typing import Dict, List, Optional
from scrabble.utility import fetch_sort_and_save_words_by_length as get_sorted_words

def start_scrabble(input_string: str) -> str:
    """
    Modifies a given string by replacing each word with a random word that starts with 
    the same letter and has the same length. If no matching word is found, the original 
    word is retained.

    Parameters:
        input_string (str): The string to be modified.

    Returns:
        str: The modified string with randomly replaced words.
    """
    sorted_words: Dict[str, Dict[str, List[str]]] = get_sorted_words(
        "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
        "words_sorted.json",
    )
    
    if not sorted_words:
        raise RuntimeError("Failed to fetch or sort words.")
    
    output_string: List[str] = []
    
    for word in input_string.split():
        first_letter: str = word[0].lower()
        word_length: str = str(len(word))
        replacement_word: str = word  # Default to the original word
        
        available_words_by_length: Optional[List[str]] = sorted_words.get(first_letter, {}).get(word_length, [])
        
        if available_words_by_length:
            replacement_word = random.choice(available_words_by_length)
        
        output_string.append(replacement_word)
    
    return " ".join(output_string)