import mysql.connector as ms
con = ms.connect(host="localhost",user="root",passwd="root",charset='utf8',database='project')
cur=con.cursor()

print("\n\n\t\t |||**** WELCOME TO AVK HOSPITAL****|||\n\n")
print("--------------------------------------------------------------------------------")
print ("\t\t\t\tLOGIN WINDOW\t\t\t\t\t\t\t")


def Doc_Menu():
    print("\t\tDOCTOR MENU!")
    print("\t\t------------")
    print("1:Create table of doctor_details ")
    print("2:Show doctor table ")
    print("3:Register Doctor Details ")
    print("4:Update Doctor details ")
    print("5:Search Doctor details ")
    print("6:Remove specific Doctor Details")
    print("7:Run Query of your choice on doctor_details table ")
    print("8:Exit")
    print("-------------------------------------------------------------------------")
    
def Patient_Menu():
    print("---------------------------------------------------------------")
    print("1:Create table patient_details ")
    print("2:Show all patient_details ")
    print("3:Register Patient details ")
    print("4:Search Patient details ")
    print("5:Update Patient details ")
    print("6:Remove specific Patient details")
    print("7:Create table Bill ")
    print("8:Show records of Bill ")
    print("9:Add Bill Details")
    print("10:Delete records of Bill ")
    print("11:Run Query of your choice on Patient table")
    print("12:Exit")
    print("-------------------------------------------------------------------------")

def Worker_Menu():
    print("\t\tWORKER MENU!")
    print("\t\t------------")
    print("1:Create table worker_details ")
    print("2:Register Worker details ")
    print("3:Display all Worker details ")
    print("4:Update Worker details")
    print("5:Search worker details")
    print("6:Remove specific worker details")
    print("7:Run Query of your choice on worker table ")
    print("8:Exit")
    print("-------------------------------------------------------------------------")

# DOCTOR DETAILS MENU
    
def Doc_Table(): #To Create Doctor's table
    cur.execute("create table if not exists doc(DOC_ID int(11),DOC_NAME char(20),DEPARTMENT char(60),SALARY int(11),Qualification char(45),PHONE_NO int(11),AGE char(10))")
    print("Table Created Successfully ")

def Doc_Show(): #To Show Doctor Table
    cur.execute("select * from doc")
    for x in cur:
        print(x)

def Add_doctor(): #To Register Doctor Details
    print("Enter New Doctor Information")
    i= int(input("Enter ID of Doctor(INT) :"))
    n=input("Enter Doctor Name(CHAR) : ")
    a=int(input("Enter Age(CHAR) : "))
    d=input("Enter the Department : ")
    p=input("Enter the Qualification : ")
    s=int(input("Enter Salary(INT): "))
    ph=int(input("Enter Phone Number : "))
    cur.execute("insert into doc values(%s,'%s','%s','%s','%s',%s,%s)"%(i,n,d,s,p,ph,a))
    con.commit()
    con.close()

