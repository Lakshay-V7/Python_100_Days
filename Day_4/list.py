#here we will know about list
#list are the datastructure that help in to take same type of data under one varible means having
# arranging the items or ordering them

list_fruit = ["mango ","litchi","pineapple","banana"]
print(list_fruit[0])


# working with list we have various method accrox to work with them
# append,extend , insert ,delete etc..
# now we will see the error that is indexerror and working with bested list
# index error: common error working with list and when we print the call for the last element
### print(list_fruit[len(list_fruit)])
## this will give an error 

print(list_fruit[len(list_fruit)-1])

# now lets us talk about list inside list so what we do is

fruit =["apple" , "banana" , "mango" ,"orange" , "raspberry"]
vegitable=["potato", "bottle gaurd", "beans", "chickpeas"]

combined_list = [fruit , vegitable]
print(combined_list[0][1])