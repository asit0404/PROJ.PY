import random
print("WELCOME TO THE APSSWORD GENERATOR")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
a=int(input("how many letters do you want in your password"))
b=int(input("how many symboles would you like"))
c=int(input("how many numbers would you like"))
password_list=[]
for asit in range (0,a):
    random_char=random.choice(letters)
    password_list+=random_char
for asit in range (0,b):
    more_random=random.choice(symbols)
    password_list+=more_random
for asit in range(0,c):
    once_more_random=random.choice(numbers)
    password_list+=once_more_random
    random.shuffle(password_list)
print(password_list)
password=""
for asit in password_list:
    password+=asit
print(f"oyur password is {password}")
