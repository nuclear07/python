num = []
n = int(input("enter the number of marks entered"))

for i in range(0,n):
    x=int(input(num))
    num.append(x)
print("total number of marks",sum(num))
    
total = sum(num)
average = total/len(num)
print("average of marks", average)

print("--------------------------------------OR-----------------------------------------------")

num = int(input("enter the number of marks entered"))
total_num = 0
for n in range(num):
    x = int(input("enter marks :"))
    total_num += x

av = total_num/num
print("average of total marks ",av)
         
         