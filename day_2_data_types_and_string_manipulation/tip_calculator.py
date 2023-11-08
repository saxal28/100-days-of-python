print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_paying_bill = input("How many people to split the bill? ")

percentage_tip = int(tip) / 100

total = float(total_bill) * (percentage_tip + 1) / int(people_paying_bill)
what_each_person_owes = round(total, 2)

print(f"Each person should pay ${what_each_person_owes}")
