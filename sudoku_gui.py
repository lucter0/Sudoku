# --------------------------------------------------
# SUDOKU SOLVER - GRAPHICAL USER INTERFACE (GUI)
# --------------------------------------------------

import tkinter as tk
from tkinter import messagebox

from sudoku_solver import find_solutions


# --------------------------------------------------
# COLOURS
# --------------------------------------------------

BACKGROUND = "#F5F5F2"
CELL_BACKGROUND = "#FFFFFF"
TEXT_COLOR = "#252A34"
DARK_BLUE = "#002944"
BLUE = "#80BDE5"
GRID_COLOR = "#002944"
LIGHT_GREY = "#E5E7EB"

# --------------------------------------------------
# CREATE THE MAIN WINDOW
# --------------------------------------------------

root = tk.Tk()

root.title("Sudoku Solver")
root.geometry("660x660")
root.resizable(True, True)
root.configure(bg=BACKGROUND)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

title = tk.Label(
    root,
    text="Sudoku Utan Ansträngning",
    font=("Helvetica", 26, "bold"),
    bg=BACKGROUND,
    fg=TEXT_COLOR
)

title.pack(pady=(25, 5))


instructions = tk.Label(
    root,
    text="Logiskt tänkande är valfritt.\nFyll i siffrorna från ditt Sudoku:",
    font=("Helvetica", 12),
    bg=BACKGROUND,
    fg="#777777"
)

instructions.pack(pady=(0, 20))

# --------------------------------------------------
# VALIDATE USER INPUT
# --------------------------------------------------

# Only allow:
# - A single digit between 1 and 9.
# - An empty cell (to allow deleting a number).
def validate_input(value):

    if value == "":
        return True

    if len(value) == 1 and value in "123456789":
        return True

    return False


# Register the validation function with Tkinter.
# "%P" represents the value the cell would have after editing.
validate_command = (root.register(validate_input), "%P")

# --------------------------------------------------
# CREATE THE SUDOKU GRID
# --------------------------------------------------

# Define the size of each square cell.
CELL_SIZE = 42

# Define the spacing between cells.
CELL_GAP = 1

# Define the extra spacing between 3x3 blocks.
BLOCK_GAP = 5

# Calculate the total grid dimensions, including the outer border.
OUTER_BORDER = 3

GRID_SIZE = (
    9 * CELL_SIZE
    + 6 * CELL_GAP
    + 2 * BLOCK_GAP
    + 2 * OUTER_BORDER
)

# Create the main grid frame.
grid_frame = tk.Frame(
    root,
    bg=DARK_BLUE,
    width=GRID_SIZE,
    height=GRID_SIZE
)

grid_frame.pack(pady=5)

# Prevent the frame from automatically changing its dimensions.
grid_frame.pack_propagate(False)

# Store all 81 entry boxes.
entries = []

for row in range(9):

    entry_row = []

    for col in range(9):

        # Calculate the exact position of each cell.
        x = (
            OUTER_BORDER
            + col * CELL_SIZE 
            + (col - col //3) * CELL_GAP
            + (col // 3) * BLOCK_GAP
        )

        y = (
            OUTER_BORDER
            + row * CELL_SIZE 
            + (row - row //3) * CELL_GAP
            + (row // 3) * BLOCK_GAP
        )

        # Create an editable Sudoku cell.
        entry = tk.Entry(
            grid_frame,
            font=("Helvetica", 17),
            justify="center",
            bg=CELL_BACKGROUND,
            fg=TEXT_COLOR,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            insertbackground=DARK_BLUE,
            validate="key",
            validatecommand=validate_command
        )

        # Position the cell using exact pixel dimensions.
        entry.place(
            x=x,
            y=y,
            width=CELL_SIZE,
            height=CELL_SIZE
        )

        entry_row.append(entry)

    entries.append(entry_row)

# --------------------------------------------------
# SOLVE BUTTON FUNCTION
# --------------------------------------------------

def solve_puzzle():

    # Read the numbers entered into the Sudoku GUI.
    grid = []

    for row in range(9):

        grid_row = []

        for col in range(9):

            value = entries[row][col].get().strip()

            if value == "":
                number = 0

            else:
                number = int(value)

            grid_row.append(number)

        grid.append(grid_row)

    # Find up to two possible solutions.
    # The solver finishes calculating before the GUI is updated.
    solutions = find_solutions(grid)

    # Check whether the initial puzzle is valid.
    if solutions is None:
        status_label.config(
            text="Nope, nu bryts det mot reglerna!.",
            fg="#D9534F"
        )
        return

    # Check whether a solution exists.
    if len(solutions) == 0:
        status_label.config(
            text="Ingen lösning hittad.",
            fg="#D9534F"
        )
        return

    # Get the complete solution.
    solution = solutions[0]

    # Fill in the entire Sudoku grid.
    for row in range(9):
        for col in range(9):

            original_number = grid[row][col]

            # Only insert numbers into originally empty cells.
            if original_number == 0:

                entries[row][col].delete(0, tk.END)

                entries[row][col].insert(
                    0,
                    str(solution[row][col])
                )

                # Numbers added by the solver become blue.
                entries[row][col].config(
                    fg=BLUE,
                    font=("Helvetica", 17, "normal")
                )

            else:
                # Original numbers become dark blue (bold)
                entries[row][col].config(
                    fg=DARK_BLUE,
                    font=("Helvetica", 17, "bold")
                )

    # Display the result.
    if len(solutions) == 1:
        status_label.config(
            text="Löst! Det där var väl inte så svårt?! Nästa Sudoku, tack.",
            fg="#27845B"
        )

    else:
        status_label.config(
            text="Löst! Det där var väl inte så svårt?! Nästa Sudoku, tack.",
            fg="#27845B"
        )

# --------------------------------------------------
# CLEAR BUTTON FUNCTION
# --------------------------------------------------

def clear_grid():

    # Empty all cells and restore their original appearance.
    for row in range(9):
        for col in range(9):

            entries[row][col].delete(0, tk.END)

            entries[row][col].config(
                fg=TEXT_COLOR,
                font=("Helvetica", 17, "normal")
            )

    status_label.config(text="")

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

button_frame = tk.Frame(root, bg=BACKGROUND)
button_frame.pack(pady=(25, 10))


# Solve button.
solve_button = tk.Button(
    button_frame,
    text="Abrakadabra",
    command=solve_puzzle,
    font=("Helvetica", 12, "bold"),
    bg=BACKGROUND,
    fg=DARK_BLUE,
    activebackground=BACKGROUND,
    activeforeground=DARK_BLUE,
    relief="flat",
    borderwidth=0,
    highlightthickness=1,
    highlightbackground=DARK_BLUE,
    highlightcolor=DARK_BLUE,
    cursor="hand2",
    padx=35,
    pady=10
)

solve_button.grid(row=0, column=0, padx=8)


# Clear button.
clear_button = tk.Button(
    button_frame,
    text="Börja om",
    command=clear_grid,
    font=("Helvetica", 12),
    bg=BACKGROUND,
    fg=DARK_BLUE,
    activebackground=BACKGROUND,
    activeforeground=DARK_BLUE,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    padx=35,
    pady=10
)

clear_button.grid(row=0, column=1, padx=8)

# --------------------------------------------------
# STATUS MESSAGE
# --------------------------------------------------

status_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 11),
    bg=BACKGROUND
)

status_label.pack(pady=10)


# --------------------------------------------------
# RUN THE APPLICATION
# --------------------------------------------------

root.mainloop()
