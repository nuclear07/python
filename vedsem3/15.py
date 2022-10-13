year = int(input("enter year"))
if((year % 4 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print ("it is a leap year")
else:
    print ("it is not a leap year")