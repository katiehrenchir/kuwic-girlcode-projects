
# Create lists to store our word types in
adjectives = []
verbs = []
nouns = []

with open("words.csv", "r") as f:
    for line in f:
        words = line.split(",")

        # Split the columns apart and put them into 3 lists
        adjectives.append(words[0])
        verbs.append(words[1])
        nouns.append(words[2].strip() )

print(adjectives)
print(verbs)
# Notice the noun list will include newline chars!
# Add 'strip' to its append operation
print(nouns)