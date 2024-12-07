import random
# import d3_project
# import my_module
# print(d3_project.choice_1)
# print(my_module.creating_a_new_module)
random_value=random.randint(12,23)
print(random_value)
random_number_0_to_1=random.random()#this gives floating number from 0 to 1(thi
                                        # s doesnt include the number li
                                        # ke 0 is included to 1 but not included)
print(random_number_0_to_1)
random_number_0_to_10=random.random()*11
print(random_number_0_to_10)
random_float=random.uniform(1,10)#this gives floating number from 0 to 1(this includ
                                                # e the number like 1 to 10 but included)
print(random_float)
##
coin_flip=random.randint(0,1)
if coin_flip ==0:
    print("heads")
else:
    print("tails")