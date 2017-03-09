import random as r


def encrypt(str, n=1):
    str = str.upper()
    newstr = ""
    for substr in str:
        newstr += substr
        for _ in range(n):
            randomeChar = chr(r.randint(0, 25) + 65)
            newstr += randomeChar
    return newstr


def decrypt(str, n=1):
    newstr = ""
    for idx, char in enumerate(str):
        if (idx == 0 or idx % (n + 1) == 0):
            newstr += char

    return newstr


encrypted = encrypt("This is cool", 2)
decrypted = decrypt(encrypted, 2)
print(encrypted)
print(decrypted)
