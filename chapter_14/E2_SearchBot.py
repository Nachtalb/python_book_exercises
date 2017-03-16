import os

print("Search for a word in files, by recursive path search")
searchfor = input("Find: ")
path = input("Path to search in: ")

print("Searchresult")
print("------------")

print("You searched for {} in \"{}\".".format(searchfor, path))

file_amount = 0
not_file_amount = 0
found = 0
for dic in os.walk(path):
    for file in dic[2]:
        filepath = os.path.join(dic[0], file)
        try:
            f = open(filepath)
            text = f.read()
            amount = text.count(searchfor)
            found += amount
            file_amount += 1
            print("{amount:>8} times in {path}".format(amount=amount, path=os.path.relpath(filepath)))
        except:
            not_file_amount += 1
            print("WARNING: Could not read file: " + filepath)

print("I searched in {} files and found {} occurrences.".format(file_amount, found))
print("{} files could not be searched in".format(not_file_amount))
