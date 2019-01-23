
# Create lists to store our word types in
adj1 = []
adj2 = []
noun = []

with open("words.csv", "r") as f:
    for line in f:
        individual_words = line.split(",")

        # Split the columns apart and put them into lists
        adj1.append(individual_words[0])
        adj2.append(individual_words[1])

        # 'Strip' removes whitespace characters from our string
        noun.append(individual_words[2].strip())

print(adj1)
print(adj2)
print(noun)