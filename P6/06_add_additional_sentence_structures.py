import random
import tweepy
# Note for GitHub viewers - our credentials file has not been uploaded
# You will need to create your own Twitter dev account
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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
    which_structure = random.randint(1,2)

    if which_structure == 1:
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)

        # Don't forget to add spaces!
        sentence = "I love my " + adj + " " + noun + " so much I could " + verb + "!"
        return sentence

    elif which_structure == 2:
        verb = random.choice(verbs)
        adj = random.choice(adjectives)
        noun = random.choice(nouns)

        # Don't forget to add spaces!
        sentence = "I love to " + verb + ", and so does my " + adj + " " + noun + "!"
        return sentence
 
# Keep in mind Twitter's 280 character limit per tweet
sentence = create_sentence() + " -Katie"

# Print the sentence to the console for our benefit
print(sentence)

# Use tweepy to update our status!
api.update_status(sentence)