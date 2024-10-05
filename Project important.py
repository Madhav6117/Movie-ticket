import csv
import os
if not os.path.exist("Movies.csv"):
    f=open("Movies.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Sl no","Movie Name"])
    f=open("Shows.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Show no","Show timings"])
    f=open("Tickets.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["        ","        |___________|      "])
    csvw.writerow(["        ","        "])
    csvw.writerow(["        ","        "])
    csvw.writerow(["---J--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---I--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---H--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---G--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---F--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---E--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---D--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---C--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["        ","        "])
    csvw.writerow(["---B--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    csvw.writerow(["---A--- ","[01][02][03][04][05]      [06][07][08][09][10]"])
    
def mov_in:
    
    f=open("Movies.csv","a+")
    l=[]
    n=int(input("Enter number of movies to be added: "))
    for i in range(n):
        m=input("Enter movie name: ")
        l.append(m)
    csvw=csv.writer(f)
