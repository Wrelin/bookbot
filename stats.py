def get_words_count(text):
    words = text.split()
    filtered_words = [w for w in words if w]
    return len(filtered_words)


def get_characters_count(text):
    characters = list(text)
    lower_characters = [c.lower() for c in characters]
    result = {}

    for c in lower_characters:
        if not c.isalpha():
            continue

        if c not in result:
            result[c] = 0
        result[c] += 1

    return result

def get_letters_list(counts_dict):
    result = []
    for letter in counts_dict:
        dct = {"char": letter, "num": counts_dict[letter]}
        result.append(dct)

    result.sort(reverse=True, key=lambda items: items["num"])
    return result
