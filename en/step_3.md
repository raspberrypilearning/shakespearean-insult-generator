## Lists in Python

Each line contains three words - the first two are **adjectives** (describing words) and the last is a **noun** (a thing). 

--- task ---

Change your code so that it only prints the first line in the list. The numbering of the lines always **starts from zero** so the first line in the list is `lines[0]`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3-4
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  line_number = 0
  print(lines[line_number])

--- /code ---


--- /task ---

--- task ---

Click **Run** and you should see `artless,base-court,apple-john` in the output area.

--- /task ---


--- task ---

Delete the `print` statement. Add some new code to split the line up whereever there is a comma, and save it as a list of `words`


--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  line_number = 0
  words = lines[line_number].split(",")

--- /code ---

--- /task ---


--- task ---

Finally, add a new print statement to print out `Thou`, followed by each word in the list of words in turn. Click **Run** to see the result.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  line_number = 0
  words = lines[line_number].split(",")
  print(f"Thou {words[0]} {words[1]} {words[2]}")

--- /code ---

--- /task ---



