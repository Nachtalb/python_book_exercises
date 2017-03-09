def konkat(*substrings):
    fullstr = ""
    for substring in substrings:
        fullstr += substring
    print(fullstr)


konkat("this ", "is ", "konkat", "!")
