#!/usr/bin/env python3

import datetime
import primeSearchServer
import isPrimeSearch
import sys
    
def main():
    
    PrimeServerConnection = primeSearchServer.primeServer()
    
    searchInterval=1000
    forceUseOfIncompleteIntervals = False
    
    if(len(sys.argv) > 1):
        if(sys.argv[1].isnumeric() and int(sys.argv[1]) > 0): #and sys.argv[1] >0)
            searchInterval = int(sys.argv[1])
        elif(sys.argv[1] == "status"):
            print("Number of primes found: %s" % (f"{PrimeServerConnection.returnTotalNumberOfPrimesFound():,d}".replace(",",".")))
            print("Biggest prime found: %s" % (f"{PrimeServerConnection.returnHighestPrimeFound():,d}".replace(",",".")))
            print("Number of unfinished intervals: %s" % ((f"{PrimeServerConnection.returnUnfinishedIntervals():,d}".replace(",","."))))
            return
        elif(sys.argv[1] == "-?"):
            print("useIntervals forces to use any open intervals on the server")
            print("status gives a status from the server")
            print("follow command with a number, and that is the interval of primes beeing searched")
        elif(sys.argv[1] == "useIntervals"):
            forceUseOfIncompleteIntervals = True

    (startSearchAt, endSearchAt) = PrimeServerConnection.returnSearchInterval(int(searchInterval), forceUseOfIncompleteIntervals)

    primeCounter = 0
    startTime = datetime.datetime.now()
    print("Search for primenumbers\nStarting at: %s\n" % startTime.strftime("%Y-%m-%d %H:%M:%S"))
    print ("Searching from %s to %s (interval: %s)" % (f"{startSearchAt:,d}".replace(",","."), f"{endSearchAt:,d}".replace(",","."), f"{(endSearchAt-startSearchAt):,d}".replace(",",".")))

    #searchRange = endSearchAt - startSearchAt

    completionRate = 0
    sys.stdout.write("\r"+str(completionRate)+"% completed")
    sys.stdout.flush()
    
    for currentNumber in range(startSearchAt, endSearchAt):
        if isPrimeSearch.checkForPrime5(currentNumber) == True:
            primeCounter += 1

            PrimeServerConnection.returnPrimeFound(currentNumber)
          
                       
                # progressBar
        if(completionRate < int(round(((currentNumber-startSearchAt)/(endSearchAt-startSearchAt))*100,0))):
            completionRate = int(round(((currentNumber-startSearchAt)/(endSearchAt-startSearchAt))*100,0))
            #print("%s%%" % completionRate )
            sys.stdout.write("\r"+str(completionRate)+"% completed")
            sys.stdout.flush()

    sys.stdout.write("\r100% completed")
    sys.stdout.flush()

    PrimeServerConnection.returnSearchedInterval(startSearchAt, endSearchAt)

    del PrimeServerConnection

    # Output to make it more readable
    endTime = datetime.datetime.now()
    print("\n\nStarting at: %s" % startTime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at: %s" % endTime.strftime("%Y-%m-%d %H:%M:%S"))
    timedelta = endTime-startTime
    #print ("Running time: %s seconds" % timedelta.seconds)
    print ("Running time: %s minutes %s seconds" % (int(timedelta.seconds/60), (timedelta.seconds % 60)))
    print ("Searched from %s to %s (interval: %s)" % (f"{startSearchAt:,d}".replace(",","."), f"{endSearchAt:,d}".replace(",","."), f"{(endSearchAt-startSearchAt):,d}".replace(",",".")))
    print ("Number of primes: %s (%s%%)" % (f"{primeCounter:,d}".replace(",","."), round(primeCounter/(endSearchAt-startSearchAt),5)))

    if primeCounter > 0:
        print ("Seconds per prime: %s" % round(timedelta.seconds/primeCounter,6) )


if __name__ == "__main__":
    main()
