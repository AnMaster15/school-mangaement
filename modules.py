import pandas as pd
 
 
#search student
def search_student():
  clear()
  while True:
    query=input("Search Student: ")
    sql="select * from STUDENTS WHERE Name LIKE '%{}%';".format(query)
    mycon=mysql()
    df=pd.read_sql(sql, mycon)
 
 
    if df.empty:
      print('Sorry, No Results Found')
      again=input("\nEnter to go back OR 'S' to search again: ")
      if again=='s' or again=='S':
        continue        #Start the while loop again
      else:
        return "empty"
    else:
      print(df)
      again=input("\nEnter to continue OR 'S' to search again: ")
      if again=='s' or again=='S':
        continue
      else:
        return df
 
 
 
#Add Student
def add_student():
  clear()
  print("----Add Student Menu----")
  name=input("Enter Student Name: ")
  if name=="":
    clear()
    print("Exiting...")
    return
  while True:
    standard=input("Enter Class: ")
    if verify('class', standard):
      break
    else:
      print("Invalid Class! Try Again")
  while True:
    section=input("Section(A-E): ").upper()
    if verify('section', section):
      break
    else:
      print("Invalid Section! Try Again")
  while True:
    dob=input("Enter DOB(yyyy-mm-dd): ")
    if verify('dob',dob):
      break
    else:
      print("Invalid Date Format! Try again")
  fname=input("Father's Name: ")
  mname=input("Mother's Name: ")
 
  if fname=="":
    fname="NA"
  if mname=="":
    mname="NA"
 
  clear()
  sql = f"INSERT INTO STUDENTS (Name, Class, Section, DOB, Father_Name, Mother_Name) VALUES ( '{name}',{standard},'{section}','{dob}','{fname}','{mname}' );"
  mycon=mysql()
  mycursor = mycon.cursor()
  mycursor.execute(sql)
  mycon.commit()
  print(f'''{name} Added Successfully
Class: {standard}-{section}
DOB: {dob}
Father's Name: {fname}
Mother's Name: {mname}
\n\n\n''')
 
 
 
#View all students
def view_student():
  clear()
  mycon=mysql()
  df=pd.read_sql("select * from STUDENTS", mycon)
  print(df)
  input("\nEnter to continue")
  clear()
 
 
 
#delete student
def del_student():
  clear()
  df=search_student()         #pandas dataframe of search results
  try:
    if df=="empty":
      return
  except:
    pass
  while True:
    adm_no=input("Enter AdmNo to DELETE(OR enter to cancel): ")   #AdmNo to delete
    if adm_no=="":
      clear()
      print("Entering Main Menu...")
      break
    try:
      int(adm_no)
    except:
      print("AdmNo should be integer! Try Again")
      continue
 
    sql="select * from Students where admno={}".format(adm_no)
    mycon=mysql()
    df=pd.read_sql(sql, mycon)
    if df.shape[0] != 1:  #there should be exactly one student
      print("Invalid AdmNo! Try Again")
      continue
    student=df.loc[0]
    confirm=input(f"Do you want to delete {student['Name'].upper()}, Class: {student['Class']}?(y/n): ")
    if confirm == 'y' or confirm =='Y':
      sql="DELETE FROM STUDENTS WHERE AdmNo={};".format(str(adm_no))
      mycursor = mycon.cursor()
      mycursor.execute(sql)
      mycon.commit()
      input("Success!\nEnter to Continue")
      break
 
 
