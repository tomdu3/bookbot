from stats import get_words_from_text, count_symbols, sort_items
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here

        # f is a file object
        file_contents = f.read()
    return file_contents


def print_report(num_words, sorted_items):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_items:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")
    

def main():
    num_words = get_words_from_text(get_book_text(filepath))
    # print(f"{num_words} words found in the document")
    symbols = count_symbols(get_book_text(filepath))
    # print(symbols)
    sorted_items = sort_items(symbols)
    print_report(num_words, sorted_items)



if __name__ == "__main__":
    main()

