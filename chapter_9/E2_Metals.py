list = [('Gold', 0.1234), ('Silver', 7.89), ('Iron', 34.9979)]

for metal in list:
    print(metal[0], metal[1], end=" // " if metal != list[-1] else "\n")

print()
for metal in list:
    print(metal[0], metal[1], sep="\t")

print()
for metal in list:
    print(metal[0]+":", format(metal[1], '8.2f'), sep="\t")
