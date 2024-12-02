print("WELCOME TO THE TIP CALCULATOR!")
bill=float(input("what was the total bill $"))
tip=int(input("how much tip would youy like to give? $10,$12,$17  :"))
split=int(input("how many people will split the bill?"))
total_bill=tip/100*bill+bill/split
final_amnt=round(total_bill,2)
print(f"each person should pay {final_amnt}$")