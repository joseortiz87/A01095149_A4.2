"""
This script reads words from a file and calculate the frequency of each unique word.
The results will be saved to file named 'WordCountResults.txt'.
"""

import sys
import time

def read_file(file_path):
    """
    Reads the file and returns a list of words. Handles invalid data.
    
    Args:
        file_path (str): The path to the file containing words.
    
    Returns:
        list: A list of words from the file.
    """
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Split the line into words by spaces and add them to the list
                    words.extend(line.strip().split())
                except UnicodeDecodeError as e:
                    print(f"Error processing line: {line.strip()}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return words


def count_word_frequencies(words):
    """
    Counts the frequency of each distinct word in the list.
    
    Args:
        words (list): A list of words.
    
    Returns:
        dict: A dictionary with words as keys and frequencies as value.
    """
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase to count words case-insensitively
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def write_results_to_file(word_count, elapsed_time):
    """
    Writes the word frequencies to WordCountResults.txt.
    
    Args:
        word_count (dict): A dictionary with word frequencies.
        elapsed_time (float): The time taken to compute the word frequencies.
    """
    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")
        file.write(f"\nTime Elapsed: {elapsed_time:.2f} seconds\n")


def main():
    """
    Main function of the script. It processes the input file, identify words
    frequency and writes the results to both the console and a file.
    """
    # Ensure the program is invoked with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Start timing
        start_time = time.time()

        # Read the file and process words
        words = read_file(file_path)

        # Handle cases where no words were found
        if not words:
            print("No valid words found in the file.")
            sys.exit(1)

        # Count word frequencies
        word_count = count_word_frequencies(words)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Print results to console
        for word, count in word_count.items():
            print(f"{word}: {count}")
        print(f"\nTime Elapsed: {elapsed_time:.2f} seconds")

        # Write results to file
        write_results_to_file(word_count, elapsed_time)

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
