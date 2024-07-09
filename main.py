import modules
import mysql.connector

while True:
  print('------Main Menu------')
  print("1.  New Admission")
  print('2.  Search Student(s)')
  print("3.  Edit Student Info")
  print("4.  Delete Student")
  print("5.  View All Students")
  print("6.  Payments")
  print("7.  Marks")
  print('8.  Close application')
  print('\n')
  choice = input('Enter your choice: ')
  if choice == '1':
    modules.add_student()
    modules.add_last_student_to_fees_table()  #adding last created student to fees and marks table
  elif choice == '2':
    modules.search_student()
  elif choice == '3':
    modules.edit_student()
    print("Success!")
  elif choice == '4':
    modules.del_student()
    print('Success')
  elif choice == '5':
    modules.view_student()
  elif choice == '6':
    modules.clear()
    print("----Fees Menu----")
    print("1. Pay Fees")
    print("2. Add New Payment Month")
    i=input("Enter Your Choice: ")
    if i =="1":
      modules.pay_fees()
    elif i =="2":
      month=input("Enter Month Name: ")
      modules.add_fee_column(month)
  elif choice == '7':
    modules.clear()
    print("----Marks Menu----")
    print("1. Add Test Marks")
    print("2. Add New Test")
    print("3. Report Card")
    i=input("Enter Your Choice: ")
    if i =="1":
      modules.add_marks()
    elif i =="2":
      test_name=input("Enter Test Name: ")
      modules.add_test_column(test_name)
    elif i=="3":
      modules.report_card()
  elif choice=="8":
    break