#edit student
def edit_student():
  clear()
  df=search_student()
  while True:
    adm_no=input("Enter AdmNo(OR Enter to cancel): ")
    if adm_no=="":
      clear()
      print("Entering Main Menu...")
      return
    try:
      adm_no=int(adm_no)
    except:
      print("AdmNo should be Integer! Try Again")
      continue
    sql="select * from Students where admno={}".format(adm_no)
    mycon=mysql()
    mycursor = mycon.cursor()
    df=pd.read_sql(sql, mycon)
    if df.shape[0] != 1:  #there should be exactly one student
      print("Invalid AdmNo! Try Again")
      continue
    else:
      break
 
  student=df.loc[0]
  name=student['Name']
  standard=student['Class']
  section=student['Section']
  dob=student['DOB']
  f_name=student['Father_Name']
  m_name=student['Mother_Name']
 
  while True:
    clear()
    print("Edit Student Info\n")
    print(f'''
1. Name: {name}
2. Class: {standard}
3. Section: {section}
4. DOB: {dob}
5. Father's Name: {f_name}
6. Mother's Name: {m_name}
''')
    choice=input("Enter Number to Edit (OR Enter to Cancel): ")
    if choice == '1':
      new_name= input("Name (OR Leave Empty to Cancel) : ")
      if new_name == "":
        continue
      name=new_name
      sql="UPDATE STUDENTS SET Name = '{}' WHERE AdmNo={};".format(name, adm_no)
      mycursor.execute(sql)
      mycon.commit()
 
    elif choice == '2':
      while True:
        new_standard = input("Class (OR Leave Empty to Cancel) : ")
        if new_standard == "":
          break
        if verify('class',new_standard) == False:
          print("Inavlid Class! Try Again")
          continue
        else:
          standard=new_standard
          sql="UPDATE STUDENTS SET Class = {} WHERE AdmNo={};".format(standard, adm_no)          
          mycursor.execute(sql)
          mycon.commit()
          break
    elif choice == '3':
      while True:
        new_section= input("Section (OR Leave Empty to Cancel) : ").upper()
        if new_section == "":
          break
        if verify('section',new_section) == False:
          print("Section should be A-E! Try Again")
          continue
        else:
          section=new_section
          sql="UPDATE STUDENTS SET Section = '{}' WHERE AdmNo={};".format(section, adm_no)
          mycursor.execute(sql)
          mycon.commit()
          break
 
    elif choice == '4':
      while True:
        new_dob= input("DOB (OR Leave Empty to Cancel) : ")
        if new_dob == "":
          break
        if verify('dob',new_dob) == False:
          print("Invalid Date! Try Again")
          continue
        else:
          dob=new_dob
          sql="UPDATE STUDENTS SET DOB = '{}' WHERE AdmNo={};".format(dob, adm_no)
          mycursor.execute(sql)
          mycon.commit()
          break
 
    elif choice == '5':
      new_f_name= input("Father's Name (OR Leave Empty to Cancel) : ")
      if new_f_name == "":
        continue
      f_name=new_f_name
      sql="UPDATE STUDENTS SET Father_Name = '{}' WHERE AdmNo={};".format(f_name, adm_no)          
      mycursor.execute(sql)
      mycon.commit()
    elif choice == '6':
      new_m_name= input("Mother's Name (OR Leave Empty to Cancel) : ")
      if new_m_name == "":
        continue
      m_name=new_m_name
      sql="UPDATE STUDENTS SET Mother_Name = '{}' WHERE AdmNo={};".format(m_name, adm_no)    
      mycursor.execute(sql)
      mycon.commit()
    else:
      return
 
 
 
 
 
 
 
 
#Clear Screen
def clear():
  import os
  os.system('cls' if os.name == 'nt' else 'clear')
 
 
#connect mysql
def mysql():
  import mysql.connector as sqltor
  mycon = sqltor.connect(
    host="localhost",
    user="root",
    password="ANCHIT2002mehra",
    database="School"
  )
  if mycon.is_connected():
    return mycon
  else:
    print("MySql Connection Failed")
    input()
 
#verify inputs(class, section,  dob)
def verify(input_type,input):
    '''eg 1.verify('class','12') ==> True
        2. verify('class','13') ==> False'''
    if input_type=='class':
        #is class int?
        try:
            int(input)
        except:
            return False
        #is class <=12 and >0:
        if int(input)<=12 and int(input)>0:
            return True
        else:
            return False
    elif input_type=='section':
        #is section A-E?
        if input.lower() in ['a','b','c','d','e']:
            return True
        else:
            return False
    elif input_type=='dob':
        if len(input)==10:
            return True
        else:
            return False 
 
 
 
def add_test_column(test_name):
  sql='''ALTER TABLE Marks ADD `{}` char(3) DEFAULT 'NA';'''.format(test_name)
  mycon=mysql()
  mycursor = mycon.cursor()
  mycursor.execute(sql)
  mycon.commit()
  print("Success!")
 
def add_fee_column(month):
  sql='''ALTER TABLE Payments ADD `{}` char(1) DEFAULT 'N';'''.format(month)
  mycon=mysql()
  mycursor = mycon.cursor()
  mycursor.execute(sql)
  mycon.commit()
  print("Success!")
 
 
 
def pay_fees():
  clear()
  print("---Pay Fees---")
  df=search_student()         #pandas dataframe of search results
  try:
    if df=="empty":
      return
  except:
    pass
  while True:
    adm_no=input("Enter AdmNo (OR enter to cancel): ")   #AdmNo to delete
    if adm_no=="":
      clear()
      print("Entering Main Menu...")
      return
    try:
      int(adm_no)
    except:
      print("AdmNo should be integer! Try Again")
      continue
 
    sql="select * from Students where admno={}".format(adm_no)
    mycon=mysql()
    df=pd.read_sql(sql, mycon)
    if df.shape[0] != 1:  #there should be exactly one student
      print("Invalid AdmNo! Try Again")
      continue
    else:
      break
  student=df.loc[0] #dataframe containing student info from 'Students Table'
  student_name=student['Name']
  sql="select * from Payments where admno={}".format(adm_no)
  df=pd.read_sql(sql, mycon)
  student_fees_series=df.loc[0]      #series containing student fees info from 'Payments Table'
  clear()
  print("---"+student_name+"'s Payment History---\n")
  counter=0
  for index, value in student_fees_series.items():
    if index !='AdmNo' and index !="Name" and value !='*':
      print(index +" : "+ value)
      counter=counter+1
  if counter==0:
    print("This is a New Student. No Fees History Available")
    return
 
  while True:
    month=input("Enter Month to Pay Fees(OR Enter to Cancel): ")
    if month=="":
      return
    if month not in student_fees_series.index:
      print("Wrong Month! Try Again")
      continue
    else:
      break
  sql="UPDATE Payments SET `{}` = 'Y' WHERE AdmNo={};".format(month, str(adm_no))
  mycursor = mycon.cursor()
  mycursor.execute(sql)
  mycon.commit()
  input("Success!\nEnter to Continue")
 
 
 
 
 
