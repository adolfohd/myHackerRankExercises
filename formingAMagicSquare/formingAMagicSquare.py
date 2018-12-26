import os
import sys
import math
import getMagicSquareList as magic


def formingMagicSquare(s):
    magicMatrixList = magic.getMagicSquareList(3)
    costs = []
    for currentMatrix in magicMatrixList:
        currentMatrixCost = 0
        for sRow, currentMatrixRow in zip(s, currentMatrix):
            for sElement, currentMatrixElement in zip(sRow, currentMatrixRow):
                currentMatrixCost += abs(sElement - currentMatrixElement) 
        costs.append(currentMatrixCost)
    return(min(costs))

s = [[4, 9, 2,],
    [ 3, 5, 7],
    [ 8, 1, 5]]

print(formingMagicSquare(s))