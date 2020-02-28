## What is a CSV file?

A **Comma Separated Values** file (or CSV file as it's commonly known) is a very basic way of storing data for use in a Python program. It's simply a text file where the contents are in a specific format: separated by commas. For instance, this could be an example of data stored in a CSV file:

```CSV
john, paul, george, ringo
```

Sometimes the values are **encapsulated**. For example, they may be encapsulated with quotes like this:

```CSV
"john", "paul", "george", "ringo"
```

This is usually because the data itself contains commas, so we need to avoid confusion between where a comma represents a break between different data items, and where it's simply part of the data. For example, in this CSV file encapsulation is definitely necessary:

```CSV
"Tabitha, slayer of mice", "Tiddles, drinker of milk", "Tiffany, leaver of hairballs"
```

The most basic way of creating a CSV file is to type data into a text file in CSV format, and then save the file with the extension `.csv`. Alternatively, you could use a program such as LibreOffice Calc or Microsoft Excel to create and save a file in CSV format.

