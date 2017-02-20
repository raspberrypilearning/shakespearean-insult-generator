# Shakespearean insult generator

Ever been lost for words? In this resource you will write a Python script to generate insults, Elizabethan style.

## What is a CSV file?

A **Comma Separated Values** file (or CSV file as it is commonly known) is a very basic way of storing data for use in a Python program. It is simply a text file where the contents are in a specific format - separated by commas. For example, this could be an example of data stored in a CSV file:

```CSV
john, paul, george, ringo
```

Sometimes the values are **encapsulated**, for example they may be encapsulated with quotes like this:

```CSV
"john", "paul", "george", "ringo"
```

This is usually because the data itself contains commas, so we need to avoid confusion between where a comma represents a break between different data items, and where it is simply part of the data. For example in this CSV file encapsulation is definitely necessary:

```CSV
"tabitha, slayer of mice", "tiddles, drinker of milk", "tiffany, leaver of hairballs"
```
The most basic way of creating a CSV file is to type data into a text file in CSV format, and then save the file with the extension `.csv`. Alternatively you could use a program such as LibreOffice Calc or Microsoft Excel to create and save a file in CSV format.

## Putting your insults into a CSV file

1. You will need to find some suitable Shakespearean words to use. Make sure to only use Elizabethan insults - they are witty, intelligent and unlikely to actually offend your friends! We found a big list of [Shakespearean insults](https://www.theatrefolk.com/free-resources) on this page (scroll down to the "Fun activities" section).

1. Now open up a document in a spreadsheet editor. These instructions are for LibreOffice Calc, which is included on the latest distribution of Raspbian, but this process works in a very similar way in other spreadsheet programs such as Microsoft Excel. Copy and paste the first column of insults into your spreadsheet, pressing OK if a box pops up.

  ![First column of insults](images/first-column.png)

1. Repeat this for the second and third columns, pasting them into columns B and C of the spreadsheet.

  ![All columns](images/all-cols.png)

1. Now save your file as `insults` and make sure to change the `File type` drop down to `Text CSV` before pressing save.

  ![Save your file](images/saving-file.png)

1. If a box pops up, choose to save the file in Text CSV format, and then press OK. Press OK on any further pop-ups.

  ![Save in text CSV format](images/use-text-csv.png)

1. Once your file has been saved, you can check that the data is now in CSV format. Right click on the file and select "Text editor" to open it up as plain text. You should see the insults you pasted in, separated by commas.

  ![See the CSV format](images/see-format.png)

## Open and read from a file

1. Now we need to read this file of insults into Python. From the `Programming` menu, open up `Python 3 (IDLE)`.

1. Click `File` > `New File` and save the file as `shakespeare.py`

1. Add the following code to open the file in read mode, read the full contents, and output the result:

  ```python
  with open("insults.csv", "r") as f:
    contents = f.read()
    print(contents)
  ```

1. What is the difference between the current line of code...

  ```Python
  contents = f.read()
  ```

  ...and this line of code?

  ```Python
  contents = f.readline()
  ```

  Change the code and see if you can work out the difference betweeen `read()` and `readline()`

1. So far we are able to read the insults from the file in the order they were written, but we can't do much with them. You may have noticed that the different columns forming the parts of the insult were different types of word. The first two columns (A and B) contain **adjectives** (describing words) and the final column (C) contains **nouns**, mostly in this case referring to a 'thing' the person resembles. If we could split them up, we could make randomised insults of the form "You [List A] [List B] [List C]", for example "You impertinent rump-fed miscreant".

## Lists in Python

1. We will add some code to read the file line by line and split each column into a separate list. You could try planning this yourself in pseudo code before looking at our solution below:

  ```
  CREATE list_a, list_b, list_c
  OPEN insults.csv in read mode
    WHILE there are still lines left to read:
      line = READ LINE
      words = line.SPLIT(",")
      APPEND words[0] to list_a
      APPEND words[1] to list_b
      APPEND words[2] to list_c
    END WHILE
  PRINT list_a
  ```

  The most unfamiliar part of this code is probably `words = SPLIT(line, ",")`. Here we will use Python's built in `split()` function to split up the line of text wherever there is a comma, and save the results as a list called `words`.

1. Here is the corresponding Python code for the code we planned above. Once again, you could have a go at translating your pseudo code into Python before you look at the solution below.

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
1. Save and run your program by pressing `F5`. You should find that the program outputs a list of all of the words you put in column A.

  ![Print list A](images/output-a.png)

1. Change your code to print out and check lists B and C too. You should spot a problem.

1. When you output `list_c` to check it, you will notice something strange - an extra `\n` character has been added to the end of each of the words:

  ![Print list C](images/output-c.png)

  The `\n` character is not a surprise when you find out that it means "new line". It is there because in our original CSV file, each group of three insult words were stored on a *new line*! However, we don't want to display it in our insult, so we can add some code to get rid of it.

1. Find this line in your code:

  ```python
  list_c.append(words[2])
  ```

  ...and add `.strip()` on the end of the word you are appending, to automatically strip out the `\n` and any other **whitespace characters**.

  ```python
  list_c.append( words[2].strip() )
  ```

## Randomly choosing an insult

## Displaying the result on a GUI

# Sorting the results
