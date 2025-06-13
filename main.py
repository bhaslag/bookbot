from stats import count_words
from stats import count_letters
from stats import descending

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    import sys
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    txt = get_book_text(sys.argv[1])

    num_letters = count_letters(txt)
    word_count = count_words(txt)
    sorted_letters = descending(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for dictionary in sorted_letters:
        if dictionary['char'].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")

main()