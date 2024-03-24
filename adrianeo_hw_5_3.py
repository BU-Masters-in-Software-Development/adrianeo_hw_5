"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-17-2024
Homework Problem # 5_3
Description: This program prompts the user for four numbers, performs a
calculation, and handles potential errors.
"""


def calculate_from_input():
    """
    Prompts user for four numbers separated by commas, performs a
    calculation, and handles errors.
    
    Returns:
    float or str: The result of the calculation or an error message.
    """
    while True:
        try:
            input_str = input("Enter four numbers separated by a comma: ")
            numbers = input_str.split(",")
            
            if len(numbers) != 4:
                raise ValueError(
                    "Please enter exactly four numbers, separated by commas."
                    )
            
            numbers = [float(num.strip()) for num in numbers]
            return sum(numbers) / len(numbers)
        except ValueError as ve:
            print(ve)
        except ZeroDivisionError:
            return "Division by zero error."


# Example usage
result = calculate_from_input()
print("Result:", result)
