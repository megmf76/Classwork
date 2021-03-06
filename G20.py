# File: dbReadFromFile.py
# Small example to demonstrate how to read input from a CSV file and store
# that info into the database

import sqlite3
import csv
import numpy as np
import matplotlib.pyplot as plt

# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')

# IMPORT DATA OF URBAN POPULATION (% of total population) #
# Create a cursor
cursor = conn.cursor()

# Drop the table if it exists
sql = '''drop table if exists urban10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a table called urban10
sql = '''create table urban10(
    Country_Name text,
    Country_Code text,
    UrbanPop real)'''
    
# Use the cursor to execute the statement
cursor.execute(sql)

# Output to screen so user knows what is going on
print("Inputting the following information into the database: ")

# Open a file for reading using csv.reader 
with open ('Desktop/FinalFinal/UrbanPopulation.csv','rb') as dataFile:
    reader = csv.reader(dataFile)
    reader.next()
    for ctyInfo in reader: # for each row in reader...
        # Find the length (i.e. how many elements in the list)
        numElements = len(ctyInfo)
        print(ctyInfo)
        Country_Name = ctyInfo[0]
        Country_Code = ctyInfo[1]
        UrbanPop = ctyInfo[2]
        sql = '''insert into urban10
             (Country_Name, Country_Code, UrbanPop)
             values
             (:st_ct, :st_ctcd, :ub)'''
             # These values are "named parameters" (like place holders)
             # Tells the SQLite library that something will be substituted here
        
        # Use the cursor to execute the statement
        # Here, a dictionary has been added for the named parameters and the items
        # to be inserted
        cursor.execute(sql,{'st_ct':Country_Name,'st_ctcd':Country_Code,'ub':UrbanPop})
        
        # Commit. Telling SQLite to save the new data. The data would be lost otherwise.
        conn.commit()
        
cursor.close() 
    
# IMPORT DATA OF GDP PER CAPITA (CURRENT US $)
 
# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')
  
# Create a cursor
cursor = conn.cursor()

# Drop the table if it exists
sql = '''drop table if exists GDPpc10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a table called GDpc10
sql = '''create table GDPpc10(
    Country_Name text,
    Country_Code text,
    GDPpc real)'''
    
# Use the cursor to execute the statement
cursor.execute(sql)

# Output to screen so user knows what is going on
print("Inputting the following information into the database: ")

# Open a file for reading using csv.reader
with open('Desktop/FinalFinal/GDP_PER_CAPITA.csv','rb') as dataFile:
    reader = csv.reader(dataFile)
    reader.next()
    for ctyInfo in reader: # for each row in reader
        # Find the length (number of elements in list)
        numElements = len(ctyInfo)
        print(ctyInfo)
        Country_Name = ctyInfo[0]
        Country_Code = ctyInfo[1]
        GDPpc = ctyInfo[2]
        sql = '''insert into GDPpc10
             (Country_Name, Country_Code, GDPpc)
             values
             (:st_ct, :st_ctcd, :gpc)'''
            # These values are "named parameters"
            # Tells the SQLite library that something will be substituted here
        
        # Use the cursor to execute the statement
        # A dictionary has been added for the named parameters and the items to be inserted
        cursor.execute(sql,{'st_ct':Country_Name,'st_ctcd':Country_Code,'gpc':GDPpc})
        
        # Commit - telling SQLite to save the new data
        conn.commit()
        
# Use the cursor to close the connection to the database
cursor.close()

# Create trades10: Country_Name,Country_Code,Imports,Exports,GDP #

# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()

# Drop the table if it exists
sql = '''drop table if exists trades10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a table called trades10
sql = '''create table trades10(
    Country_Name text,
    Country_Code text,
    Imports real,
    Exports real,
    GDP real)'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Output to screen so user knows what is going on
print("Inputting the following information into the database: ")

