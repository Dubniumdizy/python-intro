"""Creates a custom 3x5 coordinate-indexed matrix."""


ROWS = 3
COLS = 5
grid = []
for r in range(ROWS):
    row_data = []
    for c in range(COLS):
        value = (r + 1) * 10 + (c + 1)
        row_data.append(value)
    grid.append(row_data)

matrix = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]

"""
list comprehension = [for each element in X, do this on the element, save as a list]
"""