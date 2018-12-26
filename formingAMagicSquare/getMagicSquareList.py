import os
import sys
import math
import getMagicSquare

def reflectSquare(squareMatrix):
    return(list(reversed(squareMatrix)))

def rotateSquare(squareMatrix):
    return(list(zip(*reversed(squareMatrix))))

def getMagicSquareList(size):
    basicMagicSquare = getMagicSquare.getMagicSquare(size)

    magicSquareList = []
    magicSquareList.append(basicMagicSquare)
    magicSquareList.append(reflectSquare(basicMagicSquare))
    for i in range(3):
        basicMagicSquare = rotateSquare(basicMagicSquare)
        magicSquareList.append(basicMagicSquare)
        magicSquareList.append(reflectSquare(basicMagicSquare))
    return(magicSquareList)

# magicSquareList = getMagicSquareList(3)
# for i in range(len(magicSquareList)):
#    print(magicSquareList[i])