"""
This code compute descriptive statistics
(mean, median, mode, variance, and standard deviation) from a file containing numbers.
"""
import sys
import time


def read_file(file_path):
    """
    Reads the file and returns a list of numbers. Handles invalid data.
    
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
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid number, skipped: {line.strip()}")  # Req 3
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return numbers


def compute_mean(numbers):
    """
    Calculates the mean
    
    Args:
        numbers (list): The list of numbers.
    
    Returns:
        float: The mean of the numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def compute_median(numbers):
    """
    Calculates the median
    
    Args:
        numbers (list): The list of numbers.
    
    Returns:
        float: The median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def compute_mode(numbers):
    """
    Calculates the mode
    
    Args:
        numbers (list): The list of numbers.
    
    Returns:
        float or list: The mode of the numbers or a list of modes if multiple.
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    if len(modes) == 1:
        return modes[0]
    return modes  # Return multiple modes if they exist


def compute_variance(numbers, mean):
    """
    Calculates the variance
    
    Args:
        numbers (list): The list of numbers.
        mean (float): The mean of the numbers.
    
    Returns:
        float: The variance of the numbers.
    """
    variance_sum = 0
    for num in numbers:
        variance_sum += (num - mean) ** 2
    return variance_sum / len(numbers)


def compute_std_deviation(variance):
    """
    Calculates the standard deviation
    
    Args:
        variance (float): The variance of the numbers.
    
    Returns:
        float: The standard deviation of the numbers.
    """
    return variance ** 0.5


def write_results_to_file(results, elapsed_time):
    """
    Writes the computed statistics to StatisticsResults.txt file
    
    Args:
        results (dict): A dictionary containing computed statistics.
        elapsed_time (float): The time taken to compute the statistics.
    """
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")


def main():
    """
    Main function to read file & compute statistics,
    and write the results to a file.
    """
    # Req 5: Ensure the program is invoked with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <fileWithData.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Start timing
        start_time = time.time()

        # Read numbers from the input file
        numbers = read_file(file_path)

        # Req 3: Handle invalid or empty data
        if not numbers:
            print("No valid numbers found in the file.")
            sys.exit(1)

        # Compute descriptive statistics
        mean = compute_mean(numbers)
        median = compute_median(numbers)
        mode = compute_mode(numbers)
        variance = compute_variance(numbers, mean)
        std_deviation = compute_std_deviation(variance)

        # Collect results
        results = {
            "Mean": mean,
            "Median": median,
            "Mode": mode,
            "Variance": variance,
            "Standard Deviation": std_deviation
        }

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Req 7: Print results to console
        for key, value in results.items():
            print(f"{key}: {value}")
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
