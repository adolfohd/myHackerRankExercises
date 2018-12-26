import os
import sys
import math

def getMagicSquare(size):
    if (size % 2 != 0):
        return(getOddMagicSquare(size))
    else:
        print("Unhandled for even numbers")

def adjustCoordinate(pos, size):
    if pos <  0:
        return size-1
    if pos >= size:
        return 0
    return pos

def updatePosition(row, column, size, magicSquare):
    newRow    = adjustCoordinate(row    - 1, size)
    newColumn = adjustCoordinate(column + 1, size)
    if magicSquare[newRow][newColumn] != 0:
        newRow    = adjustCoordinate(row + 1, size)
        newColumn = column
    return([newRow, newColumn])


def getOddMagicSquare(size):
    magicSquare = [[0] * size for i in range(size)]    
    row    = 0
    column = math.ceil(size/2) - 1
    for i in range(1, size**2 +1):
        magicSquare[row][column] = i
        [row, column] = updatePosition(row, column, size, magicSquare)
    return(magicSquare)
