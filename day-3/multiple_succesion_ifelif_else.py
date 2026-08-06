print("welcome to rollerCoster")
height = int(input("enter your height in cm: "))
bill=0

if height>=120:
    print("you can ride the roller coster")

    age=int(input("enter your age in years: "))
    if age<=12:
        bill=5
        print("You can not ride the roller coster")
    elif age <= 18:
        bill=7
        print("You can ride the roller coster pay the $7")
    elif age >= 45 and age <= 55 :
        print("You can ride the roller coster pay the ")
    else:
        bill=12
        print("You can ride the roller coster pay the $10")

    want_photo=input("do you whant your phot to be taken? type y for yes or n for no")
    if want_photo == "y":
     bill +=3
    print(f"your final bill :{bill}")
else:
    print("you can not ride the roller coster")



