for asit in range(1,101):
    # print(asit)
    if asit%3==0 and asit%5==0:
        print("fizz buzz")
    elif asit %3 == 0:
        print("fizz")
    elif asit%5==0:
        print("buzz")
    else:
        print(asit)