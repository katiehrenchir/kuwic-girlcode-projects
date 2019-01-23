from guizero import App, Text, PushButton
import random

def compliment_me():
    word1 = random.choice(adj1)
    word2 = random.choice(adj2)
    word3 = random.choice(noun)

    compilment = "Oh, Katie, you " + word1 + ", " + word2+ ", " + word3 + "!"
    return compilment
    #print(compilment)

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


app = App("Katie's Leslie Knope Compliment Generator")

# Things to show on our GUI
message = Text(app, compliment_me() )

app.display()
