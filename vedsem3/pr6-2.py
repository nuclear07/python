num= []
n= int(input("enter the number of element entred"))
for i in range(0,n):
    x=int(input(num))
    num.append(x)
print("printing the list",num)

pos,nev,zer= 0,0,0
for i in num:
    if i > 0:
        pos +=1
    elif nev < 0:
        nev +=1
    else:
        zer +=1

    print(" total positive number",pos)
    print("total negative number",nev)
    print("total number of zero",zer)

    odd,even= 0,0
    for i in num:
        if i%2==0:
            odd +=1
            
        else:
            even +=1
    print("odd",odd)
    print("even",even)

    total = sum(num)
    average = total/len(num)
    print("average of all number of list",average)

        
