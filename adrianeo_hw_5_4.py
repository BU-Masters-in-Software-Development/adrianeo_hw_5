"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-17-2024
Homework Problem # 5_4
Description: This program reads a text file, processes it to remove
punctuation,
converts words to lowercase, and identifies words that appear exactly twice.
"""


def list_to_twice_words(filename):
    """
    Finds words that occur exactly twice in a text file.

    Args:
    filename (str): The path to the text file.

    Returns:
    list: A list of words that occur exactly twice.
    """
    with open(filename, 'r') as file:
        text = file.read()
        
        # Remove punctuation, convert to lowercase, and split into words
        words = [word.strip(".,!?:;\"'").lower() for word in text.split()]
        word_count = {}
        
        # Count occurrences of each word
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Find words that occur exactly twice
        return [word for word, count in word_count.items() if count == 2]


# Example usage
# test file: myFile0.json
filename = input("Enter the filename: ")
print(list_to_twice_words(filename))
