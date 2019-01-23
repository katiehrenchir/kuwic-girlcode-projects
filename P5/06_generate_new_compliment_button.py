from guizero import App, Text, PushButton
import random

def compliment_me():
    word1 = random.choice(adj1)
    word2 = random.choice(adj2)
    word3 = random.choice(noun)

    compilment = "Oh, Katie, you " + word1 + ", " + word2+ ", " + word3 + "!\n"
    return compilment

def generate_new_compliment():
    new_compliment = compliment_me()
    message.value = new_compliment

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


app = App("Katie's Leslie Knope Compliment Generator", width=500, height=100)

# Things to show on our GUI
message = Text(app, compliment_me())
button = PushButton(app, generate_new_compliment, text="Compliment me again!")

app.display()
