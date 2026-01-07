# THE TREASURE ISLAND GAME (Correct choice get you closer to the tresure)
print("Welcome to Tresure Island. \n Your mission is to find the tresure.")
print("Lets take the decision and make it to the tresure.")
option = input("where do you want to go.... left or right?\n")
if option == "left":
    print("move on.. you are near to the lake now..\n do you want to wait or swin the lake")
    wait_or_swim = input("wait or swim...by the way there is a island near by and boat is comming\n")
    if wait_or_swim == "wait":
        print("boat is here you can go to the island")
        open_door=input("you are close to tresure tell me which door to go RED or YELLOW\n")
        if open_door=="RED":
            print("EUREKA YOU WON")
        else:
            print("GAME OVER")
    elif wait_or_swim =="swim":
        print("GAME OVER")

else:
    print("GAME OVER")   
    