import os
import sys


def getPrimes(number):
    primes = []
    for i in range(1,number+1):
        totalFactors = 0
        for j in range(1,i+1):
            if (i % j == 0):
                totalFactors += 1
        if (totalFactors == 2):
            primes.append(i)
    return(primes)

def getMCM(a):
    primes = getPrimes(max(a))
    nPrimes = len(primes)

    primesOfA = [0] * nPrimes
    primesOfB = [0] * nPrimes
    for ai in a:
        for i in range(nPrimes):
            
            
        
'''
def getTotalX(a, b):
    getMCM(a)


a = [2,6];
b = [24,36];

getTotalX(a, b);

'''