from cmath import sqrt
import cmath

print("SOLUTION OF QUADRATIC EQUATION USING MATH LIBRARY OR CMATH")

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
delta=((b**2)-(4*a*c))
sol_1=((-b+sqrt(delta))/(2*a))
sol_2=((-b-sqrt(delta))/(2*a))
print("The value of delta is",delta)
print("The solution1 is",sol_1)
print("The solution2 is",sol_2)