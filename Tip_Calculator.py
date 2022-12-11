

print("Welcome to the Tip Calculator !!")

total_bill = float(input("What was the total bill? $"))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or, 15? "))
percentage = (percent_tip /100) + 1

num_people = int(input("How many people are there to split the bill ? "))

money_pay = (total_bill/num_people)*percentage

final_amt = "{:.2f}".format(money_pay)
print(f"Each person should pay : ${final_amt}")