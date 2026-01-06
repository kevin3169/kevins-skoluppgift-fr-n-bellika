import time

def slowprint(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()
