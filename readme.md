# Smarter Sorter

This is a Python script that sorts items based on their dimensions 
and weight. It provides a function `sort` that takes four parameters:
width, height, length, and mass. 
The function returns a string indicating the sorting category of the item.
Category is defined by:
- STANDARD: acceptable dimensions and weight.  Acceptable dimensions are each < 150 cm and total volume < 1,000,000 cm³.  Acceptable weight is < 20kg
- SPECIAL: dimensions OR weight outside acceptable range
- REJECTED: unacceptable dimensions AND weight

The script also includes a helper function `help_sort` that prints the input parameters and the sorting result for testing purposes.

To use the script, edit the script to provide the dimensions and weight of the item you want to sort and run the script directly.  It does not have a main entry point.
The script will output the sorting category of the item.
