print("Welcome to Python Pizza Delivery !!")
size=input("what size of pizza to be ordered? S , M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("Do you need extra cheeze? Y or N: ")

bill=0
if size == "S":
    bill+=15
elif size =="M":
    bill+=20
elif size =="L":
    bill+=25

if pepperoni =="Y":
    bill+=3
elif pepperoni=="N":
    bill=bill

if extra_cheese=="Y":
    bill+=1
elif extra_cheese=="N":
    bill=bill

    print(f"Your total bill is: ${bill}")

else:
    print("Sorry Not and option in our menu.....")