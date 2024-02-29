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



# 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

# git remote set-url origin https://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@github.com/Sevenwings26/django_crm_project


# git credential approve << EOF
# url=https://github.com
# username=Sevenwings26
# password= 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
# EOF