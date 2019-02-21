import random

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

def create_sentence():
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    word3 = random.choice(verbs)

    return word1 + word2 + word3
 
# Remove print statements for the lists - those were just for testing!

# Call our new create_sentence function
sentence = create_sentence()
print(sentence)