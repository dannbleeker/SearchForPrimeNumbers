#!/usr/bin/env python3

import timeit


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000, 200000):
    if isPrimeSearch.checkForPrime(currentNumber) == True:
        primeCounter += 1     
'''
print( "\nCheckForPrime1: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )

TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000, 200000):
    if isPrimeSearch.checkForPrime2(currentNumber) == True:
        primeCounter += 1     
'''
print( "CheckForPrime2: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000, 200000):
    if isPrimeSearch.checkForPrime3(currentNumber) == True:
        primeCounter += 1     
'''
print( "CheckForPrime3: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )


TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(100000, 200000):
    if isPrimeSearch.checkForPrime4(currentNumber) == True:
        primeCounter += 1     
'''
print( "CheckForPrime4: %s" % timeit.timeit(stmt = TEST_CODE, number = 1)  )

