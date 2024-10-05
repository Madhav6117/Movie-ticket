import csv
import os
from prettytable import PrettyTable
if not os.path.exists("Movies.csv"):
    f=open("Movies.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Sl no","Movie Name"])
    f=open("Shows.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Show no","Show timings"])
    
def mov_in():
    Mcount=1
    with open ("Movies.csv","a",newline="") as f:
        n=int(input("Enter number of movies to be added: "))
        csvw=csv.writer(f)
        for i in range(1,n+1):
            m=input("Enter movie name: ")
            csvw.writerow([Mcount,m])
            Mcount+=1
            fm=open(f"{m}_tickets.txt","w")
            fm.write("         |______________________________________|         \n\n\n---J---[01][02][03][04][05]      [06][07][08][09][10]\n---I---[01][02][03][04][05]      [06][07][08][09][10]\n---H---[01][02][03][04][05]      [06][07][08][09][10]\n---G---[01][02][03][04][05]      [06][07][08][09][10]\n---F---[01][02][03][04][05]      [06][07][08][09][10]\n---E---[01][02][03][04][05]      [06][07][08][09][10]\n---D---[01][02][03][04][05]      [06][07][08][09][10]\n---C---[01][02][03][04][05]      [06][07][08][09][10]\n---B---[01][02][03][04][05]      [06][07][08][09][10]\n---A---[01][02][03][04][05]      [06][07][08][09][10]")

def show_in():
    global Scount
    f=open("Shows.csv","a+",newline='')
    n=int(input("Enter number of shows to be added: "))
    csvw=csv.writer(f)
    for i in range(n):
        m=input("Enter show timing: ")
        csvw.writerow([Scount,m])
        Scount+=1

def book():
    table=PrettyTable()
    with open("Movies.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        table.field_names = headers
        for row in reader:
            table.add_row(row)
    print(table) 
