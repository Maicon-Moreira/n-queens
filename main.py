from numba import jit
from tqdm import tqdm
import numpy as np
import time
import json
def current_milli_time(): return int(round(time.time() * 1000))


solutions = []
uniqueSolutions = []
N = 11
calculations = 0
findAll = True
finded = False
board = np.zeros((N, N))

solutions.append(board.copy())


@jit()
def calculate(board, depth, N, solutions):
    calculations = 1

    if validBoard(board, N):
        if depth == N:
            solutions.append(board.copy())

        else:
            x = depth
            for y in range(N):
                if board[x][y] == 0:

                    board[x][y] = 1

                    child_calculations = calculate(
                        board, depth + 1, N, solutions)
                    calculations += child_calculations

                    board[x][y] = 0

    return calculations


@jit()
def validBoard(board, N):
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:

                for vX in range(-1, 2):
                    for vY in range(-1, 2):
                        if not (vX == 0 and vY == 0):

                            d = 0
                            while True:
                                d += 1
                                newX = x + vX * d
                                newY = y + vY * d

                                if newX < N and newX >= 0 and newY < N and newY >= 0:
                                    if board[newX][newY] == True:
                                        return False

                                else:
                                    break

    return True


def isUnique(solution):
    for uniqueSolution in uniqueSolutions:
        if not isDiff(solution, uniqueSolution):
            return False

    return True


def isDiff(a, b):
    for x in range(N):
        for y in range(N):
            if a[x][y] != b[x][y]:
                return True
    return False


before = current_milli_time()
calculations = calculate(board, 0, N, solutions)
after = current_milli_time()

print('\n\ntime elapsed', after-before)


for solution in solutions:
    if isUnique(solution):
        uniqueSolutions.append(solution)

uniqueSolutions = [a.tolist() for a in uniqueSolutions]
uniqueSolutions = uniqueSolutions[1:]


print(calculations, 'nodes')
print(len(uniqueSolutions), 'results')


with open('results.json', 'w') as file:
    file.write(json.dumps(uniqueSolutions))
