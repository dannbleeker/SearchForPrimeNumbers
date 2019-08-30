# While jump to next prime - should e faster... but is not... hm more test

# Tested with 0,10000 interval
#CheckForPrime1: 0.1651902219891781
#CheckForPrime2: 0.1480777050019242
#CheckForPrime3: 0.14326046900532674
#CheckForPrime4: 1.6963655020081205

# Tested with 1000000,2000000 interval
#CheckForPrime1: 67.9007603909995
#CheckForPrime2: 103.35641144200054
#CheckForPrime3: 99.4001969910023
#CheckForPrime4: more than 12 hours.... stoppped after that

# Tested with 100000, 200000 interval
#CheckForPrime1: 1.0779051249992335
#CheckForPrime2: 1.4072657409997191
#CheckForPrime3: 1.3987777099973755
#CheckForPrime4: 221.99308175299666

def checkForPrime1(possiblePrimeNumber):
    """ Checkes if a number is a prime. Returns true or false """
    if not isinstance(possiblePrimeNumber, int):
        return False
    
    if int(str(possiblePrimeNumber)[-1]) in (2,4,5,6,8,0):
        if possiblePrimeNumber == 2:
            return True
        elif possiblePrimeNumber == 5:
            return True
        return False
    if possiblePrimeNumber == 1:
        return False
    # Vi antager at der kun skal testes for division med ulige tal, da all der kan divideres med et lige tal er frasorteret ovenfor som ikke prime
    # Since the number candidate at this stage is not divvisble by five (numbers ending in five is not a prime and have been skipped earlier), we want to only test for uneven numers that are nto five - hence the different loops
    if possiblePrimeNumber < 25:
        for currentDivider in range (3, round(possiblePrimeNumber ** 0.5)+1,10):
            if possiblePrimeNumber % currentDivider == 0:
                return False
    else:
        for currentDivider in range (3, round(possiblePrimeNumber ** 0.5)+1,10):
            if possiblePrimeNumber % currentDivider == 0:
                return False
            
        for currentDivider in range (7, round(possiblePrimeNumber ** 0.5)+1,10):
            if possiblePrimeNumber % currentDivider == 0:
                return False
        
        for currentDivider in range (19, round(possiblePrimeNumber ** 0.5)+1,10):
            if possiblePrimeNumber % currentDivider == 0:
                return False
                
        for currentDivider in range (11, round(possiblePrimeNumber ** 0.5)+1,10):
            if possiblePrimeNumber % currentDivider == 0:
                return False
            
    # All numbers have been checked - no divisor with mod 0 ==> it is a prime
    return True

def checkForPrime2(possiblePrimeNumber):
    """ Checkes if a number is a prime. Returns true or false """
    if int(str(possiblePrimeNumber)[-1]) in (2,4,5,6,8,0):
        if possiblePrimeNumber == 2:
            return True
        elif possiblePrimeNumber == 5:
            return True
        return False
    
    for currentDivider in range (2, round(possiblePrimeNumber ** 0.5)+1):
        if possiblePrimeNumber % currentDivider == 0:
            return False
    
    return True

def checkForPrime3(possiblePrimeNumber):
    """ Checkes if a number is a prime. Returns true or false """
    
    for currentDivider in range (2, round(possiblePrimeNumber ** 0.5)+1):
        if possiblePrimeNumber % currentDivider == 0:
            return False
    
    return True

def checkForPrime4(possiblePrimeNumber):
    """ Checkes if a number is a prime. Returns true or false """
    
    for currentDivider in range (2, round(possiblePrimeNumber * 0.5)+1):
        if possiblePrimeNumber % currentDivider == 0:
            return False
    
    return True


def checkForPrime5(possiblePrimeNumber):

    if not isinstance(possiblePrimeNumber, int):
        return False
    
    # Corner cases 
    if (possiblePrimeNumber <= 1) : 
        return False
    if (possiblePrimeNumber <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (possiblePrimeNumber % 2 == 0 or possiblePrimeNumber % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= possiblePrimeNumber) : 
        if (possiblePrimeNumber % i == 0 or possiblePrimeNumber % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def checkForPrime6(possiblePrimeNumber):

    if not isinstance(possiblePrimeNumber, int):
        return False
    
    # Corner cases 
    if (possiblePrimeNumber <= 1) : 
        return False
    if (possiblePrimeNumber <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (possiblePrimeNumber % 2 == 0 or possiblePrimeNumber % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= possiblePrimeNumber) : 
        if (possiblePrimeNumber % i == 0 or possiblePrimeNumber % (i+6) == 0 or possiblePrimeNumber % (i+12) == 0 or possiblePrimeNumber % (i+18) == 0 or possiblePrimeNumber % (i+24) == 0
        or possiblePrimeNumber % (i + 2) == 0 or possiblePrimeNumber % (i + 2 +6) == 0 or possiblePrimeNumber % (i + 2 +12) == 0 or possiblePrimeNumber % (i + 2 +24) == 0 or possiblePrimeNumber % (i + 2 +30) == 0) : 
            return False
        i = i + 36
  
    return True