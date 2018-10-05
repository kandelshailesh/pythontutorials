#Here we will be discussing how we can take input from the user and
#display output to the user

#Python provides input() function for taking the user input and print() function for displaying the output

a=input()

#when this code is run , program will be paused to retrieve the input from the user . By default , the datatype of the variable is considered as string
#and but we can use typeconversion to get value in the respective datatype

print(type(a))

#output will be str

a=int(input())

print(type(a))


#We can even use string inside the parenthisis of the input() to retrieve the value from the user . Best way is to write the string which better explains the
#for what purposes we are retrieving the value which make it easier for the user to provide the value

firstname=input("Enter firstname")
print(firstname)
