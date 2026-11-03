
# --------------------------------------------------
# SUDOKU SOLVER
# --------------------------------------------------


# Check whether a number can be placed in a specific cell.
def is_valid_move(grid, row, col, number):

    # Check the row.
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check the column.
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Find the top-left corner of the corresponding 3x3 block.
    corner_row = row - row % 3
    corner_col = col - col % 3

    # Check the 3x3 block.
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


# --------------------------------------------------
# SOLVE THE SUDOKU
# --------------------------------------------------

# Solve the Sudoku using recursive backtracking.
def solve(grid, row, col, solutions):

    # Stop searching once two solutions have been found.
    if len(solutions) >= 2:
        return

    # Move to the next row when the current row is finished.
    if col == 9:
        row += 1
        col = 0

    # If all rows are completed, a solution has been found.
    if row == 9:
        solutions.append([r[:] for r in grid])
        return

    # Skip cells that already contain a number.
    if grid[row][col] != 0:
        solve(grid, row, col + 1, solutions)
        return

    # Try numbers from 1 to 9 in the empty cell.
    for number in range(1, 10):

        # Check whether the number is valid.
        if is_valid_move(grid, row, col, number):

            # Place the number in the grid.
            grid[row][col] = number

            # Recursively solve the next cell.
            solve(grid, row, col + 1, solutions)

            # Undo the move and try another number.
            grid[row][col] = 0

            # Stop if two solutions have already been found.
            if len(solutions) >= 2:
                return


# --------------------------------------------------
# VALIDATE THE INITIAL GRID
# --------------------------------------------------

# Check that the numbers already entered follow Sudoku rules.
def is_valid_grid(grid):

    # Check every cell in the grid.
    for row in range(9):
        for col in range(9):

            number = grid[row][col]

            # Only check cells that contain a number.
            if number != 0:

                # Temporarily empty the cell so it does not
                # conflict with itself during the validity check.
                grid[row][col] = 0

                # Check whether the number is valid.
                valid = is_valid_move(grid, row, col, number)

                # Restore the original number.
                grid[row][col] = number

                # Stop if a conflict is found.
                if not valid:
                    return False

    return True


# --------------------------------------------------
# FIND THE SOLUTION(S)
# --------------------------------------------------

# Find up to two solutions for a given Sudoku grid.
def find_solutions(grid):

    # Check that the grid has the correct dimensions.
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        return None

    # Check that all values are integers from 0 to 9.
    for row in grid:
        for number in row:
            if not isinstance(number, int) or number not in range(10):
                return None

    # Check whether the initial puzzle is valid.
    if not is_valid_grid(grid):
        return None

    # Create a fresh grid so the original input is not changed.
    working_grid = [row[:] for row in grid]

    # Create an empty list to store the solutions.
    solutions = []

    # Start solving from the first cell.
    solve(working_grid, 0, 0, solutions)

    # Return the solutions.
    return solutions
