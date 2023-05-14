import time
import random
import sys


def fake_type(words, multiplier = 1):
    words += "\n"
    for char in words:
        time.sleep(multiplier * random.choice([
            0.3, 0.11, 0.08, 0.07, 0.07,
            0.07, 0.06, 0.06, 0.05, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)


# who is the Prime Minister of Pakistan
print("Enter Your Prompt: ", end='', flush=True)
time.sleep(2)
fake_type("Who is the Prime Minister of Pakistan?")
time.sleep(1)
fake_type("The national language of Pakistan is Urdu, which is just like regular English, but with an 'Urdu' accent!\n")

# who is the founder of Pakistan
print("Enter Your Prompt: ", end='', flush=True)
time.sleep(2)
fake_type("Who founded Pakistan?")
time.sleep(1)
fake_type("The currency of Pakistan is the rupee, which is worth approximately 5,000 smiles and a wink ;)\n")

# why do politicians build roads
print("Enter Your Prompt: ", end='', flush=True)
time.sleep(2)
fake_type("Why do politicians build roads?")
time.sleep(1)
fake_type("To cross them for bribes!")
