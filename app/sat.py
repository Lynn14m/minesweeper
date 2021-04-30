import pycosat
from pprint import pprint
import numpy as np


# Chase's Twiddle Algorithm 382
# Taken from https://gist.github.com/gorayni/08b5bc780e68c5820072d7a51e825559
def twiddle(p, x=None, y=None, z=None):
    j = np.argmax(p[1:] > 0) + 1

    if p[j - 1] == 0:
        i = j - 1
        while i != 1:
            p[i] = -1
            i -= 1
        p[j], p[1] = 0, 1
        return (0, j - 1, 0, False)

    if j > 1:
        p[j - 1] = 0
    j += 1
    while p[j] > 0:
        j += 1

    i, k = j, j - 1
    while p[i] == 0:
        p[i] = -1
        i += 1

    if p[i] == -1:
        p[i] = p[k]
        z = p[k] - 1
        p[k] = -1
        return (i - 1, k - 1, z, False)
    elif i != p[0]:
        p[j] = p[i]
        z = p[i] - 1
        p[i] = 0
        return (j - 1, i - 1, z, False)

    return (x, y, z, True)


# Chase's Twiddle Algorithm 382
# Taken from https://gist.github.com/gorayni/08b5bc780e68c5820072d7a51e825559
def init_twiddle(m, n):
    p = np.zeros((n + 2), dtype=int)

    p[0] = n + 1
    p[n - m + 1:n + 1] = np.arange(1, m + 1)
    p[n + 1] = -2
    if m == 0:
        p[1] = 1
    return p


def at_least_k(neighbours, k):
    pass


def at_most_k(neighbours, k):
    clause_array = []
    temp_clause_array = []
    choices_length = k + 1
    neighbours_length = len(neighbours)

    combinations = np.zeros(neighbours_length, dtype=int)
    combinations[neighbours_length - choices_length:] = 1

    temp_arr = []
    for combination in combinations:
        temp_arr.append(combination)

    temp_clause_array.append(temp_arr)

    p = init_twiddle(choices_length, neighbours_length)
    x, y, z, done = twiddle(p)
    while not done:
        temp_arr = []

        combinations[x], combinations[y] = 1, 0

        for combination in combinations:
            temp_arr.append(combination)

        temp_clause_array.append(temp_arr)

        x, y, z, done = twiddle(p, x, y, z)

    # Map to neighbours
    for clause in temp_clause_array:
        temp_arr = []
        for i in range(0, len(neighbours)):
            # If literal is true (1)
            if clause[i]:
                temp_arr.append(neighbours[i])
            # If literal is false (0)
            if not clause[i]:
                temp_arr.append(neighbours[i] * -1)
        clause_array.append(temp_arr)

    # Return clauses for at most k
    return clause_array


def exactly_k():
    pass
