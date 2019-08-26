# SearchForPrimeNumbers
Python code to search for prime numbers.

There are several different search methods for primes in the file "isPrime.py". The default is isprime(), which upon testing have been found to be the fastest overall (but not for low numbers below 1.000.000 or so).

The code is split into a server and a client part. Both are assumed to run together as one program, with a MySQL database behind it. The server part serves up intervals to be searched for primes and keeps track of current searches, found primes, etc.. The client part searches for the primes.
