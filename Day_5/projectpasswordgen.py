import string
import random
# needful things 
alpha = list(string.ascii_letters)      # a-z + A-Z
symbol = list(string.punctuation)       # all special symbols
number = list(string.digits)   
# here we are at the end of day 5 with project my password generator
print("Welcome to PyPassword Generator !!")
letter = int(input("How many letter would you like in your password ?"))
symbols= int(input("How many symbols would you need ?"))
numbers= int(input("How many number needed?"))

# #easy
# password =""
# for char in range(1, letter+1):
#     password+=random.choice(alpha)
# for char in range(1, symbols+1):
#     password+=random.choice(symbol)
# for char in range(1, numbers+1):
#     password+=random.choice(number)
    
# print(password)

# Hard
password =[]
for char in range(1, letter+1):
    password.append(random.choice(alpha))
for char in range(1, symbols+1):
    password.append(random.choice(symbol))
for char in range(1, numbers+1):
    password.append(random.choice(number))

random.shuffle(password)

final_password=""
for passcode in password:
    final_password+= passcode
    
print(final_password)

#<RTK:C3>14ELosO+prjO5Z49N5
#bM0F9,F4xN*Jt!9zm1u6DT9Sz\