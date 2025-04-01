import sqlite3

var = 2
var2 = 4
var3 = 53

# DISCLAIMER: Table inserts done in form:
# (attemptNum, shipHealth, totalFuel, fuelAmtUsed, fuelRemaining, totalWeight, passengersAmt, cargoWght, attemptTime, attemptSuccess, failureReason)

# Connect to your SQL database, make sure you are using the exact file name
conn = sqlite3.connect('lunarlander.db')

# Creates a cursor object to execute SQL commands
cursor = conn.cursor()

# cursor.execute takes in any standard SQL query, so use it to select, delete, insert, etc.
#cursor.execute('''INSERT INTO Attempts VALUES (2, 100, 23, 34, 65, 400, 180, 220, 44.0, NULL, NULL)''')

# We can also use variables, so say if we wanted to insert the variable for fuel, we would use this syntax
#cursor.execute("INSERT INTO Attempts VALUES (?, ?, ?)", (var, var2, var3))

# Commit the changes and close the connection
conn.commit()

cursor.execute('SELECT * FROM Attempts')

# Print all rows of table in previous query, assuming the previous query was a select query
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
"""Can execute multiple statements in """ 