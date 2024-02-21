# connect project to database  

# pip install mysql
# pip install mysql-connector 
# pip install mysql-connector-python 


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "arowosola1449",
)

# connect to database 
mycusor = database.cursor()

# create database 
# mycusor.execute('CREATE DATABASE focalco')

print('Created database')