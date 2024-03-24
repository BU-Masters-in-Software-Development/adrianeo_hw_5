"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-17-2024
Homework Problem # 5_5
Description: This program calculates the factorial of a number using both
recursive and non-recursive methods.
"""


def factorial_recursive(target_number):
    """
    Calculates the factorial of a number recursively.

    Args:
    target_number (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    if target_number == 0:
        return 1
    else:
        return target_number * factorial_recursive(target_number - 1)


def factorial_non_recursive(target_number):
    """
    Calculates the factorial of a number non-recursively.

    Args:
    target_number (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    factorial_result = 1
    for factor in range(2, target_number + 1):
        factorial_result *= factor
    return factorial_result


# Example usage
number_to_factorial = int(input("Enter a number: "))
recursive_result = factorial_recursive(number_to_factorial)
non_recursive_result = factorial_non_recursive(number_to_factorial)

print(f"Recursive Factorial: {recursive_result:,}")
print(f"Non-Recursive Factorial: {non_recursive_result:,}")
