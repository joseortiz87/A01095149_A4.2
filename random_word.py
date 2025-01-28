import random

# Predefined list of words
word_list = [
    "apple", "banana", "cherry", "date", "hello", "word"
]

def generate_file_with_data(filename, num_words=1000, words_per_line=10):
    """Generates a file with random words from the predefined list."""
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(num_words):
            word = random.choice(word_list)
            file.write(word + " ")
            if (i + 1) % words_per_line == 0:
                file.write("\n")
    print(f"{filename} with {num_words} random words.")

# Generate the file
generate_file_with_data('fileWithData3.txt', 1000, 10)

