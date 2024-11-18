import csv
import os
from datetime import date
from prettytable import PrettyTable
d={'A':12,'B':11,'C':10,'D':9,'E':8,'F':7,'G':6,'H':5,'I':4,'J':3}
if not os.path.exists("Movies.csv"):
    f=open("Movies.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Sl no","Movie Name"])
    f=open("Shows.csv","w")
    csvw=csv.writer(f)
    csvw.writerow(["Show no","Show","timings"])

def show_in():
    #global Scount
    f=open("Shows.csv","w",newline='')
    n=int(input("Enter number of shows to be added: "))
    csvw=csv.writer(f)
    csvw.writerow(["Show No.", "Name of movie", "Timing"])
    for i in range(n):
        name=input("Enter name of movie: ")
        timing=input("Enter show timing: ")
        fm=open(f"{str(i+1)}_tickets.txt","w")
        fm.write("            |___________________________________|    \n\n\n---J---[01][02][03][04][05]      [06][07][08][09][10]\n---I---[01][02][03][04][05]      [06][07][08][09][10]\n---H---[01][02][03][04][05]      [06][07][08][09][10]\n---G---[01][02][03][04][05]      [06][07][08][09][10]\n---F---[01][02][03][04][05]      [06][07][08][09][10]\n---E---[01][02][03][04][05]      [06][07][08][09][10]\n---D---[01][02][03][04][05]      [06][07][08][09][10]\n---C---[01][02][03][04][05]      [06][07][08][09][10]\n---B---[01][02][03][04][05]      [06][07][08][09][10]\n---A---[01][02][03][04][05]      [06][07][08][09][10]")

        csvw.writerow([i+1,name, timing])
    f.close()
def book():
    table = PrettyTable()
    tot_price=0
    table.field_names = ["Movie","Seats" ,"Price(rs)","GST"]
    choice="y"
    f=open("Shows.csv", 'r')
    csvr=csv.reader(f)
    for i in csvr:
        print(i[0], i[1], i[2])
    while choice.lower()=="y":
        shownum=input("Enter show number: ")
        
        with open('Shows.csv', 'r') as file1:
            reader1 = csv.DictReader(file1)
            for row in reader1:
                if row['Show No.'] == shownum:
                    movienn=(row['Name of movie'])
        s=open(f"{shownum}_tickets.txt", "r").read()
        print("SEATING ARRANGEMENT: ")
        print(s)
        s=s.splitlines()
        choice="y"
        if choice.lower()=='y':
            n=int(input("Enter number of tickets:"))
            row=input("Enter row: ")
            for z in range(n):
                seatnumber=input("Enter seat number: ")
                for i in s:
                    if row in i:
                        if seatnumber in i:
                            i=i.replace(seatnumber, "  ")
                            s[d[row]]=i
                            g=open(f"{shownum}_tickets.txt", "w")
                            for i in range(len(s)):
                                g.write(s[i]+'\n')
                            g.close()
                            print(f"Seat {seatnumber} Successfully booked")
                            table.add_row([movienn,(row+str(seatnumber)),200,36])
                            tot_price+=236
                        else:
                            print("Sorry the seat is already booked.") 
                                          
                    else:
                        pass
        else:
            pass
        print(".\n.\n.\n Generating bill")

        with open('tname.txt','r') as reaad:
            sss=reaad.read()
            sname=str(sss)
        billamnt=0
        user=input("Customer name:")
        no=int(input("Mobile number:"))
        billp=f'\n\n**************************************************************\n                    |{sname}|\n  >name:{user}\n  >contactno:{no}\n  >date:{date.today()}\n**************************************************************\n\n{table}\n                 grand total:{str(tot_price)+"₹"}\n\n Enjoy the show!!!\n**************************************************************'
        print(billp)
        with open(f'mticket_{no}.txt','w',encoding="utf-8") as billt:
            billt.write(billp)
            billt.close()
            print(f"Your bill has been saved in your system as mticket_{no}.txt")
        choice=""
def setname():
    tname=input("Enter Theatre name:")
    print(f"Theatre name has been set to {tname}")
    with open('tname.txt','w') as namee:
        namee.write(tname)
    print(f"\nSuccesfully set theater name as {tname}")  
ch="Y"
while ch.upper()=="Y":
    print("We have 3 main functions\n1) Setname   :   To set the name of the theater.  \n2) Input     :   To input a show into the movies list. \n3) Book      :   To book tickets.")
    choice=int(input("Enter choice: "))
    if choice==1:
        setname()
    if choice==2:
        show_in()
    if choice==3:
        book()
    ch=input("Would you like to continue (Y/N): ")
if ch.upper()=="N":
    print("Thank you")