def Doc_Update(): #To Update Doctor Details
    d = int(input("Enter the Doctor's ID to be modified : "))
    a = input("1.To change Doctor's Age\n2.To change Doctor's Name\n3.To change Doctor's Department\n4.To change Doctor's Phone Number\n5.To change Doctor's Salary\n")
    if a=='1':
        x = input("Enter the Doctor's new Age : ")
        cur.execute("update doc set AGE='%s' where DOC_ID = %s"%(x,d))
        con.commit()
        l=input("Do you want to see the Updated Table(Y/N):")
        if l=='Y':
            Doc_Show()
        else:
            print("Your query has been executed and updated")
  
      
    elif a=='2':
        x = input("Enter the Doctor Name(new): ")
        cur.execute("update doc set DOC_NAME = '%s' where DOC_ID = %s"%(x,d))
        con.commit()
        l=input("Do you want to see the Updated Table(Y/N):")
        if l=='Y':
            Doc_Show()
        else:
            print("Your query has been executed and updated")
    elif a=='3':
        x = input("Enter the Doctor's new Department : ")
        cur.execute("update doc set DEPARTMENT ='%s' where DOC_ID = %s"%(x,d))
        con.commit()
        l=input("Do you want to see the Updated Table(Y/N):")
        if l=='Y':
            Doc_Show()
        else:
            print("Your query has been executed and updated")
   
    elif a=='4':
        x = input("Enter the new phone Number : ")
        cur.execute("update doc set PHONE_NO ='%s' where DOC_ID = %s"%(x,d))
        con.commit()
        l=input("Do you want to see the Updated Table(Y/N):")
        if l=='Y':
            Doc_Show()
        else:
            print("Your query has been executed and updated")
    elif a=='5':
        x=int(input("Enter Doctor's new  Salary: "))
        cur.execute("update doc set SALARY=%s where DOC_ID= %s"%(x,d))
        con.commit()
        l=input("Do you want to see the Updated Table(Y/N):")
        if l=='Y':
            Doc_Show()
        else:
            print("Your query has been executed and updated")
    else :
        print(" Invalid Option!! ")
        return
    con.commit()
    con.close()

def Search_Doctor(): #To Search Doctor
    d = int(input(" Enter the ID of Doctor to be searched(int) : "))
    cur.execute("select * from doc where DOC_ID =%s"%(d,))
    x = cur.fetchone()
    if x == None:
        print(" No such Records of Doctor is found !! ")
    else:
        for i in x:
            print(i,end="\t")
        print()

def delete_doc_records(): #To Delete Records.
    l=int(input("Enter the doctor id to be deleted:"))
    if l== None:
        print("No such Doctor Id found!Please check the Doctor id you have entered")
    else:
        cur.execute("delete from doc where DOC_ID = %s" %(l,))
        print("Deleted successfully")
    
                    

def Admin_Query_doctor():
    print(" Which type of query you want to execute ? ")
    ch=int(input(" Press 1 : For Select query\n Press 2 : For Non-Select query\n"))
    if ch==1:
        s=input(" Enter your Select command Query:")
        cur.execute(s)
        if cur==[]:
            print(" :( SORRY!!! None of the records satisfied your query ")
        else:
            for i in cur:
                print(i)
                print("\n")
    elif ch==2:
        s=input(" Enter your non-select query:")
        cur.execute(s)
        con.commit()
        print("| CONGRATS!!! Query executed successfully |")
        print(" Check out the records")
        cur.execute("select * from doc")
        for i in cur:
            print(i)
            print("\n")
       
    else:
        print(" Invalid Choice!! ")
    cur.close()
    con.close()
    


# WORKER DETAILS MENU

def Worker_details(): #To Create Worker's table
    cur.execute("create table if not exists worker(WID char(10) primary key,WORKER_NAME  char(20),DEPT char(20),AGE int,PHONE_NO char(11));")
    print(":::::::::::|||||||:::::::::: Table Created Successfully :::::::::::|||||||::::::::::")

def Worker_Show(): #To Show Worker_Table
    print(" Structure of worker table ")
    cur.execute("select * from worker")
    for i in cur:
        print(i)
    con.close()

def Add_worker(): #To Add New Worker
    print(" Enter New Worker Information : ")
    i= input(" Enter ID of Worker : ")
    n=input(" Enter Worker Name : ")
    d=input(" Enter Department : ")
    a=int(input(" Enter the age of the worker : "))
    ph=input(" Enter Phone Number : ")
    cur.execute("insert into worker values('%s','%s','%s',%s,'%s')"%(i,n,d,a,ph))
    print("Worker added successfully! Here is your updated table!!")
    cur.execute("select * from worker")
    for i in cur:
        print(i)
    con.commit()
    con.close()
    

