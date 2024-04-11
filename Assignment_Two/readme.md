# Assignment 2  |  The Skyline Problem

## Class
- CS4306: Algorithm Analysis
- Instructor: M. Alexiou
- 
## Team
- Sergio Sanchez-Alvares
  - Student ID: 001123021
- Zion Johnson
  - Student ID: 000878533

## Program Structure
___All files must be located in the same directory___

### CSV Reader
Reads the csv file. Will record each row as a building tuple and append it
to the buildings array

### Skyline Shaper
This function takes in the buildings array as a parameter

It looks through each building and takes the height, left, and right bound

It sorts the buildings based on the right bound position

On each iteration, it will check if any buildings should have ended and remove them

It keeps track of the max height. Should it change on each iteration, it will adjust

returns the skyline array

## Input
Accepts a csv file as defined in the assignment instructions.

Input comes from input files in the `InputsOuputs` directory
 
Define the csv file on `line 9` as follows: 

    './<File Name>.csv' 

The csv should be structured similar to the example on the assignment instructions

    Building Height, Left Bound Position, Right Bound Position
    |
    Repeat

The program assumes that the data points are ordered in ascending order.
The same way that the assigment example is ordered.

## Output

<u>*Output is printed to the terminal and csv files*.</u>

    Height, X position
    |
    Repeat

Output is written to csv files in the `InputOutput` directory
