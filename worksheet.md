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

## Putting your insults in a CSV file

1. You will need to find some suitable Shakespearean words to use. Make sure to only use Elizabethan insults - they are witty, intelligent and unlikely to actually offend your friends! We found a big list of [Shakespearean insults](https://www.theatrefolk.com/free-resources) on this page (search for "Shakespearean insults").

1. Now open up a document in a spreadsheet editor. These instructions are for LibreOffice Calc, which is included on the latest distribution of Raspbian, but this process works in a very similar way in other spreadsheet programs such as Microsoft Excel. Copy and paste the first column of insults into your spreadsheet, pressing OK if a box pops up.

  ![First column of insults](images/first-column.png)

1. Repeat this for the second and third columns, pasting them into columns B and C of the spreadsheet.

  ![All columns](images/all-cols.png)

1. Now save your file as `insults` and make sure to change the `File type` drop down to `Text CSV` before pressing save.

  ![Save your file](images/saving-file.png)

1. When a box pops up, choose to save the file in Text CSV format, and then press OK. Press OK on any further pop-ups.

  ![Save in text CSV format](images/use-text-csv.png)

1. Once your file has been saved, you can check that the data is now in CSV format. Right click on the file and select "Text editor" to open it up as plain text. You should see the insults you pasted in, separated by commas.

  ![See the CSV format](images/see-format.png)

## Open and read from a file

## Lists in Python

## Randomly choosing an insult

## Displaying the result on a GUI

# Sorting the results
