#Programmer: Alex Thornton
#Program: Variables and Methods
#Date: 1.11.2024

quote = "Sully is a Cornball" 
print(quote)

print(quote.upper()) #Uppercase
print(quote.lower()) #Lowercase
print(quote.title()) #Title
print(len(quote)) #length of characters in our quote

name = "Alex" #String
age = 16 #Int - Whole Number
gpa = 4.1 #Float - Has a Decimal

print(int(age))
print(int(gpa)) #Cast a float into an int 

print("\nMy name is " + name + " and I am " + str(age) + " with a GPA " + str(gpa) + ".") #Concatenate variables while casting int to str

print("\nMy name is", name ,"and I am", str(age) ,"with a GPA", str(gpa) + ".") #Concatenate variables while casting int to str

#Concatenate using a comma instead of a + while casting our gpa variable into a string to account for the spacing before the period

print("")

age += 1 #Adds one onto the variable age 
print(age)

print("")

age += 10 #Adds one onto the variable age 
print(age)

print("")

birthday = 1 
age += birthday #We can add two variables with the values as int together
print(age)