# Open a file for reading using csv.reader
with open ('Desktop/FinalFinal/TradeOpenness.csv','rb') as dataFile:
    reader = csv.reader(dataFile)
    reader.next()
    for ctyInfo in reader: # for each row in reader
        # Find the lenght (number of elements in the list)
        numElements = len(ctyInfo)
        print(ctyInfo)
        Country_Name = ctyInfo[0]
        Country_Code = ctyInfo[1]
        Exports = ctyInfo[2]
        Imports = ctyInfo[3]
        GDP = ctyInfo[4]
        sql = '''insert into trades10
             (Country_Name, Country_Code, Exports, Imports, GDP)
             values
             (:st_ct, :st_ctcd, :ex, :im, :gdp)'''
             # These values are "named parameters" (like place holders)
             # Tells the SQLite library that something will be substituted here
    
        # Use the cursor to execute the statement
        # Here, a dictionary has been added of the named parameters and the items
        # to be inserted.
        cursor.execute(sql, {'st_ct':Country_Name, 'st_ctcd':Country_Code, 'ex':Exports, 'im':Imports, 'gdp':GDP})
    
        # Commit. Telling SQLite to save the new data. The data would be lost otherwise.
        conn.commit()
    
# Use the cursor to close the connection to the database
cursor.close()

# Import data of power consumption: Country_Name, Country_Code, Power #

# Create a connection to the database.
conn = sqlite3.connect('mydatabase.db')

# Create a cursor. 
cursor = conn.cursor()


# Drop the table if it exists
sql = '''drop table if exists power10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a table called power10
sql = '''create table power10(
    Country_Name text,
    Country_Code text,
    Power real)'''
    
# Use the cursor to execute the statement
cursor.execute(sql)

# Output to screen so user knows what is going on
print("Inputting the following information into the database: ")

# Open a file for reading using csv.reader [See above for file contents]
with open('Desktop/FinalFinal/PowerConsumption.csv', 'rb') as dataFile:
    reader = csv.reader(dataFile)
    reader.next()
    for ctyInfo in reader: # for each row in reader...
        # Find the length (i.e. how many elements in the list) (should be 3)
        numElements = len(ctyInfo)
        print(ctyInfo)
        Country_Name = ctyInfo[0]
        Country_Code = ctyInfo[1]
        Power = ctyInfo[2]
        sql = '''insert into power10
             (Country_Name, Country_Code, Power)
             values
             (:st_ct, :st_ctcd, :pw)'''
             # These values are "named parameters" (like place holders)
             # Tells the SQLite library that something will be substituted here
    
        # Use the cursor to execute the statement
        # Here, a dictionary has been added of the named parameters and the items
        # to be inserted.
        cursor.execute(sql, {'st_ct':Country_Name, 'st_ctcd':Country_Code, 'pw':Power})
    
        # Commit. Telling SQLite to save the new data. The data would be lost otherwise.
        conn.commit()

# Use the cursor to close the connection to the database, now that we're done.
cursor.close()

# Import employment.csv: contain a check constraint as extra credit

# Create a connection to the database.
conn = sqlite3.connect('mydatabase.db')

# Create a cursor. 
cursor = conn.cursor()

#drop employment10 if it have already been created 
sql = '''drop table if exists employment10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a table called employment10 with check_constraint that Agriculture Industry and Services must in 0 between 100.
sql = '''create table employment10(
    Country_Name text NOT NULL,
    Country_Code text NOT NULL,
    Agriculture real NOT NULL,
    Industry real NOT NULL,
    Services real NOT NULL,
    CONSTRAINT chk_Person CHECK(Agriculture>0 AND Agriculture<100 AND Industry>0 AND Industry<100 AND Services >0 AND Services<100)
    )'''
    
    
cursor.execute(sql)

#import Employment.csv into table employment
with open('Desktop/FinalFinal/Employment.csv', 'rb') as dataFile:
    reader = csv.reader(dataFile)
    reader.next()
    for ctyInfo in reader: # for each row in reader...
        # Find the length (i.e. how many elements in the list) (should be 3)
        numElements = len(ctyInfo)
        print(ctyInfo)
        Country_Name = ctyInfo[0]
        Country_Code = ctyInfo[1]
        Agriculture  = ctyInfo[2]
        Industry = ctyInfo[3]
        Services = ctyInfo[4]
        sql = '''insert into employment10
             (Country_Name, Country_Code, Agriculture, Industry, Services )
             values
             (:st_ct, :st_ctcd, :Ar, :In, :Se)'''
        cursor.execute(sql, {'st_ct':Country_Name, 'st_ctcd':Country_Code, 'Ar':Agriculture, 'In':Industry, 'Se':Services})  
        # Commit. Telling SQLite to save the new data. The data would be lost otherwise.
        conn.commit()
        