def DisplayAllWorker(): #To Display All Workers
    print(" In which order you want to display the worker_details : ")
    x=int(input(" 1: Ascending order \n 2: Descending order \n 3: As present in table\n "))
    if x==1:
        col=input(" Enter column name with respect to which you want to order the records : ")
        cur.execute("select * from worker order by %s " %(col,))
        for i in cur:
            print(i)
    elif x==2:
        col=input(" Enter column name with respect to which you want to order the records : ")
        cur.execute("select * from worker order by %s desc" %(col,))
        for i in cur:
            print(i)
    else:
        cur.execute("select * from worker")
        for i in cur:
            print(i)
            
    con.close()

def update_worker(): #To Update Worker Details
    d = input(" Enter the Worker's ID to be modified : ")
    a = input(" 1: To change the Age \n 2: To change work name \n 3: To change the phone number \n 4: To change the department\n")
    if a == '1':
        x = int(input(" Enter the new Age : "))
        cur.execute("update worker set AGE =%s where WID = '%s'"%(x,d))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Worker_Show()
        else:
            print("Your query has been executed and updated successfully")
        
    elif a=='2':
        x = input(" Enter the new Worker name : ")
        cur.execute("update worker set WORKER_NAME = '%s' where WID  = '%s'"%(x,d))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Worker_Show()
        else:
            print("Your query has been executed and updated successfully")
        

    elif a=='3':
        x = (input(" Enter the new phone number : "))
        cur.execute("update worker set PHONE_NO ='%s' where WID = '%s'"%(x,d))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Worker_Show()
        else:
            print("Your query has been executed and updated successfully")
        

    elif a=='4':
        x = input(" Enter the new department for the worker :")
        cur.execute("update worker set DEPT='%s' where WID = '%s'"%(x,d))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Worker_Show()
        else:
            print("Your query has been executed and updated successfully")
        

    else :
        print(" Invalid Option!! ")
        return
    con.commit()
    con.close()

def SearchWorker(): #To Search Worker
    d = input(" Enter the ID of worker to be searched : ")
    cur.execute("select * from worker where WID ='%s'"%(d,))
    x = cur.fetchone()
    if x == None:
        print(" No such Worker found !! ")
    else:
        for i in x:
            print(i,end="\t")
        print()


def delete_worker_records(): #To Delete Records
    l=input("Enter the Worker id to be deleted:")
    if l== None:
        print("No such Worker Id found!Please check the Worker id you have entered")
    else:
        cur.execute("delete from worker where WID = '%s'" %(l,))
        print("Deleted successfully")
    
    
    
def Admin_Query_worker():
    print(" Which type of query you want to execute ? ")
    ch=int(input(" Press 1 : For Select query\n Press 2 : For Non-Select query\n"))
    if ch==1:
        s=input(" Enter your Select command Query\n")
        cur.execute(s)
        d=cur.fetchall()
        if d==[]:
            print(" :( SORRY!!! None of the records satisfied your query ")
        else:
            for m in d:
                for n in m:
                    print(n,end="\t")
                print()
    elif ch==2:
        s=input(" Enter your non-select query:\n ")
        cur.execute(s)
        con.commit()
        print("| CONGRATS!!! Query executed successfully |")
        print(" Check out the records ")
        cur.execute("select * from worker")
        p=cur.fetchall()
        for m in p:
            print(m)
    else:
        print(" Invalid Choice !! ")

        
# PATIENT DETAILS MENU

def Add_Patient(): #To Register Patient Details
    print("Enter New Patient Information :")
    p=input("Enter patient name")
    age=int(input("Enter age"))
    pno=input("Enter phone no")
    g=input("Enter gender")
    d=input("Enter diagnosis")
    rid=input("Enter Room ID")
    pid=input("Enter Patient ID")
    cur.execute("insert into patient values('%s',%s,'%s','%s','%s','%s','%s')"%(p,age,pno,g,d,rid,pid))
    con.commit()
    con.close()



