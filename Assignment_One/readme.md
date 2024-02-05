# Assignment 1  |  Stable Matching Problem

## Class
- CS4306: Algorithm Analysis
- Instructor: M. Alexiou
- Section: ?

## Team
- Sergio Sanchez-Alvares
  - Student ID: 001123021
- Zion Johnson
  - Student ID: 000878533

## Program Structure
___All files must be located in the same directory___
1. Hospital Object ```Hospital.py```
   1. name string
   2. slots num
   3. preferences list
   4. current_matched list
2. Resident Object ```Resident.py```
   1. name string
   2. preferences list
   3. current_match string
3. Algorithm ```stable_matching.py```
   1. Input csv file
   2. Compute Algorithm
   3. Print process and result to terminal

## Input
Accepts a csv file. Capitalization and white space does not affect the performance of the program.
 
Define the csv file on ```line 9``` as follows: 

    './<File Name>.csv'

The csv should be structured similar to the example on the assignment instructions

    Hospital Name, Number of Slots, Preferences seperated by commas in decending order
    ...
    <Empty line signals that hospital list has ended and residents begin>
    Resident Name, Preferences seperated by commas in decending order
    ...

## Output

<u>*Output is printed to the terminal and csv file*.</u>

Each iteration gets an output as shown below:
    
    Iteration Number
    Action Taken

At the end of the algorithm, the list is re-ordered to hospitals and residents together

    Hospital Name, Resident 1, ... , Resident n

Official output is written to `output.csv`