cursor.close()  

# Explore urbanization topic #

# Create a connection to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()  

# Query: Urbanization vs. Economic development

sql = '''select Country_Name, UrbanPop from urban10
        order by UrbanPop'''

# Use the cursor to execute the statement
results=cursor.execute(sql)

# Save data of GDP per capita
urban = results.fetchall()

# Bar chart for urbanization
ind = np.arrange(20)
width = 0.35

p1=plt.bar(ind,zip(*urban)[1])
plt.ylabel('Urban population as percentage of total population')
plt.title('Urbanization of G20')
plt.xticks(ind+width/2.,zip(*urban)[0],rotation=30)
plt.yticks(np.arrange(0,110,10))
plt.show()

# Query: GDP per capita
sql = '''select Country_Name, GDPpc from GDPpc10
         order by GDPpc'''

# Use the cursor to execute the statement
results=cursor.execute(sql)

# Save data of GDP per capita
gdppc = results.fetchall()

# Bar chart for GDP per capita to find a boundary to dividing into two groups

ind = np.arange(20) 
width = 0.35

p1=plt.bar(ind, zip(*gdppc)[1])
plt.ylabel('GDP per capita in current US $')
plt.title('GDP per capita of G20')
plt.xticks(ind+width/2., zip(*gdppc)[0],rotation=30)
plt.yticks(np.arange(0,1.1,0.1))
plt.show()

# Query
# Create table urbanpc10 by joining two tables of urban10 and GDPpc10

# Drop the table if it exists
sql = '''drop table if exists urbanpc10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Create a SQL statement to natural join urban data and GDP per capita data

sql = '''create table urbanpc10 as select * from urban10 natural join GDPpc10'''
         
cursor.execute(sql)

# Drop the table if it exists
sql = '''drop table if exists bot9'''

cursor.execute(sql)

# extract urban population of countries with bottom 9 GDP per capita and save
# it as a table
sql = '''create table bot9 as 
         select Country_Name, urbanPop, GDPpc from urbanpc10
         order by GDPpc ASC
         limit 9''' 
            
# Use the cursor to execute the statement
cursor.execute(sql)

# extract urban population of countries with bottom 9 GDP per capita
sql = '''select Country_Name, urbanPop, GDPpc from bot9
         order by GDPpc ASC''' 
            
# Use the cursor to execute the statement
results = cursor.execute(sql)

# Save % of urban population and GDP per capita
urban_bot = results.fetchall()

# Query
# extract urban population of countries with top 11 GDP per capita:
# extract set difference between the full set and the set of bottom 9

sql = '''select Country_Name, urbanPop, GDPpc from urbanpc10
         except
         select Country_Name, urbanPop, GDPpc from bot9