def DisplayAllPatient(): #To Display All Patients
    print(" In which order you want to display the patient_details : ")
    x=int(input(" 1: Ascending order \n 2: Descending order \n 3: As present in table \n "))
    if x==1:
        col=input(" Enter column name with respect to which you want to order the records : ")
        cur.execute("select * from patient order by %s asc" %(col,))
        for i in cur:
            print(i)
    elif x==2:
        col=input(" Enter column name with respect to which you want to order the records : ")
        cur.execute("select * from patient order by %s desc" %(col,))
        for i in cur:
            print(i)
    else:
        cur.execute("select * from patient")
        for i in cur:
            print(i)
    con.close()


def Patient_Table(): #To Create Patient's table
    cur.execute("create table if not exists patient(PATIENT_NAME char(40), AGE int(5), PHONE_NO char(10), GENDER char(20), DIAGNOSIS char(20), ROOM_ID char(30), PATIENT_ID char(30)")
    print("Table Created ")

def Patient_Show(): #To Show Patient's Table
    cur.execute("select * from patient")


def Search_Patient(): #To Search Patient
    p = input(" Enter the ID of Patient to be searched : ")
    cur.execute("select * from patient where PATIENT_ID ='%s'"%(p,))
    x = cur.fetchone()
    if x == None:
        print(" No such Records of Patient is found !! ")
    else:
        for i in x:
            print(i,end="\t")
        print()

