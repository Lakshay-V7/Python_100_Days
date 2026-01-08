# here we creating a simple game using list and randomization
import random
# BANKER ROULETTE

people_list = ["Alice" ,"BoB", "Devanshu" ,"lakshay"]

#option 1
print(random.choice(people_list))

#option 2 using randint
randomnumber = random.randint(0,3)
print(people_list[randomnumber])