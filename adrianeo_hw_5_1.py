"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-17-2024
Homework Problem # 5_1
Description: This program counts the number of vowels and consonants in a
text file
and returns the count of each in a dictionary. The text is converted to
uppercase before processing.
"""

import os


def vc_counter(filename):
    """
    Counts the vowels and consonants in the specified file.

    Args:
    filename (str): The name of the file to be read.

    Returns:
    dict: A dictionary with the count of vowels and consonants.
    """
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    try:
        with open(filename, 'r') as file:
            text = file.read().upper()
            for letter in text:
                if letter in vowels:
                    vowel_count += 1
                elif letter in consonants:
                    consonant_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    
    return {"vowels": vowel_count, "consonants": consonant_count}


# Example usage
current_path = "/Users/adrianeortiz/Local_Stuffs/CS_521/adrianeo_hw_5"
filename = "TEST_FILE.txt"
full_path = os.path.join(current_path, filename)
print(vc_counter(full_path))
