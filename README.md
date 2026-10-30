# Sudoku

## Sudoku Solver

A Python-based Sudoku solver that uses **recursive backtracking** to find all possible solutions to a given Sudoku puzzle.

The solver checks whether numbers can be placed according to standard Sudoku rules and systematically explores possible combinations until it finds valid completed grids.

## How it works

The solver uses two main functions:

### 1. `is_valid_move(grid, row, col, number)`

This function checks whether a number can be placed in a specific cell without breaking Sudoku rules.

It checks three conditions:

- **Row:** The number must not already exist in the same row.
- **Column:** The number must not already exist in the same column.
- **3×3 box:** The number must not already exist in the corresponding 3×3 box.

The function returns `True` if the move is valid and `False` otherwise.

### 2. `solve(grid, row, col, solutions)`

This function solves the puzzle using recursive backtracking.

The algorithm works as follows:

1. **Move through the grid:** The solver starts at the first cell (row 0, column 0) and moves from left to right, then top to bottom.
2. **Skip filled cells:** If a cell already contains a number, the solver moves to the next cell.
3. **Try possible numbers:** If a cell is empty (represented by `0`), the solver tries numbers from 1 to 9.
4. **Check validity:** Each number is checked using `is_valid_move()`.
5. **Continue recursively:** If a number is valid, it is placed in the cell and the solver calls itself to process the next cell.
6. **Backtrack if necessary:** If a chosen number eventually leads to a dead end, the solver resets that cell to `0` and tries the next possible number.
7. **Store solutions:** When the solver reaches the end of the grid, it has found a valid solution. A copy of the completed grid is saved in the `solutions` list.

The process continues until all possible combinations have been explored.

## Understanding recursive backtracking

**Recursion** means that a function calls itself. Here, `solve()` repeatedly calls itself to move forward through the Sudoku grid, one cell at a time.

**Backtracking** means undoing a previous choice when it leads to a dead end. The solver removes the number it placed and tries another possibility.

Together, these concepts allow the solver to explore different combinations systematically until all valid solutions have been found.

## Input format

The Sudoku puzzle is represented as a list of nine lists, each containing nine integers.

- Numbers `1–9` represent filled cells.
- `0` represents an empty cell.

Example:

```python
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
```

## Running the solver

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <repository-name>
   ```

3. Add your Sudoku puzzle to the `grid` variable in the Python script.

4. Run the script:

   ```bash
   python sudoku_solver.py
   ```

The solver creates a new empty `solutions` list each time it runs, so solutions from previous puzzles are not carried over.

## Output

The solver prints:

- The total number of valid solutions found.
- Each completed Sudoku grid.

Depending on the puzzle, the solver may find:

- **No solutions:** The puzzle has no valid completion.
- **One solution:** The puzzle has a unique solution.
- **Multiple solutions:** More than one valid completion exists.
