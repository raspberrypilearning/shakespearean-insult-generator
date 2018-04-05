## Open and read from a file

- Open up **Python 3 IDLE**.

- Click `File` > `New File` and save the file as `shakespeare.py`.

- Add the following code to open the file (`insults.csv`) in read mode (`"r"` means *read mode*), read the full contents, and output the result:

    ```python
    with open("insults.csv", "r") as f:
        contents = f.read()
        print(contents)
    ```

- What's the difference between the current line of code...

  ```Python
  contents = f.read()
  ```

  ...and this line of code?

  ```Python
  contents = f.readline()
  ```

  Change the code and see if you can work out the difference betweeen `read()` and `readline()`.

- So far, we're able to read the insults from the file in the order they were written, but we can't do much with them. You may have noticed that the different columns forming the parts of the insult were different types of word. The first two columns (A and B) contain **adjectives** (describing words) and the final column (C) contains **nouns**, mostly in this case referring to a 'thing' the person resembles. If we could split them up, we could make insults of the form "Thou [List A] [List B] [List C]" by choosing a random word from each list. An example might be "Thou impertinent rump-fed miscreant".

