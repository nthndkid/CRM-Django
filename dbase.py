# pip install my-sql-connector
# pip install my-sql-connector-python

import mysql.connector

# database connection
dbase = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = '',
)

# prepare a cursor object
cursorObj = dbase.cursor()

# create a database
cursorObj.execute("CREATE DATABASE crm_dbase")

print("Done!")