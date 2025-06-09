## Randomly choosing an insult


--- task ---

You can find out how many lines there are in the file by printing the `len()` which is the **length**. Add this code, then click **Run** to see the answer. Delete this code when you know how many lines there are.

--- code ---
---
language: python line_numbers: true line_number_start: 1
line_highlights: 4
---
with open("insults.csv", "r") as f: lines = f.readlines() line_number = 0 print(len(lines))

--- /code ---

--- /task ---

--- task ---

Try changing the `line_number` variable to another number between 0 and one less than the length.

--- code ---
---
language: python line_numbers: true line_number_start: 1
line_highlights: 3
---
with open("insults.csv", "r") as f: lines = f.readlines() line_number = 32 words = lines[line_number].split(",") print(f"Thou {words[0]} {words[1]} {words[2]}")


--- /code ---

--- /task ---

--- task ---

Click **Run** and you should see a different insult printed.

--- /task ---

--- task ---

On the first line of your code, add some code to import the `random` library:

--- code ---
---
language: python line_numbers: true line_number_start: 1
line_highlights: 1
---
import random with open("insults.csv", "r") as f: --- /code ---

--- /task ---

--- task ---

Now use the `randint` function from the `random` library in your code to choose a random line from the file to generate the insult. The line chosen will be a random line between 0 and the number of lines available minus one.

--- code ---
---
language: python line_numbers: true line_number_start: 1
line_highlights: 4
---
import random with open("insults.csv", "r") as f: lines = f.readlines() line_number = random.randint(0, len(lines)-1) words = lines[line_number].split(",") print(f"Thou {words[0]} {words[1]} {words[2]}")


--- /code ---

--- /task ---

The random choice needs to be between 0 and the length minus one because the line numbering starts at 0. For example, in the list `['a', 'b', 'c']`, the length of the list is 3 because it contains 3 items, but the last item in the list is numberered `2` because the numbering system starts with 0.