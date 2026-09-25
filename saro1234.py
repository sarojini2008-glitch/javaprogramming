print("welcome to bank")
amount=5000
a=in6+put("Enter the name :")
b=input("Enter the password:")
if (a=="saro" and b=="sa"):
    print("Login successfull\nwelcome to bank\nyour account balance is 5000")
    while(True):
       c=input("do you want to deposite press y")
       if (c=="y"):
          dep=int(input("enter the Amount to deposite"))
          amount+=dep
          print("your account balance is ",amount)
       else:
           print("Thank you for banking with us ")
           break
    else:
        print("Login failed ",a)
