def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def word_count(book_content):
    words = book_content.split()
    num_words = len(words)
    return num_words

def character_count(filepath):
    characters = get_book_text(filepath)
    char_count = {}
    low_char = characters.lower()
    for char in low_char:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count


def sorted_part(filepath):
    sorted_part = []
    dict = character_count(filepath)
    for key in dict:
        sorted_part.append({"char": key, "num" : dict[key]})
    def sort_on(dict):
        return dict["num"]
    sorted_part.sort(reverse=True, key = sort_on)
    return sorted_part
