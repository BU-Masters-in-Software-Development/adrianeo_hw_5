"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-17-2024
Homework Problem # 5_2
Description: This program includes functions for analyzing the frequency of
letters
in a string, identifying the most common letter, and printing a histogram of
letter frequencies.
"""

from collections import Counter


def letter_frequency(input_string):
    """
    Counts the frequency of each letter in a string, ignoring case.

    Args:
    input_string (str): The input string.

    Returns:
    Counter: A collection that counts each letter's occurrences.
    """
    return Counter(
        letter.lower() for letter in input_string if letter.isalpha()
        )


def most_common_letter(input_string):
    """
    Finds the most common letter in a string.

    Args:
    input_string (str): The input string.

    Returns:
    str: The most common letter.
    """
    letter_freq = letter_frequency(input_string)
    return max(letter_freq, key = letter_freq.get)


def letter_histogram(input_string):
    """
    Prints a histogram of letter frequencies in a string.

    Args:
    input_string (str): The input string.
    """
    letter_freq = letter_frequency(input_string)
    for letter in sorted(letter_freq):
        print(f"{letter}: {'*' * letter_freq[letter]}")


# Example usage
text = "example string"
print("Letter Frequency:", letter_frequency(text))
print("Most Common Letter:", most_common_letter(text))
print("Letter Histogram:")
letter_histogram(text)
