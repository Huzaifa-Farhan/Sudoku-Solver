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

## Installation
To install the required Python packages, run:  

   ```bash
   pip install pyautogui numpy

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

4. Have the Sudoku puzzle open right next to the script. When you click run, click the top left box of the puzzle right away so the puzzle can be filled out directly.

## Important Notes
Ensure the Code Runs Perfectly: For the correct results, make sure that the script runs without interruptions. The use of pyautogui simulates keyboard actions, so ensure that your cursor is on a suitable text editor or input field that can accept the simulated key presses.
Example
makefile
Copy code
Input:
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079

Output:
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Acknowledgments
Special thanks to the developers of the pyautogui and numpy libraries.

Make sure to run the code perfectly to see the correct results!
