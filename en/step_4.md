## Randomly choosing an insult


--- task ---

You can find out how many lines there are in the file by printing the `len()` which is the **length**. Add this code, then click **Run** to see the answer:

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
  print(len(lines))

--- /code ---

--- /task ---

--- task ---

Try changing the `line_number` variable to another number between 0 and one less than the length. Press **Run** and you should see a different insult printed.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3
---
with open("insults.csv", "r") as f:
  lines = f.readlines()
  line_number = 32
  words = lines[line_number].split(",")
  print(f"Thou {words[0]} {words[1]} {words[2]}")


--- /code ---

--- /task ---