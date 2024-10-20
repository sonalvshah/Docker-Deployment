import os
import re
from collections import Counter
import socket

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return ""

def split_words(text, handle_contractions=False):
    if handle_contractions:
        text = re.sub(r"[’']", " ", text)
    words = re.findall(r'\b\w+\b', text.lower(), re.UNICODE)
    return words

def count_words(words):
    return len(words)

def top_n_words(words, n=3):
    word_counts = Counter(words)
    return word_counts.most_common(n)

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print(f"Error getting IP address: {e}")
        return "Unknown"

def main():
    try:
        # Paths to the text files
        file1_path = '/home/data/IF.txt'
        file2_path = '/home/data/AlwaysRememberUsThisWay.txt'

        # Read files
        text1 = read_file(file1_path)
        text2 = read_file(file2_path)

        # Process files
        words1 = split_words(text1)
        words2 = split_words(text2, handle_contractions=True)

        # Count total words in each file
        total_words_file1 = count_words(words1)
        total_words_file2 = count_words(words2)

        # Calculate grand total
        grand_total_words = total_words_file1 + total_words_file2

        # Get top 3 frequent words in each file
        top3_file1 = top_n_words(words1, 3)
        top3_file2 = top_n_words(words2, 3)

        # Get IP address
        ip_address = get_ip_address()

        # Prepare the result string
        result = (
            f"Total words in IF.txt: {total_words_file1}\n"
            f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n"
            f"Grand total of words: {grand_total_words}\n\n"
            f"Top 3 words in IF.txt:\n"
        )

        for word, count in top3_file1:
            result += f"- {word}: {count}\n"

        result += "\nTop 3 words in AlwaysRememberUsThisWay.txt:\n"

        for word, count in top3_file2:
            result += f"- {word}: {count}\n"

        result += f"\nIP Address of the machine running the container: {ip_address}\n"

        # Write results to result.txt
        output_dir = '/home/data/output'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'result.txt')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)

        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()