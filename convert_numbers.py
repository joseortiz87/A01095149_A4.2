"""
This script reads numbers from a file, converts them to binary and hexadecimal.
The results will be saved to file named 'ConvertionResults.txt'.
"""

import sys
import time

def read_file(file_path):
    """
    Reads the file and returns a list of valid numbers. Handles invalid data.
    
    Args:
        file_path (str): The path to the file containing numbers.
    
    Returns:
        list: A list of valid numbers from the file.
    """
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid number, skipped: {line.strip()}")  # Req 3
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return numbers


def convert_to_binary(number):
    """
    Converts a number to binary.
    
    Args:
        number (int): The number to be converted
    
    Returns:
        string: Binary representation of the number.
    """
    binary = ""
    if number == 0:
        return "0"
    is_negative = number < 0
    number = abs(number)
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    if is_negative:
        binary = "-" + binary
    return binary


def convert_to_hexadecimal(number):
    """
    Converts a number to hexadecimal.
    
    Args:
        number (int): The number to be converted
    
    Returns:
        string: Hexadecimal representation of the number.
    """
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    if number == 0:
        return "0"
    is_negative = number < 0
    number = abs(number)

    while number > 0:
        remainder = number % 16
        # Ensure remainder is a valid index and hex_digits is a string
        if isinstance(remainder, int) and isinstance(hex_digits, str):
            hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16
    if is_negative:
        hexadecimal = "-" + hexadecimal
    return hexadecimal


def write_results_to_file(results, elapsed_time):
    """
    Writes the computed statistics to ConvertionResults.txt file.
    
    Args:
        results (dict): A dictionary containing conversions.
        elapsed_time (float): The time taken to compute the conversions.
    """
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
        for number, conversions in results.items():
            file.write(f"Number: {number}, Binary: {conversions['binary']}, "
                       f"Hexadecimal: {conversions['hexadecimal']}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")


def main():
    """
    Main function of the script. It processes the input file, converts the numbers
    to binary and hexadecimal, and writes the results to both the console and a file.
    """
    # Ensure the program is invoked with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <fileWithData.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Start timing
        start_time = time.time()

        # Read only numbers from the input file
        numbers = read_file(file_path)

        # Handle cases where no valid numbers were found
        if not numbers:
            print("No valid numbers found in the file.")
            sys.exit(1)

        # Convert numbers to binary and hexadecimal
        results = {}
        for number in numbers:
            results[number] = {
                "binary": convert_to_binary(number),
                "hexadecimal": convert_to_hexadecimal(number),
            }

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Print results to console
        for number, conversions in results.items():
            print(f"Number: {number}, "
                  f"Binary: {conversions['binary']}, "
                  f"Hexadecimal: {conversions['hexadecimal']}")
        print(f"Time Elapsed: {elapsed_time:.2f} seconds")

        # Write results to file
        write_results_to_file(results, elapsed_time)

    # Req3. Error handlers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
        sys.exit(1)
    except ValueError as value_error:
        print(f"Error processing data: {value_error}")
        sys.exit(1)
    except OSError as os_error:
        print(f"File system error: {os_error}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Execution interrupted by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
