import pyautogui as pg  # Import the pyautogui module for simulating keyboard/mouse actions
import numpy as np  # Import numpy for array manipulations (not used directly here)
import time  # Import time module for delays

grid = []  # Initialize an empty list to store the Sudoku grid

# Input loop to populate the Sudoku grid
while True:
    row = list(input('Row: '))  # Input a row of numbers as a string
    ints = []  # Initialize an empty list to store the integers of the row

    for n in row:
        ints.append(int(n))  # Convert each character to an integer and add to the list
    grid.append(ints)  # Add the row to the grid

    if len(grid) == 9:  # Check if 9 rows have been entered
        break  # Exit the loop when the grid is complete
    print('Row ' + str(len(grid)) + ' Complete')  # Print the row completion status

time.sleep(1)  # Wait for 1 second before proceeding

# Function to check if a number can be placed in a specific cell
def possible(x, y, n):
    # Check if the number n is already in the column (x)
    for i in range(9):
        if grid[i][x] == n and i != y:
            return False

    # Check if the number n is already in the row (y)
    for i in range(9):
        if grid[y][i] == n and i != x:
            return False

    # Check if the number n is already in the 3x3 subgrid
    x0 = (x // 3) * 3  # Calculate the top-left x-coordinate of the subgrid
    y0 = (y // 3) * 3  # Calculate the top-left y-coordinate of the subgrid
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):
            if grid[Y][X] == n:
                return False    
    return True  # Return True if the number n can be placed in the cell

# Function to print the grid using pyautogui
def Print(matrix):
    for row in matrix:
        for num in row:
            pg.press(str(num))  # Simulate key press for each number
            pg.hotkey('right')  # Move to the right in the GUI
        # Move to the next row in the GUI after each row is printed
        pg.hotkey('down')
        for _ in range(8):  # Move left 8 times to get to the beginning of the next row
            pg.hotkey('left')

# Recursive function to solve the Sudoku puzzle
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:  # If the cell is empty (contains 0)
                for n in range(1, 10):  # Try numbers from 1 to 9
                    if possible(x, y, n):  # Check if the number can be placed
                        grid[y][x] = n  # Place the number in the cell
                        solve()  # Recursively try to solve the rest of the grid
                        grid[y][x] = 0  # Reset the cell if the solution doesn't work
                return
    Print(grid)  # Print the solved grid using pyautogui

solve()  # Start solving the Sudoku puzzle
