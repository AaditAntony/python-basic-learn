print("welcome to the tip calculator")
bill= float(input("what was the total bill? "))
tip = int(input("what percentage tip would you like to give? "))
people = int(input("how many people to split the bill? "))
tip_percent = tip/100
total_tip= bill*tip_percent
total_bill = bill + total_tip
bill_pre_person= total_bill/people
final_amount =round(bill_pre_person,2)
print(f"each person should pa : {final_amount}")
12345673423434