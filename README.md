# SearchForPrimeNumbers
Python code to search for prime numbers.

There are several different search methods for primes in the file "isPrime.py". The default is isprime(), which upon testing have been found to be the fastest overall (but not for low numbers below 1.000.000 or so).

The code is split into a server and a client part. Both are assumed to run together as one program, with a MySQL database behind it. The server part serves up intervals to be searched for primes and keeps track of current searches, found primes, etc.. The client part searches for the primes.

Note that an MySQL (or MariaDB) needs to be installed. A database needs to be avaiable for the script as well as a user. If you want to run this from other computers than the database is hosted, be aware that you need to enable access to MySQL from other adresses on your network. This is both an issue for the specefic user (and/or datbase element) as well as for MySQL itself. Ensure that the mysql config file is correct with bind-adress= 0.0.0.0 and that the user have rights to logon from more than localhost. MySQL config is usually in /etc/mysql/my.cnf or thereabout.

Enjoy :-)
