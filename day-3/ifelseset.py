print("welcome to rollerCoster")
height = int(input("enter your height in cm: "))

if height>=120:
    print("you can ride the roller coster")

    age=int(input("enter your age in years: "))
    if age<=12:
        print("You can not ride the roller coster")
    elif age <= 18:
        print("You can ride the roller coster pay the $7")
    else:
        print("You can ride the roller coster pay the $10")




else :
    print("you can not ride the roller coster")