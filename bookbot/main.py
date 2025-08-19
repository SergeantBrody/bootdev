from stats import count_words, count_characters, report
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    
    content = get_book_text(path_to_file=path_to_book)
    print(f"Analyzing book found at {path_to_book}...")
    sum_of_words = count_words(content)
    print("----------- Word Count ----------")
    print(f"Found {sum_of_words} total words")
    characters_sum = count_characters(content)
    report(characters_sum)
def get_book_text(path_to_file):
 with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents



main()
