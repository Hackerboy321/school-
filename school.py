import mysql.connector
dk= mysql.connector.connect(host = 'localhost' , password = 'dkbose', user = 'u0_a623', database = 'HGS_SCHOOL' )


def menu(): 
      ch =  input("Do you want go no menu [ y/n]")
      if ch == "y":
       main()
def thanku():
        print("            ", "•"*40)
        print("                                  Thank you")
        print("            ", "•"*40)

def AddS():
    print("-"*50)
    N = input("Enter Name :- ")
    print("•"*50)
    C = int(input("Enter Class :- "))
    print("•"*50)
    R = int(input("Enter Roll.No :- "))
    print("•"*50)
    S = input ("Enter Section :- ")
    print("•"*50)
    N = int(input("Enter Phone Number :- "))
    print("•"*50)
    A = input("Address :- ")
    print("-"*50)
    info = (N,C,R,S,N,A)
    sql = "insert into student values(%s, %s,%s,%s,%s,%s)"
    car = dk.cursor()
    car.execute(sql,info)
    dk.commit()
    
def RemS():
    print("-"*50)
    N = input("Name :- ")
    print("•"*50)
    C = int(input("Class :-  "))
    print("•"*50)
    R= int(input("Roll No :- "))
    print("-"*50)
    info = (N,C,R)
    sql = "Delete for student where Name = %s and Class = %s and Roll_No = %s"
    car = dk.cursor()
    c.execute(sql,info)
    dk.commit()
    
def aadt():
     print("-"*50)
     N = input("Name :-" )
     print("•"*50)
     P = input("Post :- ")
     print("•"*50)
     S = input ("subject :- ")
     print("•"*50)
     Sa = int(input("Salary :-"))
     print("•"*50)
     Add = input("Address :- ")
     print("•"*50)
     Ph = int(input("Phone Number :- "))
     print("-"*50)
     info = (N,P,S,Sa,Add,Ph)
     sql = "Insert into Teacher values(%s,%s,%s,%s,%s,%s)"
     car = dk.cursor()
     c.execute(sql,info)
     dk.commit()
     
def Remt(): 
     print("-"*50)
     N = input("Name :- ")
     print("•"*50)
     Ph = int(input("Phone number :- "))
     print("-"*50)
     sql = "Delete from Teacher where Name = %s and Phone Number =%s"
     car = dk.cursor()
     c.execute(sql,info)
     dk.commit()
     
def fees():
    print("-"*50)
    N = input("Name :- ")
    print("•"*50)
    C = int(input("Class :- "))
    print("•"*50)
    R = int(input("Roll.No :- "))
    print("•"*50)
    S = input("Section :- ")
    print("•"*50)
    M = input( "moths Years :- ")
    print("•"*50)
    F = input("Fees :- ")
    print("•"*50)
    Date = input("Date :- ")
    print("-"*50)
    info = (N,C,R,S,M,F,Date)
    sql = "Insert into Fees values(%s,%s,%s,%s,%s,%s)"
    car = dk.cursor()
    c.execute(sql,info)
    dk.commit()
    
def classatt():
    print("-"*50)
    d = input("Date :- ")
    print("•"*50)
    C = input("Class :- ")
    print("•"*50)
    ab = input("Number of Absent Student")
    print("-"*50)
    data = (d,cl,ab)
    sql ="insert into attendance values(%s,%s,%s)"
    car = dk.cursor()
    c.execute(sql,info)
    dk.commit()
    
    
     
     
def main():
   print("        Harmann Gmeiner School Bhimtal                 ")
   print("             >--------------------------------------<")
   print ("""          1. Add Student           2. Remove teachers
          3. Add Teachers        4. Remove teachers
          5. Submit Fees           6. Pay salary
          7. Class Attendence  8. Teachers Attendence
          9. Display Class       10. Teachers List""")
   print("             >--------------------------------------<")        
   ch = int(input("               Please Enter you choose :-"))
   print("•"*50)
   if ch == 1:
      print("•"*50)
      print("Do you want you add a new student [y/n]")
      print("•"*50)
      ch1 = input("Enter You Choose :- ")
      if ch1== "y":
       AddS()
       print("            ", "•"*40)
       print("                   Student add successfully")
       print("            ", "•"*40)
       menu()
      else:
       menu()
   if ch == 2:
       print("Do you want removed student [y/n]")
       ch1 = input("Enter You Choose :- ")
       if ch1 == "y":
        RemS()
        print("            ", "•"*40)
        print("         Student Removed successfully")
        print("            ", "•"*40)
        menu()
       else:
        menu()
       
   if ch == 3:
       print("Do you want add Teacher  [y/n]")
       ch1 = input("Enter You Choose :- ")
       if ch1 == "y":
        aadt()
        print("            ", "•"*40)
        print("                   Teacher add successfully")
        print("            ", "•"*40)
        menu()
       else:
        menu()
        
   if ch == 4:
        print("Do you want Removed Teacher  [y/n]")
        ch1 = input("Enter You Choose :- ")
        if ch1 == "y":
         Remt()
         print("            ", "•"*40)
         print("                   Teacher Removed successfully")
         print("            ", "•"*40)
         menu()
        else:
         menu()
         
   if ch == 5:
        print("•"*50)
        print("Do you want to submit you fees  [y/n]")
        print("•"*50)
        ch1 = input("Enter You Choose :- ")
        if ch1 == "y":
         fees()
         print("            ", "•"*40)
         print("                   Fees submitted successfully")
         print("            ", "•"*40)
         menu()
        else:
         menu()
         
         
         
         
         
         
         
         
         
 
main()             
thanku()       
