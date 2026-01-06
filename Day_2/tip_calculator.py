print("Welcome to tip calculator !!")

bill=float(input("What was the total bill? $ "))
percentage= float(input("how much percentage would you like to give? 10 ,12 or 15 \n"))
split= int (input("how many people to split the bill\n"))

total_bill= ((bill*percentage)/100)+bill
print(f"Your total bill is :{total_bill}$")
splitting= total_bill/split
print(f"Your split is :{splitting}$")

print("Thankyou and visit again")