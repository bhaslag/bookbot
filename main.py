from stats import count_words
from stats import count_letters
from stats import descending

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    txt = get_book_text('books/frankenstein.txt')

    # num_words = count_words(txt)
    # print(f"{num_words} words found in the document")

    num_letters = count_letters(txt)
    word_count = count_words(txt)
    sorted_letters = descending(num_letters)
    # print(num_letters)
    # print(word_count)
    print(sorted_letters)

main()