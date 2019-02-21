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
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)

    # Don't forget to add spaces!
    sentence = "I love my " + adj + " " + noun + " so much I could " + verb + "!"
    return sentence
 
sentence = create_sentence()
print(sentence)