print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people_to_split = int(input("How many people to split the bill?"))
tip_per_person = float(tip_percent / 100 * total_bill / people_to_split)
split_bill = total_bill / people_to_split
bill_per_person = split_bill + tip_per_person
total_bill_per_person = round((bill_per_person),2)
print(f"Each person should pay: {total_bill_per_person}")