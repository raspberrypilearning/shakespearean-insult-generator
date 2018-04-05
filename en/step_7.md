## Lists in Python

- We will add some code to read the file line by line and split each column into a separate list. Try planning this yourself in pseudocode before looking at our solution below:

  ```
  CREATE list_a, list_b, list_c as BLANK LISTS
  OPEN insults.csv in read mode
    FOR each line in the file, READ INTO variable line
      words = SPLIT line EVERY "," INTO A LIST
      APPEND first word IN words TO list_a
      APPEND second word IN words TO list_b
      APPEND third word IN words TO list_c
    END WHILE
  PRINT list_a
  ```

  The most unfamiliar part of this code is probably `words = SPLIT line EVERY "," INTO A LIST`. Here we will use Python's built-in `split()` function to split up the line of text wherever there's a comma, and save the results as a list called `words`.

- Here is the corresponding Python code for the code we planned above. Once again, you could have a go at translating your pseudocode into Python before you look at the solution below. Delete your existing code and replace it with the new code:

--- collapse ---

---
title: Show the code
---

  ```python
  list_a = []
  list_b = []
  list_c = []

  with open("insults.csv", "r") as f:
      for line in f:
          words = line.split(",")
          list_a.append(words[0])
          list_b.append(words[1])
          list_c.append(words[2])

  print( list_a )


  ```

--- /collapse ---

- Save and run your program by pressing F5. You should find that the program outputs a list of all of the words you put in column A.

  ![Print list A](images/output-a.png)

- Change your code to print out and check lists B and C too. You should spot a problem.

When you output `list_c` to check it, you will notice something strange - an extra `\n` character has been added to the end of each of the words:

  ![Print list C](images/output-c.png)

  The `\n` character is not a surprise when you find out that it means "new line". It's there because in our original CSV file, each group of three insult words was stored on a *new line*! However, we don't want to display it in our insult, so we can add some code to get rid of it.

- Find this line in your code:

  ```python
  list_c.append(words[2])
  ```

  ...and add `.strip()` on the end of the word you're appending, to automatically strip out the `\n` and any other **whitespace characters**.

  ```python
  list_c.append( words[2].strip() )
  ```