def Patient_Update(): #To Update Patient Details
    p = int(input(" Enter the Patient's ID to be modified : "))
    a = input("1. To change patient's name\n 2. To change patient's age\n 3. To change patient's phone number\n 4. To change patient's gender\n 5. To change patient's diagnosis\n 6. To change patient's room ID\n 7. To change patient's patient ID")
    if a == 1:
        x = input("Enter the patient's new name")
        cur.execute("update patient set PATIENT_NAME = '%s' where PATIENT_ID =%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==2:
        x = int(input("Enter the patient's new age"))
        cur.execute("update patient set PATIENT_NAME = %s where PATIENT_ID =%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==3:
        x = input("Enter the patient's new phone no")
        cur.execute("update patient set PHONE_NO ='%s' where PATIENT_ID=%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==4:
        x = input(" Enter the patient's new gender")
        cur.execute("update patient set GENDER ='%s' where PATIENT_ID =%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==5:
        x = input("Enter the patient's new diagnosis")
        cur.execute("update patient set DIAGNOSIS='%s' where PATIENT_ID=%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==6:
        x = input("Enter the patient's new room ID")
        cur.execute("update patient set ROOM_ID='%s' where PATIENT_ID=%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    elif a==7:
        x = input("Enter the patient's new patient ID")
        cur.execute("update patient set PATIENT_ID='%s' where PATIENT_ID=%s"%(x,p))
        con.commit()
        l=input("Do you want to see the updated table[Y/N]?:")
        if l=='Y':
            Patient_Show()
        else:
            print("Your query has been executed and updated successfully")
    else :
        print(" Invalid Option!! ")
    return
    con.commit()
    con.close()

def Remove_Patient():
    i=input("Enter the patient's ID that you want to remove")
    cur.execute("delete from patient where PATIENT_ID='%s'"%(i,))
    print("Specified record has been Deleted Successfully")
    con.commit()
    con.close()

    
def Bill_details(): #To Create Bill
    cur.execute("create table if not exists bill(PATIENT_ID char(30),PATIENT_NAME char(40),AGE int(5),Doctor_Fee int(40),Medicines char(15),Room_Charges int(15))")
    print("Table Created ")
    
def AddBill(): #To Add Bill
    i = int(input("Enter ID of Patient : "))
    n = input("Enter Patient Name : ")
    a = int(input("Enter Patient age : "))
    d = int(input("Enter fee of Doctor's visits : "))
    m = int(input("Enter the cost of medicines : "))
    r = int(input("Enter Room charges : "))
    cur.execute("insert into bill values('%s','%s',%s,%s,%s,%s)"%(i,n,a,d,m,r))
    con.commit()
    con.close()
    
def ShowBill(): #To Show Bill
    print(" All Records of Bill ")
    cur.execute("Select * from bill ")
    for i in cur :
        for j in i:
            print(j,end="\t")
            print()
    con.close()

def DeleteBill(): #To Delete Bill
    x = input("Enter a column name of which you want to remove the details of: ")
    v = eval(input("Enter its value : "))
    if x in ("PATIENT_ID","PATIENT_NAME","AGE","Doctor_Fee","Medicines","Room_Charges"):
        cur.execute("delete from bill where '%s' = '%s'" %(x,v))
    else:
        print("Invalid Entry")
    con.commit()
    con.close()
    print("Bill Removed Successfully")

def Admin_Query_patient():
    print("Which type of query you want to execute?")
    ch=int(input("1 : Select query\n2 : Non-Select query\n"))
    if ch==1:
        s=input(" Enter your Select command Query\n")
        cur.execute(s)
        d=cur.fetchall()
        if d==[]:
            print("SORRY!!! None of the records satisfied your query")
        else:
            for m in d:
                for n in m:
                    print(n,end="\t")
                    print()
    elif ch==2:
        s=input(" Enter your non-select query:\n")
        cur.execute(s)
    con.commit()
    print("CONGRATS!!! Query executed successfully")
    print("Check out the records")
    cur.execute("select * from patient_details")
    p=cur.fetchall()
    for m in p:
        for n in m:
            print(n,end="\t")
            print()
        else:
            print(" Invalid Choice!! ")


#MAIN PROGRAM

ch=int(input("Press 1: To login as ADMIN\nPress 2: To login as USER\n\n"))
if ch==1:
    a=input("Enter Admin Password : ")
    if a == a:
        print("\n\n\t\t| WELCOME ADMIN : Here is the Menu |\n\n")
    while True:
            print("\n")
            print("1.Doc_Menu()")
            print("2.Patient_Menu()")
            print("3.Worker_Menu()")
            print("4.Exit")
            print("\n")
            n = int(input("Enter Your Choice: "))
            if n==1:
                Doc_Menu()
                m=int(input("Which operation you want to perform?:"))
                if m==1:
                    Doc_Table()
                elif m==2:
                    Doc_Show()
                elif m==3:
                    Add_doctor()
                elif m==4:
                    Doc_Update()
                elif m==5:
                    Search_Doctor()
                elif m==6:
                    delete_doc_records()
                elif m==7:
                    Admin_Query_doctor()
                elif m==8:
                    break
            elif n==2:
                Patient_Menu()
                k=int(input("Which operation you want to perform?:"))
                if k==1:
                    Patient_Table()
                elif k==2:
                    DisplayAllPatient()
                elif k==3:
                    Add_Patient()
                elif k==4:
                    Search_Patient()
                elif k==5:
                    Patient_Update()
                elif k==6:
                    Remove_Patient()
                elif k==7:
                    Bill_details()
                elif k==8:
                     ShowBill()
                elif k==9:
                    AddBill()
                elif k==10:
                    DeleteBill()
                elif k==11:
                    Admin_Query_patient()
                elif k==12:
                    break
            elif n==3:
                Worker_Menu()
                y=int(input("Which operation you want to perform?:"))
                if y==1:
                    Worker_details()
                elif y==2:
                    Add_worker()
                elif y==3:
                    DisplayAllWorker()
                elif y==4:
                    update_worker()
                elif y==5:
                    SearchWorker()
                elif y==6:
                    delete_worker_records()
                elif y==7:
                    Admin_Query_worker()
                elif y==8:
                    break
            elif n==4:
                break

                    
                    
                
                    
                    
                    

#END OF CODING



