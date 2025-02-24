from stats import get_num_words
from stats import characterCounter, get_book_text

import sys

def main():
    try:
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        get_num_words(path)
        print("--------- Character Count -------")
        characterCounter(path)
    except:
        print("invalid token")
        sys.exit(1)
main()

