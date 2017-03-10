def charFrequencies(string):
    chars = set(string)
    d = {}
    for k in chars:
        d[k] = string.count(k)
    return d


print(charFrequencies("This is an example."))
