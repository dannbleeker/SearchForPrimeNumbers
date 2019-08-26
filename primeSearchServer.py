""" Class that works as the primeServer - serves up intervals to search for primes """
#sudo apt install python3-mysqldb
import MySQLdb

class primeServer:
    
    def __init__(self):
        self._db_connection =  MySQLdb.connect(host="10.0.0.28",
                     user="username",
                     passwd="password",
                     db="mysqlsystemuser")

        self._db_cur = self._db_connection.cursor()
        
        self._createTablesIfMissing()
        
        self._cleanUpDatabase()
        
    def __del__(self):
        self._db_connection.close()
        
    def _createTablesIfMissing(self):
        
        self._db_cur.execute("show tables like 'primeSearches'")
        if self._db_cur.rowcount == 0:
            
        
            sqlToRun = """
CREATE TABLE `primeSearches` (
  `StartNumber` bigint(20) NOT NULL,
  `EndNumber` bigint(20) NOT NULL,
  `Startdate` timestamp NOT NULL DEFAULT current_timestamp(),
  `Completed` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
            self._db_cur.execute(sqlToRun)
            self._db_connection.commit()
            
            sqlToRun = """     
ALTER TABLE `primeSearches`
  ADD UNIQUE KEY `EndNumber` (`EndNumber`),
  ADD UNIQUE KEY `StartNumber` (`StartNumber`);
"""
            self._db_cur.execute(sqlToRun)
            self._db_connection.commit()
        
        self._db_cur.execute("show tables like 'primes'")
        if self._db_cur.rowcount == 0:


            sqlToRun = """
CREATE TABLE `primes` (
  `prime` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
            self._db_cur.execute(sqlToRun)
            self._db_connection.commit()
        
            sqlToRun = """
ALTER TABLE `primes`
  ADD UNIQUE KEY `prime` (`prime`);
"""
            self._db_cur.execute(sqlToRun)
            self._db_connection.commit()
        
        return True
    
    def _cleanUpDatabase(self):
        # First ensure that the ranges start from 1
        self._db_cur.execute("SELECT DISTINCT MIN(StartNumber) FROM primeSearches")
        
        if self._db_cur.rowcount == 0:
            return
                 
        firstStartNumber = self._db_cur.fetchone()

        if firstStartNumber[0] > 2:
            self._db_cur.execute("INSERT INTO primeSearches (StartNumber,EndNumber) VALUES (%s, %s)" % (2,firstStartNumber(0)))
            self._db_connection.commit()
        
        # Second ensure that there is no numbers not covered by an interval (up untill the highest number in the intervals)
        self._db_cur.execute("SELECT DISTINCT leftTable.EndNumber+1 FROM primeSearches as leftTable LEFT JOIN primeSearches as rightTable ON leftTable.EndNumber+1 = rightTable.StartNumber WHERE rightTable.StartNumber is null AND leftTable.EndNumber not IN (SELECT max(EndNumber) FROM primeSearches)")

        if self._db_cur.rowcount == 0:
            pass

            # No non allocated intervals
        else:
            startNumbersOfNewIntervals = self._db_cur.fetchall()
            
            for rowOfNewStartNumbers in startNumbersOfNewIntervals:
                
                # find end numbers
                self._db_cur.execute("SELECT DISTINCT MIN(StartNumber)-1 FROM primeSearches WHERE StartNumber > %s" % (rowOfNewStartNumbers[0]))
                
                rowWithEndNumbers = self._db_cur.fetchone()
                
                self._db_cur.execute("INSERT INTO primeSearches (StartNumber,EndNumber) VALUES (%s, %s)" % (rowOfNewStartNumbers[0],rowWithEndNumbers[0]))
                
                self._db_connection.commit()
          
                # Next unassigned interval       
                
    
    
    def returnSearchInterval(self, intervalSize = 10000, forceUseOfOldIntervals = False):
        
        if not isinstance(intervalSize, int):
            intervalSize = 1000
        
        intervalSize = round(intervalSize,0)
        
        sqlToRun = "SELECT * FROM `primeSearches` WHERE completed = 0 AND DATEDIFF(Startdate,NOW()) < 0"
        
        if(forceUseOfOldIntervals):
            sqlToRun = "SELECT * FROM `primeSearches` WHERE completed = 0"
            #print ("using forced search")
        
        ## handle workload not returned - dato for returnering 1 døgn
        self._db_cur.execute(sqlToRun)
        if self._db_cur.rowcount > 0:
            # Earlier incomplete search should be handed out again
            # random order
            
            sqlReturn = self._db_cur.fetchone()
            self.startNumber = sqlReturn[0]
            self.endNumber = sqlReturn[1]
            #print("debug UseEarlierInterval: %s %s" % (self.startNumber, self.endNumber))
            #Update timestamp for handout
            self._db_cur.execute("UPDATE primeSearches SET Startdate = CURRENT_TIMESTAMP() WHERE StartNumber = %s AND EndNumber = %s" % (self.startNumber, self.endNumber))
            self._db_connection.commit()

            # Skip ahead if some primes have been handed in
            # PROBLEMEt ER AT INTERVALLET DER BLEV FUNDET SKA_L _REDUCERES, completed og et nyt laves
            self._db_cur.execute("SELECT max(prime) from primes WHERE prime < %s AND prime > %s" % (self.endNumber, self.startNumber))
            sqlReturn = self._db_cur.fetchone()

            if not sqlReturn[0] == None:
 
                self._db_cur.execute("UPDATE primeSearches SET Completed = 1, EndNumber=%s WHERE StartNumber = %s AND EndNumber = %s AND Completed = 0" % (sqlReturn[0], self.startNumber, self.endNumber))
                self._db_connection.commit()
                # lav nyt interval
                self.startNumber = sqlReturn[0]+1
                self._db_cur.execute("INSERT INTO primeSearches (StartNumber,EndNumber) VALUES (%s, %s)" % (self.startNumber, self.endNumber))
                self._db_connection.commit()
                #print("start number adjusted: %s" % (self.startNumber))                
                if self.startNumber > self.endNumber:
                    self.startNumber = self.endNumber
            
        else:
            self._db_cur.execute("SELECT MAX(EndNumber)+1 FROM primeSearches")
            
            #print(self._db_cur.rowcount)
            sqlReturn = self._db_cur.fetchone()
            if self._db_cur.rowcount == 0 :
                #print("HER")
                self.startNumber = 2 #If we start from scratch
          
            else:
                #print(sqlReturn)
                self.startNumber = sqlReturn[0]
                if self.startNumber is None:
                    self.startNumber = 2

            self.endNumber = self.startNumber+intervalSize            
            self._db_cur.execute("INSERT INTO primeSearches (StartNumber,EndNumber) VALUES (%s, %s)" % (self.startNumber, self.endNumber))
            self._db_connection.commit()
            
        return (self.startNumber,self.endNumber)

    def returnSearchedInterval(self, StartNumber, EndNumber):
        #print("UPDATE primeSearches SET Completed = 1 WHERE StartNumber = %s AND EndNumber = %s" % (StartNumber, EndNumber))
        if not isinstance(StartNumber, int):
            return False
        
        StartNumber = round(StartNumber,0)
        
        if not isinstance(EndNumber, int):
            return False
        
        EndNumber = round(EndNumber,0)  
        
        self._db_cur.execute("UPDATE primeSearches SET Completed = 1 WHERE StartNumber = %s AND EndNumber = %s" % (StartNumber, EndNumber))
        self._db_connection.commit()
        
        return True

    def returnPrimeFound(self, foundPrimeNumber):
        
        if not isinstance(foundPrimeNumber, int):
            return False
        
        foundPrimeNumber = round(foundPrimeNumber,0)
        
        self._db_cur.execute("SELECT prime FROM primes WHERE prime = %s" % foundPrimeNumber)
        
        
        #print("SELECT prime FROM primes WHERE prime = %s" % foundPrimeNumber)
        #print("Rowcount: %s" % self._db_cur.rowcount)
        sqlReturn = self._db_cur.fetchone()
        
        if sqlReturn == None:

            try:
                self._db_cur.execute("INSERT INTO primes (prime) VALUES (%s)" % foundPrimeNumber)
                self._db_connection.commit()
            except:
                #print ("FEJL %s" % foundPrimeNumber)
                return False
                
        return True
    
    def returnHighestPrimeFound(self):
        self._db_cur.execute("SELECT MAX(prime) FROM primes")
        
        if self._db_cur.rowcount == 1 :
        
            sqlReturn = self._db_cur.fetchone()
        
            return sqlReturn[0]
        
        return None

    def returnTotalNumberOfPrimesFound(self):
        self._db_cur.execute("SELECT COUNT(*) FROM primes")
        
        if self._db_cur.rowcount == 1 :
        
            sqlReturn = self._db_cur.fetchone()
        
            return sqlReturn[0]
        
        return None
    
    def returnUnfinishedIntervals(self):
        self._db_cur.execute("SELECT COUNT(*) FROM primeSearches WHERE Completed = 0")
        
        if self._db_cur.rowcount == 1 :
        
            sqlReturn = self._db_cur.fetchone()
        
            return sqlReturn[0]
        
        return None
