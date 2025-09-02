import sys
import stats as s

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frankenstein_path = sys.argv[1]
    frankenstein_text = get_book_text(frankenstein_path)

    words_count = s.get_words_count(frankenstein_text)
    char_count = s.get_characters_count(frankenstein_text)
    letters = s.get_letters_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for letter in letters:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