def add_marks():
  clear()
  print("---Add Marks---")
  df=search_student()         #pandas dataframe of search results
  try:
    if df=="empty":
      return
  except:
    pass
  while True:
    adm_no=input("Enter AdmNo (OR enter to cancel): ")   #AdmNo to delete
    if adm_no=="":
      clear()
      print("Entering Main Menu...")
      break
    try:
      int(adm_no)
    except:
      print("AdmNo should be integer! Try Again")
      continue
 
    sql="select * from Students where admno={}".format(adm_no)
    mycon=mysql()
    df=pd.read_sql(sql, mycon)
    if df.shape[0] != 1:  #there should be exactly one student
      print("Invalid AdmNo! Try Again")
      continue
    else:
      break
  student=df.loc[0] #dataframe containing student info from 'Students Table'
  student_name=student['Name']
  sql="select * from Marks where admno={}".format(adm_no)
  df=pd.read_sql(sql, mycon)
  student_marks_series=df.loc[0]      #series object containing student marks info from 'Marks Table'
  clear()
  print("---"+student_name+"'s Marks History---\n")
  counter=0
  for index, value in student_marks_series.items():
    if index !='AdmNo' and index !="Name" and value !='*':
      print(index +" : "+ value)
      counter=counter+1
  if counter==0:
    print("This is a New Student. No Marks History Available")
    return
 
  while True:
    test_name=input("Enter Test Name (OR Enter to Cancel): ")
    if test_name=="":
      return
    if test_name not in student_marks_series.index:
      print("Wrong Test Name! Try Again")
      continue
    else:
      break
  while True:
    marks = input("Enter Marks: ")
    #check if marks is integer and <= 100
    try:
      marks=int(marks)
      if marks<=100:
        break
      else:
        print("Marks should be atmost 100! Try Again")
        continue
    except:
      print("Marks should be integer! Try Again")
  sql="UPDATE Marks SET `{}` = '{}' WHERE AdmNo={};".format(test_name, marks,str(adm_no))
  mycursor = mycon.cursor()
  mycursor.execute(sql)
  mycon.commit()
  input("Success!\nEnter to Continue")
 
 
 
 
 
 
 
 
 
 
def add_last_student_to_fees_table():
  sql="select AdmNo,Name from Students ORDER BY AdmNo DESC LIMIT 1;"
  mycon=mysql()
  df=pd.read_sql(sql, mycon)
  admno=str(df.iloc[0,0])  #admno of last added student
  name=str(df.iloc[0,1])    #name of last added student
  #create new record with this admno in Payments and marks table
  for table_name in ['Payments','Marks']:
    sql="INSERT INTO {} (AdmNo,Name) VALUES ({},'{}');".format(table_name,admno,name)
    mycursor = mycon.cursor()
    mycursor.execute(sql)
    mycon.commit()
    #put all fee/marks columns before this student's admission to '*'.
    sql="SHOW COLUMNS FROM {};".format(table_name)
    df=pd.read_sql(sql, mycon)
    column_names = df['Field'].tolist()   #list of all columns of fees table i.e ['AdmNo', "january","feb"....]
    for column_name in column_names:
      if column_name !='AdmNo' and column_name!='Name':
        sql="UPDATE {} SET `{}` = '*' WHERE AdmNo = {};".format(table_name,column_name,admno)
        mycursor.execute(sql)
        mycon.commit()
 
 
 
def report_card():
  import numpy as np
  while True:
    standard = input("Enter Class(1-12) to compile result: ")
    try:
      standard=int(standard)
      if standard <=12 and standard >=1:
        break
      else:
        print("Class should be 1-12! Try Again")
    except:
      print("Class should be 1-12! Try Again")
  sql="select AdmNo from students where Class = {};".format(str(standard))
  mycon=mysql()
  df=pd.read_sql(sql, mycon)
  a=df['AdmNo'].tolist()   #list of all AdmNo of selected class
  if a==[]:
    print("No Students Found!")
    return
  sql="select * from marks where AdmNo in ({});".format(str(a)[1:-1])  #converting [2,3,4] format to (2,3,4) format. For Mysql Syntax
  df=pd.read_sql(sql, mycon)
  df.drop('AdmNo', inplace=True, axis=1)
  df=df.replace(to_replace =["*", "NA"], value =np.nan)   #If any student's marks is missing, replace it with NaN(to exclude it in average marks).
  df = df.apply(pd.to_numeric,errors="ignore")  #convert string values to integer to calculate mean
  new_df=df[:]
  df['Mean'] = new_df.mean(axis=1,numeric_only=True)
  df = df.sort_values('Mean', ascending=False)  #sort by average marks
  df['Total'] = new_df.sum(axis=1,numeric_only=True)

  print(df)
 