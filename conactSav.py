import db_setting as db
import os 
import time
import sys

class Contacts:
    def root(self):
            euid = os.getuid()
            if euid != 0:
                print("Only Root Allowed") 
                sys.exit()
            else:
                self.menu()

    def menu(self):
        print('#'*5,'Menu','#'*5)
        print("1.View\n2.Add\n3.Remove\n4.Edit\n5.Search\n6.Exit")
        print('-'*5,'#','-'*5)
        try:
            cho = int(input("Enter Your Choice: "))
            if(cho == 1):
                self.View()
            elif(cho == 2):
                self.Add()
            elif (cho == 3):
                self.Remove()
            elif (cho == 4):
                self.Edit()
            elif (cho == 5):
                self.Search()
            elif (cho == 6):
                self.Exit()
            else:
                print("Invalid Option")
                self.menu()
        except ValueError:
            print("Only Integer Allowed")
            self.menu()

    def View(self):
        db.show()
        self.menu()

    def Add(self):
        try:
            n = input("Enter Contact Name: ")
            p =  int(input("Enter a Contact No: "))
            e = input("Enter Contact Email id: ")
            db.Add_det(n, p, e)
            db.show()
            self.menu()
        except ValueError:
            print("Enter Form")
            self.menu()

    def Remove(self):
        
        d = int(input("Which id DO you want to Remove: "))
        print(f"Id {d} Successfully Removed")
        db.Delet_it(d)
        self.menu()

    def Edit(self):
        d = input("Which Id Do You Want to Modify: ")
        db.Modify(d)

    def Search(self):
        db.ser()
        self.menu()

    def Exit(self):
        print("Exiting...")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    c = Contacts()
    c.root()
