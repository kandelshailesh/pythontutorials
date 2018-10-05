#Here we will be discussing about the string datatype and the operation that can be performed on the string
str1="Welcome"
str2="Buddies"
 #we can '+' operator to concatenate the string
str3=str1+str2
print(str3)
#as we can see the output as 'WelcomeBuddies'.To add gap between str1 and str2 we can use 
str3=str1+' '+str2
print(str3)

#we can strip the string use : operator
print(str1[2:]) #output lcome

print(str1[2:6]) #output  lcom

# to chop the string  from the backward
print(str1[:-2])
#output will the string from the index 2 to the (length of element+1).Index start from 0 in python

# to display the len of the string, we can use len(str) function where str is the string 
print(len(str1))
print(str1.count('d',0,len(str1)))
