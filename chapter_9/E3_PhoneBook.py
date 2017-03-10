import pickle as p


def createPhoneBook():
    global phoneBook
    try:
        f = open("phonebook.dat", "rb")
        phoneBook = p.load(f)
        f.close()
    except:
        phoneBook = {}
    return phoneBook


def search():
    global phoneBook
    print("SEARCH")
    name = input("Who are you searching for? ")
    print(name + ":", phoneBook.get(name, "does not exist"))


def addNumber():
    global phoneBook
    print("ADD NEW NUMBER")
    name = input("What is the new contacts name? ")
    while name != "":
        if name in list(phoneBook.keys()):
            print("Name already exists")
        else:
            tel = input("And his/her phone number? ")
            phoneBook[name] = tel
            print(name, "added.\n")
        name = input("What is the new contacts name? ")


def listAllNumbers():
    global phoneBook

    print("LIST ALL CONTACTS")
    for name in phoneBook:
        print(name + "\t" + phoneBook.get(name, "error"))


def close():
    global phoneBook
    f = open("phonebook.dat", "wb")
    p.dump(phoneBook, f)
    f.close()


def menu():
    userinput = " "
    while userinput != "":
        print("(S)earch for contact by full name", "(A)dd new contact", "(L)ist all contacts", "(C)lose the phone book",
              sep="\n")
        userinput = input(": ")

        if userinput in ["S", "s"]: search()
        elif userinput in ["A", "a"]: addNumber()
        elif userinput in ["L", "l"]: listAllNumbers()
        elif userinput in ["C", "c"] or userinput is "":
            userinput = ""
            close()
        print()


# Main Part
phoneBook = {}
createPhoneBook()
menu()
