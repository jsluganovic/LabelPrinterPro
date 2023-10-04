# Barcode_gen

## What is a barcode? 

A barcode is a method of representing data in visual, machine-readable format. Typically a 1D barcode. 


## What is the logic behind the barcode generator?

The barcode generator is a function that takes in a string of numbers and outputs a barcode. The barcode is a list of 1s and 0s. The 1s and 0s are then used to generate a barcode image.


## Random 

> 95 bars, either black or white 

> first three bars are always black, white black and long

> middle ones same but short 

> last ones same as first 

-> This is all to differencitate the different section of the barcode

> the remaining 84 bars are split into groups of 7 to create 12 sections, each group of 7 corresponds to a number 