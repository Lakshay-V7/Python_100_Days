#today we will learn about loops in python with List
fruits = ["apple" , "mango" , "stawberry"]
for fruit in fruits:
    print(fruit)

# student score

student_score =[150,200,300,500,500,123,12,345,66,5,43234,242]
#basically python is very user friendly and it has variour function for datastructure
final_sum = sum(student_score)
print(final_sum)

#now performing it using loops
sum=0
for  score in student_score:
    sum+=score

print(sum)

#now program is to calculate largest number in the list
largest = 0
for score in student_score:
    if score > largest:
        largest = score
    else:
        score = score
        
        
print(largest)


#now we will learn about loops in range function
for number in range(1,11):
    print(number)
    
# now we will see how we will breakdown in range
for numbers in range(1,11,2):
    print(numbers)
    
#adding up number 1 to 100 using loops 
sum =0
for sumup in range(1, 101):
    sum+=sumup
print(sum)
