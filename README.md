# Sudoku-Solver
This Python script provides a solution for solving Sudoku puzzles. It uses backtracking to find the correct numbers for the grid and displays the solution using pyautogui.

## Features  
* Input Sudoku Grid: Enter the grid row by row.
* Solve the Puzzle: The script uses a recursive backtracking algorithm to solve the puzzle.
* Display the Solution: The solution is displayed using simulated key presses.

## Requirements
* Python 3.x
* pyautogui module
* numpy module

## Usage 
1. Run the Script:

   ```bash
   python sudoku_solver.py
   
2. Input the Sudoku Grid:  
You will be prompted to enter each row of the Sudoku grid. Enter the numbers without spaces, and use 0 for empty cells.  
Example input for a row:  

   ```bash
   530070000

3. Wait for the Solution:  
The script will process the input and solve the Sudoku puzzle. Once the solution is found, it will be displayed using pyautogui.  

## Important Notes
Ensure the code runs perfectly to see the correct results. The use of pyautogui simulates keyboard actions, so ensure that your cursor is on a suitable text editor or input field that can accept the simulated key presses.

## Example

* Input:

   ```bash
   530070000
   600195000
   098000060
   800060003
   400803001
   700020006
   060000280
   000419005
   000080079

* Output:

   ```bash
   534678912
   672195348
   198342567
   859761423
   426853791
   713924856
   961537284
   287419635
   345286179


> **Note:**
> I was able to create the following application by following the Tutorial created by 'Terranova Tech' on Youtube. Here is a link for the tutorial for anyone interested: [https://youtu.be/PY_N1XdFp4w?si=FD3UEbBrWPXYE23](https://youtu.be/jESGMTcrhSY?si=Gc1o1Zrg06ml1T-2)
