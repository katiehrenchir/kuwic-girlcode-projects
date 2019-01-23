
# Create lists to store our word types in
adj1 = []
adj2 = []
noun = []

with open("words.csv", "r") as f:
    for line in f:
        individual_words = line.split(",")

        # Split the columns apart and put them into 3 lists
        adj1.append(individual_words[0])
        adj2.append(individual_words[1])
        noun.append(individual_words[2])

print(adj1)
print(adj2)
#Notice the noun list will include newline chars
print(noun)