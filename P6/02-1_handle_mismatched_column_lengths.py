
# Create lists to store our word types in
adjectives = []
verbs = []
nouns = []

with open("words.csv", "r") as f:
    for line in f:
        words = line.split(",")

        # Split the columns apart and put them into 3 lists
        if words[0]:
            adjectives.append(words[0])

        if words[1]:
            nouns.append(words[1])

        if words[2].strip():
            verbs.append(words[2].strip() )

print(adjectives)
print(nouns)
# Notice the noun list will include newline chars!
# Add 'strip' to its append operation
print(verbs)