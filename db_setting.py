import sqlite3
import time
import conactSav as cv
import os

conn = sqlite3.connect('Number.db')
cur = conn.cursor()
# cur.execute('''SELECT count(rowid) FROM person WHERE type='table' AND rowid="1" ''')
c = cv.Contacts()

def CreateTable():
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()
    if cur.fetchone():
            c.menu()
    else:
        cur.execute("""CREATE TABLE person 
        (
            Name TEXT,
            PhNo INTEGER,
            Email TEXT
        )
        """)
        conn.commit()
        conn.close()

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' and name='person' ''')
if cur.fetchone()[0] == 1:
    None
else:
    CreateTable()

def show():
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid, * FROM person")
    print('-'*5,'LIST','-'*5)
    for det in cur.fetchall():
        print("ID: ", det[0])
        print("Name: ", det[1])
        print("PhNo: ", det[2])
        print("Email: ", det[3])
        print('-'*5,'-','-'*5)
    
    c = cv.Contacts()
    c.menu()


def Add_det(name, phno, email):
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO person VALUES (?,?,?)",(name, phno, email))
    conn.commit()
    conn.close()

def Delet_it(x):
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()

    cur.execute("DELETE from person WHERE rowid = (?)", (x, ))
    conn.commit()
    conn.close()

def ser():
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()
    print("Serch Via\n1.Name\n2.PhNo\n3.Email")
    s = input("Enter here: ")
    def ser_show():
        print('-'*5,'Founded','-'*5)
        for det in cur.fetchall():
            print('='*10)
            print("ID: ",det[0])
            print("Name: ", det[1])
            print("PhNo: ", det[2])
            print("Email: ", det[3])
            print('-'*5,'-','-'*5)
    def ser_name(n):
        
        cur.execute(f"SELECT rowid, * FROM person WHERE Name LIKE '{n}%'")
        ser_show()

    def ser_pho(p):
        cur.execute(f"SELECT rowid, * FROM person WHERE PhNo LIKE '{p}%'")
        ser_show()

    def ser_email(e):
        cur.execute(f"SELECT rowid, * FROM person WHERE Email LIKE '{e}%'")
        ser_show()

    if(s == '1'):
        n = input("Search via Name: ")
        ser_name(n)
    elif(s == '2'):
        p = input("Search via Phno: ")
        ser_pho(p)
    elif(s == '3'):
        e = input("Search via Email: ")
        ser_email(e)
    else:
        print("Invalid Option")
        c.menu()
    conn.commit()
    conn.close()

def Modify(row):
    conn = sqlite3.connect('Number.db')
    cur = conn.cursor()

    def name(x):
        cur.execute("""UPDATE person SET Name=? WHERE rowid =? """,(x, row))
        print("New Name Have been Changed")
        conn.commit()
        conn.close()
        show()

    def no(x):
        cur.execute("UPDATE person SET PhNo = ? WHERE rowid = ?", (x, row))
        print("New Phno Have been Changed")
        conn.commit()
        conn.close()
        show()

    def mail(x):
        cur.execute("UPDATE person SET Email = ? WHERE rowid = ?", (x, row))
        print("New Email Have been Changed")
        conn.commit()
        conn.close()
        show()

    print("What do You Need to Modify")
    print("1.Name\n2.Phno\n3.Email")
    x = int(input("Enter Your Choice: "))
    cur.execute("SELECT rowid, * FROM person")

    if x == 1:
        n = input("Enter new Name: ")
        if len(n) != 0:
            name(n)
        else:
            print("Enter a New Name or Exit Edit Section")
            c.menu()
    elif x == 2:
        o = input("Enter New PhNo: ")
        if len(o) != 0:
            no(o)
        else:
             print("Enter a New PhNo or Exit Edit Section")
             c.menu()
    elif x == 3:
        e = input("Enter a new Email: ")
        if len(e) != 0:
            mail(e)
        else:
             print("Enter a New Email or Exit Edit Section")
             c.menu()
    else:
        print("Invalid Option")
        show()
