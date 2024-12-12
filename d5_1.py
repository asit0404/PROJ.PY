fruits=["apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " asit")
    print(fruits)
#--------------------------------------------------------------------------------------------------------------
student_score=[120,123,234,878,676,998,678,876,867,677]
total=sum(student_score)
print(total)
sum=0
for scoer in student_score:
    sum+=scoer
print(sum)
#--------------------------------------------------------------------------------------------------------------
max=0
for asit in student_score:
    if asit > max:
        max=asit
print(max)
#range------------------------------------------------
for asit in range(1,11+1):
    print(asit)
#step to any number-------------------------------
for asiyt in range(1,11,2):
    print(asiyt)
# adding all 1 to 100----------------------------
sum=0
for number in range(1,101):
    sum+=number
print(sum)