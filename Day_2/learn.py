# This is the simplest exercise where i will use type conversion and variour data type int , float , round

print("program to calculate body mass index")

height= float(input("please tell me your height in \n"))
weight= int(input("Your weight please \n"))

bmi = weight /(height**2)

print(bmi)
print(int(bmi))
print(round(bmi)) #mathematical technique to calcute approx of floating number

# we will also know about left assign
# +=
# -=
# *=
# /=

# fstring : make it easy print different data type value in same line

print(f"your bmi is :{bmi}")
