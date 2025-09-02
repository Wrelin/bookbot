import stats as s

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    frankenstein_path = 'books/frankenstein.txt'
    frankenstein_text = get_book_text(frankenstein_path)

    char_count = s.get_characters_count(frankenstein_text)

    print(char_count)


if __name__ == "__main__":
    main()
