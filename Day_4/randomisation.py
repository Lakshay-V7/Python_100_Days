#here we will learn about randomisation (this help us to predict and take any random number from any range)
import random
# random nubmer between range
random_number = random.randint(1,10)
print(random_number)
# random floating point number in range
random_number1= random.random()
print(random_number1)

#now to seee working of floating point number with  in given range
random_number2= random.uniform(1,10)
print(random_number2)


# now we will se tossing a coin
tossed = random.randint(0,2)
if(tossed==0):
    print("heads")
else:
    print("tails")