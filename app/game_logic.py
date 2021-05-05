import numpy as np
import random


def init_grid(grid):
    rows = grid.rows_count
    columns = grid.columns_count

    # initialise new grid
    grid_array = np.array([[0 for col in range(columns)] for row in range(rows)])

    # add mines to grid array
    mines = grid.mines_count

    while mines > 0:
        mine_location = [random.randint(0, rows - 1), random.randint(0, columns - 1)]

        if grid_array[mine_location[0], mine_location[1]] == -1:
            continue

        grid_array[mine_location[0], mine_location[1]] = -1

        print(grid_array[mine_location[0], mine_location[1]])

        mines -= 1

    # place numbers onto board based on the number of mines in the neighbouring locations
    for row in range(rows):
        for column in range(columns):
            if grid_array[row][column] == -1:
                continue

            mine_count = 0
            neighbourhood = get_neighbours(row, column, rows, columns)

            # count the number of mines around the current square at coordinates (row, col)
            for neighbour in neighbourhood:
                # disregards if neighbour is not a mine
                if grid_array[neighbour[0]][neighbour[1]] != -1:
                    continue

                # increment mine count
                mine_count += 1

            grid_array[row][column] = mine_count

    return grid_array


def get_neighbours(row, column, rows, columns):
    neighbours = {1: [-1, -1], 2: [-1, 0], 3: [-1, 1], 4: [0, -1], 5: [0, 1], 6: [1, -1], 7: [1, 0], 8: [1, 1]}

    neighbourhood = []

    for position in neighbours:
        neighbour_row = row + neighbours[position][0]
        neighbour_col = column + neighbours[position][1]

        # ensures neighbour locations do not go out of of board bounds
        if neighbour_row < 0 or neighbour_col < 0 or neighbour_row > rows - 1 or neighbour_col > columns - 1:
            continue

        neighbourhood.append([neighbour_row, neighbour_col])

    return neighbourhood
