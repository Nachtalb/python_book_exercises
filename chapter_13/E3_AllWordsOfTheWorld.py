def read_document(path):
    try:
        f = open(path)
        text = f.read()
        f.close()
        return text
    except:
        print("There was an error")


def generate_list(text):
    text = text.replace("\n", " ")
    wordlist = []
    for word in text.split(" "):
        if wordlist == [] or not any(word in words for words in wordlist):
            wordlist += [(word, text.count(word))]
    return sorted(wordlist)


text = read_document("./text.txt")
wordlist = generate_list(text)

for idx, tuple in enumerate(wordlist):
    print(tuple, end=" ")
    if (idx + 1) % 10 == 0:
        print("\n", end="")
