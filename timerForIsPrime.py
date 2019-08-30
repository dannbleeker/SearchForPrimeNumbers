#!/usr/bin/env python3
import timeit

import sys
temp = sys.stdout # store original stdout object for later



sys.stdout = open('log.txt', 'a') # redirect all prints to this log file

# Indsæt variable heri

startNumber = 1000100000
endNumber = 1000200000

print ("Searching from %s to %s (interval: %s)" % (f"{startNumber:,d}".replace(",","."), f"{endNumber:,d}".replace(",","."), f"{(endNumber-startNumber):,d}".replace(",",".")))

# [1, 2, 3, 5, 6]

for currentPrimeSearch in range (1,7):
    TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
currentNumber = %s
while currentNumber <= %s:
    if isPrimeSearch.checkForPrime%s(currentNumber) == True:
        primeCounter +=  1
    currentNumber += 1
''' % (startNumber, endNumber, currentPrimeSearch)
    #print(TEST_CODE)
    print("CheckForPrime%s (whl): %s" % (currentPrimeSearch,round(timeit.timeit(stmt = TEST_CODE, number = 1),4)  ))

## With skip one after prime
    
for currentPrimeSearch in range (1,7):
    TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
currentNumber = %s
while currentNumber <= %s:
    if isPrimeSearch.checkForPrime%s(currentNumber) == True:
        primeCounter +=  1
        currentNumber += 1        
    currentNumber += 1
''' % (startNumber, endNumber, currentPrimeSearch)

    print("CheckForPrime%s (wsa): %s" % (currentPrimeSearch,round(timeit.timeit(stmt = TEST_CODE, number = 1),4)  ))

## With for loop
for currentPrimeSearch in range (1,7):
    TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(%s, %s):
    if isPrimeSearch.checkForPrime%s(currentNumber) == True:
        primeCounter +=  1
''' % (startNumber, endNumber, currentPrimeSearch)
    #print(TEST_CODE)
    print("CheckForPrime%s (for): %s" % (currentPrimeSearch,round(timeit.timeit(stmt = TEST_CODE, number = 1),4)  ))

sys.stdout.close()                # ordinary file object
sys.stdout = temp                 # restore print commands to interactive prompt