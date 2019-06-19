import os
a=os.path.exists('chinook.db')
print(a)
import sqlite3 as sql
vt = sql.connect('chinook.db')
im = vt.cursor()



print("""Welcome my database "chinook.db"
There are 11 tables in the chinook database and lots of information in it.For:\n
table names: 1
album names(by ascending): 2
composers from track:3
customers (specifying row and quantity):4
phone numbers accordung to country code:5
invoice info from-to: 6
for exit: 0
\n""")

def tablenames():
    im.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = im.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        print(table_name)
        
def orderAlbumsbyname():
    im.execute("SELECT Title FROM albums ORDER BY Title ASC;")
    liste=im.fetchall()
    for i in liste:
        print(i)
        
def findcomposerTracks(x):
      artist="SELECT TrackId,Name FROM tracks WHERE composer LIKE "+"'%"+x+"%';"
      im.execute(artist)
      liste = im.fetchall()
      for i in liste:
        print(i)
        
def findCustomers(x,y):
      customer="SELECT FirstName,LastName,Country FROM customers LIMIT "+x+" OFFSET "+y+";"
      im.execute(customer)
      liste = im.fetchall()
      for i in liste:
        print(i)
        
def findPhonenumbers(x):
      company="SELECT Phone,City FROM customers WHERE Phone GLOB '"+x+"*';"
      im.execute(company)
      liste = im.fetchall()
      for i in liste:
        print(i)

def invoicesInfo(x,y):
      invoice="SELECT BillingAddress, Total FROM invoices WHERE Total BETWEEN "+x+" and "+y+" ORDER BY Total;"
      im.execute(invoice)
      liste=im.fetchall()
      for i in liste:
        print(i)


transaction=int(input("Please select your transaction:"))

if transaction==1:
      print("Tables:")
      tablenames()
if transaction==2:
      print("Albums:")
      orderAlbumsbyname()
if transaction==3:
      a=input("insert artist name:")
      findartistAlbums(a)
if transaction==4:
      a=input("how many:")
      b=input("from row number:")      
      findCustomers(a,b)
if transaction==5:
      a=input("enter number with(+: )")
      findPhonenumbers(a)
      
if transaction==6:
      x=input("beginning from: ")
      y=input("ending from: ")
      invoicesInfo(x,y)
if transaction==0:
    print("Database is closing....")
    exit()
      
      
      
      

 