'''

# Use the cursor to execute the statement
results = cursor.execute(sql)

# Save % of urban population and GDP per capita
urban_top = results.fetchall()

##########################
# PLOTS

# generate a scatter plot between urban pop and GDP per capita
plt.scatter(zip(*urban_top)[2], zip(*urban_top)[1], color='r',s=100)
plt.scatter(zip(*urban_bot)[2], zip(*urban_bot)[1], color='g',s=100)
plt.ylabel('Urban population, percentage of total population')
plt.xlabel('GDP per capita in current US $')
plt.title('Urbanization vs GDP per capita by economic development')
plt.yticks(np.arange(25,105,10))
plt.xticks(np.arange(1000,53000,5000))
plt.legend(['Top 11', 'Bottom 9'], loc='lower right')

plt.show()

#Investigate the relationship between employment for each industry and urbanization 

conn = sqlite3.connect('mydatabase.db')

# Create a cursor. 
cursor = conn.cursor()

# Query
#Create a table including employment for each industry and urban population

sql = '''drop table if exists em10'''
cursor.execute(sql)

sql = '''create table em10 as select Country_name, Agriculture, Industry, Services,UrbanPop from employment10 natural join urban10'''
cursor.execute(sql)

# Query
# Select data from em10 sort them by UrbanPop so that we can compare 
# urbanization and industry distribution 

sql='''SELECT * FROM em10 ORDER BY UrbanPop '''
results3 = cursor.execute(sql)
Employment2 = results3.fetchall()

#plot the bar chart

ind = np.arange(len(Employment2))
width = 0.2
opacity = 0.4
error_config = {'ecolor': '0.3'}
p1=plt.bar(ind, zip(*Employment2)[1],  width, color='b', alpha=opacity, error_kw=error_config, label='Agriculture')
p2=plt.bar(ind+width, zip(*Employment2)[2],  width, capsize=10,color='r',alpha=opacity, error_kw=error_config,label='Industry')
p3=plt.bar(ind+2*width, zip(*Employment2)[3],  width, capsize=10,color='y',alpha=opacity, error_kw=error_config,label='Service')
plt.ylabel('Employment ratio')
plt.title('Labor structure of G20')
plt.xticks(ind+1.5*width, zip(*Employment2)[0],rotation=60)
plt.yticks(np.arange(0,90,5))
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

cursor.close()

# Explore the relationship between power consumption and Urbanization #

conn = sqlite3.connect('mydatabase.db')

# Create a cursor. 
cursor = conn.cursor()

sql = '''drop table if exists po10'''

# Use the cursor to execute the statement
cursor.execute(sql)

# Query
# Create a table em10 contains urban population and power consumption

sql = '''create table po10 as select Country_Name,Industry, UrbanPop,Power from em10 natural join power10'''
cursor.execute(sql)

sql='''SELECT * FROM po10'''
results1 = cursor.execute(sql)
Power1 = results1.fetchall()
plt.scatter(zip(*Power1)[3], zip(*Power1)[2], color='r',s=100)
plt.ylabel('Urban population, percentage of total population')
plt.xlabel('Power Consumption')
plt.title('Urbanization vs Power Consumption')
plt.yticks(np.arange(25,90,10))
plt.xticks(np.arange(0,17000,1000),rotation=90)
plt.show()

# Explore the relationship between Tradeopenness and Urbanization #

# Query
# Create a SQL statement to print out all the trade openness in the database
sql = '''select Country_Name, (Exports + Imports)/GDP AS Trade_Openness
      from trades10'''

# Use the cursor to execute the statement
# The SQL statement generates some results so the variable "results" is
# created to store the results
results = cursor.execute(sql)

# Finally the fetchall() function is used to store all the trade openness index
# into a new variable, "trade_openness"
trade_openness = results.fetchall()

# Query
# Calculate trade openness and compare it with urbanization
sql = '''select trades10.Country_Name, urban10.UrbanPop, 
        (trades10.Exports + trades10.Imports)/trades10.GDP AS Trade_Openness 
        from trades10 INNER JOIN urban10
        on urban10.Country_Name=trades10.Country_Name'''
        
results1 = cursor.execute(sql)

urban_trade = results1.fetchall()

# Use the cursor to close the connection to the database, now that we're done
cursor.close()

# Generate a bar chart of trade openness index
ind = np.arange(20)
width = 0.35
p1=plt.bar(ind, zip(*trade_openness)[1])
plt.ylabel('Trade openness')
plt.title('Trade openness of G20')
plt.xticks(ind+width/2., zip(*trade_openness)[0],rotation=30)
plt.yticks(np.arange(0,1.1,0.1))
plt.show()

# Generate a scatter plot between trade openness and urbanization #
plt.scatter(zip(*urban_trade)[2], zip(*urban_trade)[1],s=80)
plt.xlabel('Trade openness index')
plt.ylabel('Urban population, percentage of total population')
plt.title('Trade openness vs Urbanization of G20')
plt.xticks(np.arange(0.2,1.1,0.1))
plt.yticks(np.arange(20,110,10))
plt.show()

# Use the cursor to close the connection to the database, now that we're done.
cursor.close()

