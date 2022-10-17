weight = float(input("enter the value of weight"))
height = float(input("enter the value of height"))
bmi = weight / (height**2)
if (bmi > 25):
    print("person is over weight")
elif (bmi < 18):
    print ("person is under weight")
else:
    print ("person is healthy")
