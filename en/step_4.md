## Randomly choosing an insult


--- task ---

You can find out how many lines there are in the file by printing the `len()` which is the **length**. Add this code:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  print(lines[0])
  print(len(lines))

--- /code ---

--- /task ---

--- task ---

Try changing the number inside the [square brackets] to another number between 0 and one less than the length. Press **Run** and you should see a different line printed.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  print(lines[32])
  print(len(lines))

--- /code ---

--- /task ---