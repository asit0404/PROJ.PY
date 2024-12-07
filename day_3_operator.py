print("WELCOME TO THE ROLLERCOASTER")
height=int(input("enter your height in cm :"))
if height >= 120:
    print("chal bhai")
else:
    print("go away")
#precise equal to and not equal to------(!=)
print("WELCOME TO THE ROLLERCOASTER")
height = int(input("enter your height in cm :"))
if height == 120:
    print("chal bhai")
else:
    print("go away")
a=10%3
print(a)
print("WELCOME TO ODD EVEN FINDER")
number=int(input("ENTER THE NUMBER"))
if number%2==2:
    print("even number")
else:
    print("odd number")
    #NESTED LOOP
print("WELCOME TO THE ROLLERCOASTER")
height=int(input("enter your height in cm :"))
age = int(input("enter the age"))
if height >= 120:
    print("chal bhai")
    if age<=18:
        print("please pay $7")
    else:
        print("please pay $12")

else:
    print("go away")
 #   elif(HERE INTENDED)
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
    else:
        bill=12
        print("please pay $12")
    pic=input("do you want a photo : say in yes or no :")
    if pic=="yes":
        bill+=3
    else:
        print("enjoy the ride")
    print(f"your total bill is ${bill}")
else:
    print("go away")

 #question
weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi>=18.5:
    print("normal weight")
elif bmi>=25.0:
        print("overweight")
else:
    print("go diet")