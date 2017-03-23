def find_words_by_length(text, length):
    """
    >>> find_words_by_length("This is a wonderful small text with some words in it.", 4)
    ['This', 'text', 'with', 'some']
    
    >>> find_words_by_length(4, 4)
    You you used an int instead of a string!
    
    :param text: 
    :param length: 
    :return: 
    """
    try:
        results = []
        for word in text.split(" "):
            if len(word) == length:
                results += [word]
        return results
    except:
        print("You you used an int instead of a string!")

def search_words(text, length):
    clean_text = text.join([c for c in text if c not in ".;:,!?-"])
    wlist = set(clean_text.split())
    l = [word for word in wlist if len(word) == length]
    return l

print(find_words_by_length("""This is a wonderful small text with some words in it.""", 4))
print(find_words_by_length(4, 4))
print(search_words("""This is a wonderful small text with some words in it.""", 4))

import doctest as d
d.testmod()
