a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
x = a if a > b else b
max = x if x > c else c
print ("maximum number is ",max)
