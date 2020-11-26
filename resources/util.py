#! Python3
# util.py

def write(text):
    # from time import sleep    # Uncomment for slow printing
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02)            # Uncomment for slow printing
    # print()