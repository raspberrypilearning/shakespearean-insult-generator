import random

with open("insults.csv", "r") as f:
    lines = f.readlines()
    line_number = random.randint(0, len(lines) - 1)
    words = lines[line_number].split(",")
    print(f"Thou {words[0]} {words[1]} {words[2]}")
