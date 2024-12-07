print("WELCOME TO THE ROLLERCOASTER")
height=int(input("enter your height in cm :"))
age = int(input("enter the age"))
bill=0
if height >= 120:
    print("chal bhai")
    if age<=12:
        bill=5
        print("please pay $5")
    elif age<=18:
        bill=7
        print("please pay $7")
    elif age>=45 and age<=55:
        print("you got the ride free")
        bill-=3
    else:
        bill = 12
        print("please pay $12")
    pic=input("do you want a photo : say in yes or no :")
    if pic=="yes":
        bill+=3
    else:
        print("enjoy the ride")
    print(f"your total bill is ${bill}")
else:
    print("go away")
