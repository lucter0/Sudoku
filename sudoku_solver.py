# --------------------------------------------------
# FUNCTION 1: CHECK IF A NUMBER IS A VALID MOVE
# --------------------------------------------------
# This function checks whether a number can be placed
# in a specific cell without breaking Sudoku rules.
#
# grid   = the Sudoku grid
# row    = the row index (0-8)
# col    = the column index (0-8)
# number = the number we want to place (1-9)


def is_valid_move(grid, row, col, number):

    # Check the entire row.
    # range(9) gives us the numbers 0-8. (indexing is 0-8, so 9 values)
    # If the number already exista in this row, the move is invalid.
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check the entire column.
    # If the number already exists in this column, the row is invalid.
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Find the top-left corner of the 3x3 box that contains our current cell.
    # The modulo operator (%) gives the remainder that helps find the beginning of the box.
    # Eg: if row = 5, then 5 - (5 % 3) = 3.
    corner_row = row - row % 3
    corner_col = col - col % 3

    # Check all nine cells inside 3x3 box.
    for x in range(3):
        for y in range(3):

            # If the number already exists in the box, the move is invalid. 
            if grid[corner_row + x][corner_col + y] == number:
                return False

    # If the number does not exist in the row, column or 3x3 box, the move is valid.
    return True

# --------------------------------------------------
# FUNCTION 2: SOLVE THE SUDOKU USING BACKTRACKING
# --------------------------------------------------

# This function tries to solve the Sudoku.
#
# grid      = the Sudoku grid
# row       = current row position
# col       = current column position
# solutions = a list where we store all completed
#             Sudoku solutions

def solve(grid, row, col, solutions):

    # If we reach column 9, we have finished the current row because the columns are indexed 0-8.
    #
    # Move to the next row and reset the column to 0.
    if col == 9:
        row += 1
        col = 0

    # If we reach row 9, we have completed all nine rows.
    # This means we have found a complete solution.
    if row == 9:

        # Save a copy of the completed Sudoku grid.
        # 
        # r[:] creates a copy of each row.
        # This is important because the original grid will continue changing during backtracking.
        solutions.append([r[:] for r in grid])

        # Return to the previous recursive call.
        # We do not stop the entire search here.
        return


    # Check whether the current cell already contains a number from the original Sudoku puzzle.
    #
    # If the value is greater than 0, we assume it is a given number and move to the next cell.
    if grid[row][col] > 0:

        # Recursive call: continue with the next column.
        solve(grid, row, col + 1, solutions)

        # No need to check other numbers in this cell
        return

    # Try current cell is empty (value = 0).
    # Try every possible number from 1 to 9.
    for number in range(1, 10):

        # Check wheter the number follows Sudoku rules.
        if is_valid_move(grid, row, col, number):

            # If the move is valid, temporarily place the number in the current cell.
            grid[row][col] = number

            # Recursive call: Move to the next cell and try to solve the rest of the Sudoku.
            solve(grid, row, col + 1, solutions)

            # BACKTRACKING:
            # After the recursive call returns, reset the cell to 0 so we can try another number.
            # This allows the algorithm to explore alternative solutions.
            grid[row][col] = 0


# --------------------------------------------------
# STEP 3: DEFINE THE INITIAL SUDOKU GRID
# --------------------------------------------------

# Each inner list represents one row.
# Each number represents one cell.
#
# 0 represents an empty cell.
# Numbers 1-9 represent the given numbers.

grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]

# --------------------------------------------------
# STEP 4: FIND ALL POSSIBLE SOLUTIONS
# --------------------------------------------------

# Create an empty list to store the solutions.
solutions = []

# Start solving from the first cell: row = 0, col = 0.
# The function will search through the entire grid and store every valid completed solution.
solve(grid, 0, 0, solutions)

# --------------------------------------------------
# STEP 5: PRINT THE RESULTS
# --------------------------------------------------

# Check how many solutions were found.
if len(solutions) == 0:

    # No valid solutions were found.
    print("Ingen lösning hittades för den här sudokun.")

else:

    # Print the total number of solutions.
    print(f"Antal möjliga lösningar: {len(solutions)}")

    # Check wheter the Sudoku has one or multiple solutions.
    if len(solutions) == 1:
        print("Sudokun har en unik lösning")
    else:
        print("Sudokun har flera möjliga lösningar")

    # Go through every solution in the solutions list.
    #
    # enumerate() gives us both:
    # - solution_number: the solution's position
    # - solution: the actual completed Sudoku grid
    #
    # start=1 makes the numbering begin at 1 instead of 0.
    for solution_number, solution in enumerate(solutions, start=1):

        # Print the amount of possible solutions.
        print(f"\nLösning {solution_number}:")

        # Print the Sokudo grid row by row.
        for i in range(9):

            # Print each number in the row.
            # end=" " keeps the numbers on the same line. 
            for j in range(9):
                print(solution[i][j], end=" ")

            # Move to a new line after each row.     
            print()

