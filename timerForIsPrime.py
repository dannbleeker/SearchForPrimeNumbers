#!/usr/bin/env python3

import timeit


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(1, 1000000):
    if isPrimeSearch.checkForPrime(currentNumber) == True:
        primeCounter += 1     
'''
#print( "\nCheckForPrime1: %s" % timeit.timeit(stmt = TEST_CODE, number = 5)  )

TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
currentNumber = 100000000
while currentNumber <= 110000000:
    if isPrimeSearch.checkForPrime5(currentNumber) == True:
        primeCounter +=  1
        currentNumber += 1
    currentNumber += 1
'''
print( "\nCheckForPrime5 + 1: %s" % timeit.timeit(stmt = TEST_CODE, number = 5)  )

TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000000, 110000000):
    if isPrimeSearch.checkForPrime5(currentNumber) == True:
        primeCounter += 1     
'''
print( "\nCheckForPrime5: %s" % timeit.timeit(stmt = TEST_CODE, number = 5)  )

TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(1000000, 2000000):
    if isPrimeSearch.checkForPrime2(currentNumber) == True:
        primeCounter += 1     
'''
#print( "CheckForPrime2: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(1000000, 2000000):
    if isPrimeSearch.checkForPrime3(currentNumber) == True:
        primeCounter += 1     
'''
#print( "CheckForPrime3: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000, 200000):
    if isPrimeSearch.checkForPrime4(currentNumber) == True:
        primeCounter += 1     
'''
#print( "CheckForPrime4: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )

