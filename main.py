import sqlite3
###############Connect to database
#conn = sqlite3.connect('test.db')

#print ("Opened database successfully");


#######################Create a table
#import sqlite3

#conn = sqlite3.connect('test.db')
#print ("Opened database successfully");

##conn.execute('''CREATE TABLE ashlya
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
#         SALARY         REAL);''')
#print ("Table created successfully");

#conn.close()


###################################Insert Function

#conn = sqlite3.connect('test.db')
#print ("Opened database successfully");

#conn.execute("INSERT INTO ashlya (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

#conn.execute("INSERT INTO ashlya (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

#conn.execute('''INSERT INTO ashlya (ID,NAME,AGE,ADDRESS,SALARY) \
#    VALUES(3,'Bishal',16,'Dhangadhi',39000)''')
#conn.commit()
#print ("Records created successfully");
#conn.close()

###########################Display result from database
#conn = sqlite3.connect('test.db')
#cursor = conn.execute("SELECT id, name, address, salary from ashlya")
#for row in cursor:
 #  print ("ID = ", row[0])
 #  print ("NAME = ", row[1])
 #  print ("ADDRESS = ", row[2])
 #  print ("SALARY = ", row[3]), "\n"
#print ("Operation done successfully");
#conn.close()

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("UPDATE ashlya set SALARY = 25000.00 where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3]), "\n"

print ("Operation done successfully");
conn.close()


