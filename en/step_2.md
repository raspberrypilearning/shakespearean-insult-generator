## Open and read from a file

--- task ---

Open the <a href="https://editor.raspberrypi.org/en/projects/shakespearean-insult-starter" target="_blank">starter project</a>.

--- /task ---

--- task ---

Add some code to open the file (`insults.csv`) in read mode (`"r"` means *read mode*), read the full contents, and output the result:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
with open("insults.csv", "r") as f:
        line = f.readline()
        print(contents)

--- /code ---

--- /task ---



So far, we're able to read the insults from the file in the order they were written, but we can't do much with them. You may have noticed that the different columns forming the parts of the insult were different types of word. The first two columns (A and B) contain **adjectives** (describing words) and the final column (C) contains **nouns**, mostly in this case referring to a 'thing' the person resembles. If we could split them up, we could make insults of the form "Thou [List A] [List B] [List C]" by choosing a random word from each list. An example might be "Thou impertinent rump-fed miscreant".

