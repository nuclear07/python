import math

#def main():
angle = eval(input("eneter the value of angler"))
height = eval(input("eneter the value of height"))
angler = (3.14/180)*angle
length = (height / math.sin(angler) )
print("length of ladder", length)


#main()