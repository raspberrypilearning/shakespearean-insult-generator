## Lists in Python

Each line contains three words - the first two are **adjectives** (describing words) and the last is a **noun** (a thing). 

--- task ---

Change your code so that it only prints the *first** line in the list. The numbering of the lines always **starts from zero** so the first line in the list is `lines[0]`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  print(lines[0])

--- /code ---


--- /task ---

--- task ---

Click **Run** and you should see `artless,base-court,apple-john` in the output area.

--- /task ---

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


