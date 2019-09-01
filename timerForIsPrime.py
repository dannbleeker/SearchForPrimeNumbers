#!/usr/bin/env python3
import timeit

useLogFile = True

if (useLogFile):
    logfile = open('log.txt', 'a')  # redirect all prints to this log file

# Indsæt variable heri

startNumber = 0
endNumber = 100000000

print("Searching from %s to %s (interval: %s)" % (
    f"{startNumber:,d}".replace(",", "."), f"{endNumber:,d}".replace(",", "."),
    f"{(endNumber - startNumber):,d}".replace(",", ".")))

if (useLogFile):
    print("Searching from %s to %s (interval: %s)" % (
        f"{startNumber:,d}".replace(",", "."), f"{endNumber:,d}".replace(",", "."),
        f"{(endNumber - startNumber):,d}".replace(",", ".")), file=logfile)

## With skip one after prime - revised version

for currentPrimeSearch in range(6, 7):
    TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
currentNumber = %s
while currentNumber <= %s:
    if isPrimeSearch.checkForPrime%s(currentNumber) == True:
        primeCounter +=  1
        currentNumber += 2
    else:        
        currentNumber += 1
''' % (startNumber, endNumber, currentPrimeSearch)
    timeToRun = round(timeit.timeit(stmt=TEST_CODE, number=1), 4)
    print("CheckForPrime%s (wsa2): %s" % (currentPrimeSearch, timeToRun))
    if (useLogFile):
        print("CheckForPrime%s (wsa2): %s" % (currentPrimeSearch, timeToRun),
              file=logfile)

## With for loop
for currentPrimeSearch in range(6, 7):
    TEST_CODE = '''
import isPrimeSearch
primeCounter = 0
for currentNumber in range(%s, %s):
    if isPrimeSearch.checkForPrime%s(currentNumber) == True:
        primeCounter +=  1
''' % (startNumber, endNumber, currentPrimeSearch)
    # print(TEST_CODE)
    timeToRun = round(timeit.timeit(stmt=TEST_CODE, number=1), 4)
    print("CheckForPrime%s (for1): %s" % (currentPrimeSearch, timeToRun))
    if (useLogFile):
        print("CheckForPrime%s (for1): %s" % (currentPrimeSearch, timeToRun),
              file=logfile)

logfile.close()  # ordinary file object
