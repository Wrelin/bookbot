def get_words_count(text):
    words = text.split()
    filtered_words = [w for w in words if w]
    return len(filtered_words)


def get_characters_count(text):
    characters = list(text)
    lower_characters = [c.lower() for c in characters]
    result = {}

    for c in lower_characters:
        if c not in result:
            result[c] = 0
        result[c] += 1

    return result

