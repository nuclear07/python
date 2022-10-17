hour = int(input("enter hours worked"))
if (hour <= 40):
    print (hour * 100)
else:
    extra = (hour - 40)
    z = (extra * 50) + 4000
    print(z)
    
