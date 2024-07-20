  #COMPUTER PROJECT
print("WELCOME TO HOTEL VANAKKAM " .center(150))
import csv
while True:
  print ('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
  print ("MAIN MENU      ".center(20))
  print ("1. Check Inn   ".center(25))
  print ("2. Package     ".center(25))
  print ("3. Check Out   ".center(25))
  print ("4. Payment     ".center(25))
  print ("5. Exit        ".center(25))
  print ('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
  choice=int(input("Enter your choice:"))
  if (choice==1):
      csvfile=open('record.csv','a',newline='')
      csvobj=csv.writer(csvfile)
      lines=[]

      while True:
            print("Check Inn"  .center(100))
            name=input("Enter your name: ")
            phone_no=int(input("Enter your mobile number: "))
            address=input("Enter your address: ")
            aadhar=int(input("Enter your Aadhar number: "))
            print("You've successfully checked-inn")
            lines.append([name,phone_no,address,aadhar])
            csvobj.writerows(lines)
            csvfile.close()
            break
      print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  elif (choice==2):
      print ("PACKAGE" .center(100))
      print ('*******************************************************************************************************************************************************')
      while True:
        print ("Room Category-")
        print ("1. Standard Room")
        print ("2. Queen Room")
        print ("3. King Room")
        print ("4. Charge per night")
        print ("5. Go Back to Main Menu") 
        Room_info= input("Enter the room type of which you want information:")
        if (Room_info=='1'):
            print ("May have one or more beds.The room size or area of Double Rooms are generally between 40 m² to 45 m².Room Charge- Rs. 2000/-")
            amount=2000
        elif (Room_info=='2'):
            print ("A room with a queen-sized bed.The room size or area of Queen Rooms are generally between 32 m² to 50 m². Room Charge- Rs.3500/-")
            amount=3500
        elif (Room_info=='3'):
            print ("A room with a king-sized bed.The room size or area of King Rooms are generally between 32 m² to 50 m². Room Charge- Rs.5000/-")
            amount=5000
        elif (Room_info=='4'):
            print (" Charge per night is : Rs.1000/- ")
            amount=1000
        else  :
            break
      Room_type=int(input("Enter the room type that you want to select"))
      total_amount=amount
      print ("Total amount is ",total_amount)
      print ('*******************************************************************************************************************************************************')
      while True: 
        print ("Facilities-")
        print ("1. Breakfast")
        print ("2. Lunch")
        print ("3. Dinner")
        print ("4. None")
        print ("5. Go to Main Menu")
        info=input("Enter the option of which you want some information:")
        if (info=='1'):
          print (" The charges of breakfast per plate is Rs.1500/-")
          amt=1500
        elif (info=='2'):
          print (" The charges of lunch per plate is Rs.2500/-")
          amt=2500
        elif (info=='3'):
          print (" The charges of dinner per plate is Rs.3500/-")
          amt=3500
        elif (info=='4'):
          print ("No Facilities required")
          amt=0000
        else :
          break
      facilities_type=int(input("Enter the facilities type that you want to select"))
      total_amt=amt
      print ("Total amount is ",total_amt)
      print ('********************************************************************************************************************************************************')
      print ("Billing Time")
      x=int(input("Enter the no. of night the customer stayed"))
      RC=x*1000+total_amount+total_amt
      print ('(',x,'X','1000',')','+','Room_type','+','Facilities_type','=',RC)
      print ("Dear Coustmer your Total Bill is: Rs.",RC)
      print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  elif (choice==3):
      print ("CHECK OUT" .center(100))
      room_no=input('Enter the room no. alloted')
      checkname=input("Enter your the registered name: ")
      if checkname==name:
            print("You've successfully checked-out")
      else:
            print("Wrong entry. Please check if there is a typo")
      print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')      
  elif (choice==4):
      print ("PAYMENT" .center(100))
      print ("1. By Credit/Debit card")
      print ("2. By Cash")
      print ("3. By Online Transaction ")
      method=input("Enter you method of payment ")
      if (method==1):
        print ("Hotel's Account No. is *************")
      elif (method==2):
         Amount_given=input ("Enter 'YES' or 'yes' if amount is given and 'NO' or 'no' if not given ")
         if Amount_given=='YES' or 'yes':
           print ("All Dues Are Clear Now")
         else :
           print ("Amount Not Yet Given")
      else :
         print ("Done")
         print ("Thank You for visiting our Hotel hope you like our service")
      print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  elif (choice==5):
      print ("EXIT" .center(100))
      break
